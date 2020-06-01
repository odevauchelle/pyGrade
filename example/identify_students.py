import json
import sys
sys.path.append('./../')

import pyGrade as grd

file_path = '../homework/graded_homework_khalo_rivera.pdf'

document = open( file_path, "rb")

with open('../students/students.json') as the_file :
    students = json.load(the_file)

for i in grd.IdentifyStudent( students, document, expected_number_of_students = 2 ) :
    print( students[i]['lastname'] )
