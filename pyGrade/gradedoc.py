
from pdfreader import PDFDocument, SimplePDFViewer
import PyPDF2

import re


defaut_point_flags = ('%','%')

def ParsePointString( point_string, point_flags = defaut_point_flags ):

	'''
	points, point_string = ParsePointString( point_string, point_flags = defaut_point_flags )
	'''

	try :
		point_strings = re.search( '.*'.join( point_flags ), point_string ).group(0).split('%') #

		try :
			points = 0
			for point_string in point_strings :
				try :
					points += float( point_string )
				except :
					pass

			return points, point_strings

		except :
			return None, point_strings

	except :
		return None, None


def GradePage( strings, verbose = True, point_flags = defaut_point_flags  ) :
	'''
	grade = GradePage( page_canvas, verbose = True, point_flags = defaut_point_flags )
	'''
	grade = 0

	for string in strings :

		points, point_string = ParsePointString( string, point_flags = point_flags )

		if not points is None :

			grade += points

			if verbose :
				print( string )

	return grade

def GradeDocSafe(document, verbose = False, point_flags = defaut_point_flags ) :

	'''
	grade = GradeDoc(document, verbose = False, point_flags = defaut_point_flags )
	'''

	doc = PDFDocument( document )
	viewer = SimplePDFViewer( document )

	grade = 0

	for page_number, page in enumerate( doc.pages() ) :

		if verbose :
			print('------------------')
			print('Page:', page_number + 1 )

		viewer.navigate( page_number + 1 )
		viewer.render()

		grade += GradePage( viewer.canvas.strings, verbose = verbose, point_flags = point_flags )

	return grade

def GradeDoc( document, verbose = False, point_flags = defaut_point_flags ) :

	'''
	grade = GradeDoc(document, verbose = False, point_flags = defaut_point_flags )
	'''

	read_pdf = PyPDF2.PdfFileReader( document )

	grade = 0

	for page_number in range( read_pdf.getNumPages() ) :

		if verbose :
			print('------------------')
			print('Page:', page_number + 1 )

		page = read_pdf.getPage( page_number )
		page_text = page.extractText().split('\n')
		grade += GradePage( page_text, verbose = verbose, point_flags = point_flags )

	return grade

if __name__ == '__main__':


	for point_string in ['%4%','%5', 'toto %6%hdsfouze_ç %56%rotio%'] :
		print( point_string,'parsed to',  ParsePointString( point_string ) )

	document = open('../homework/graded_homework_khalo_rivera.pdf', "rb")

	print('Total grade:', GradeDoc(document))
