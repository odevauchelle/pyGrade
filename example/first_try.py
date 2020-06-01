import sys
sys.path.append('./../')

import pyGrade as grd

document = open('../homework/graded_homework_khalo_rivera.pdf', "rb")

print( grd.GradeDoc(document) )
