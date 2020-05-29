import sys
sys.path.append('./../')

import pyGrade as grd

document = open('../homework/graded_homework.pdf', "rb")

print( grd.grade_document(document) )
