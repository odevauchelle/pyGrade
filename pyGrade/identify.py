from pdfreader import SimplePDFViewer
from fuzzywuzzy import fuzz, process
import numpy as np
import PyPDF2

equivalent_to_space = ['.', ',', '_', '/']

def GetFrontPageText( document, ID_page = 0 ) :

    read_pdf = PyPDF2.PdfFileReader( document )
    page = read_pdf.getPage(ID_page)
    page_text = page.extractText()

    if len(page_text) == 0 :

        viewer = SimplePDFViewer( document )
        viewer.navigate( ID_page + 1 )
        viewer.render()

        page_text = ''.join( viewer.canvas.strings )

    return page_text

def LastnameFilter(lastname) :

    lastname_pieces = lastname.split(' ')
    lastname = lastname_pieces[ np.argmax( [ len(piece) for piece in lastname_pieces ] ) ]

    return lastname

def IdentifyStudent( students, document, ID_page = 0, expected_number_of_students = 1, minimum_score = 50, debug_mode = False ) :

    '''
    student_indices = IdentifyStudent( students, document, ID_page = 1, expected_number_of_students = 1 )
    '''
    names =  [ LastnameFilter( student['lastname'] ) for student in students ]

    page_text = GetFrontPageText( document, ID_page = ID_page )

    filename_text = ' ' + document.name

    for character in equivalent_to_space :

        filename_text = filename_text.replace( character, ' ' )

    if debug_mode :
        print(page_text)

    winner_index = []

    for winner in process.extract( page_text + filename_text, names, limit = expected_number_of_students  ) :
        if winner[1] >= minimum_score :
            winner_index += [ names.index( winner[0] ) ]

    return winner_index
