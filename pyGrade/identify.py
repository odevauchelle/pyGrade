from pdfreader import SimplePDFViewer
from fuzzywuzzy import fuzz
import numpy as np

default_ID_keys = ['lastname', 'firstname']

default_ScoreMixer = np.mean

def default_name_filter(name) :
    return name.replace(' ', '').lower()

default_page_filter = default_name_filter

def GetMatchingScore( student, page_text, ID_keys = None, score_mixer = None, name_filter = None, page_filter = None ) :
    '''
    matching_score = get_matching_score( student, page_text, ID_keys = None, score_mixer = None )
    '''

    if ID_keys is None :
        ID_keys = default_ID_keys

    if score_mixer is None :
        score_mixer = default_ScoreMixer

    if name_filter is None :
        name_filter = default_name_filter

    if page_filter is None :
        page_filter = default_page_filter

    matching_score = []

    for ID_key in ID_keys :

        matching_score += [ fuzz.partial_ratio( page_filter( page_text ), name_filter( student[ID_key] ) ) ]

    return score_mixer( np.array( matching_score ) )


def IdentifyStudent( students, document, ID_page = 1, expected_number_of_students = 1 ) :

    '''
    student_indices = IdentifyStudent( students, document, ID_page = 1, expected_number_of_students = 1 )
    '''

    viewer = SimplePDFViewer( document )

    viewer.navigate( ID_page )
    viewer.render()
    page_text = ''.join( viewer.canvas.strings )

    matching_score = []

    for student in students :

        matching_score += [ GetMatchingScore( student, page_text ) ]

    # return students[ np.argsort(matching_score)[:expected_number_of_students] ]

    print( default_page_filter( page_text ) )
    print(np.sort(matching_score)[::-1])

    return np.argsort(matching_score)[-expected_number_of_students:]
