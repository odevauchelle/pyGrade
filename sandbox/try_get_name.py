from pdfreader import PDFDocument, SimplePDFViewer
from fuzzywuzzy import fuzz
import numpy as np
import json
# from difflib import get_close_matches


default_ID_keys = ['lastname']

default_score_mixer = np.mean

def get_matching_score( student, page_text, ID_keys = None, score_mixer = None ) :
    '''
    matching_score = get_matching_score( student, page_text, ID_keys = None, score_mixer = None )
    '''

    if ID_keys is None :
        ID_keys = default_ID_keys

    if score_mixer is None :
        score_mixer = default_score_mixer

    matching_score = []

    for ID_key in ID_keys :
        matching_score += [ fuzz.partial_ratio( page_text, student[ID_key] ) ]

    return score_mixer( np.array( matching_score ) )

def identify_student( students, document, ID_page = 1, expected_number_of_students = 1 ) :

    viewer = SimplePDFViewer( document )

    viewer.navigate( ID_page )
    viewer.render()
    page_text = ''.join( viewer.canvas.strings )

    matching_score = []

    for student in students :

        matching_score += [ get_matching_score( student, page_text ) ]

    # return students[ np.argsort(matching_score)[:expected_number_of_students] ]

    return [ students[ index ] for index in np.argsort(matching_score)[-expected_number_of_students:] ]


file_path = '../homework/graded_homework_khalo_rivera.pdf'

document = open( file_path, "rb")

students = [
    {"firstname":"Frida","lastname":"Kahlo","idnumber":"9584785904"},
    {"firstname":"Diego","lastname":"Rivera","idnumber":"95856545904"},
    {"firstname":"Aimée","lastname":"Césaire","idnumber":"95853453404"}]

with open('students.json', 'w') as the_file :
    json.dump(students, the_file)

print( identify_student( students, document, expected_number_of_students = 2 ) )
