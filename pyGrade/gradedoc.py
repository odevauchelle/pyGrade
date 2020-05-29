
from pdfreader import PDFDocument, SimplePDFViewer
import re


defaut_point_flags = ('%','%')

def ParsePointString( point_string, point_flags = defaut_point_flags ):

	'''
	points, point_string = ParsePointString( point_string, point_flags = defaut_point_flags )
	'''

	try :
		point_string = re.search( '.*'.join( point_flags ), point_string ).group(0)

		try :
			points = float( point_string[1:-1] )
			return points, point_string

		except :
			return None, point_string

	except :
		return None, None


def GradePage( page_canvas, verbose = True, point_flags = defaut_point_flags  ) :
	'''
	grade = GradePage( page_canvas, verbose = True, point_flags = defaut_point_flags )
	'''
	grade = 0

	for string in page_canvas.strings :

		points, point_string = ParsePointString( string, point_flags = point_flags )

		if not points is None :

			grade += points

			if verbose :
				print( string )

	return grade

def GradeDoc(document, verbose = False, point_flags = defaut_point_flags ) :

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

		grade += GradePage( viewer.canvas, verbose = verbose, point_flags = point_flags )

	return grade


if __name__ == '__main__':


	for point_string in ['%4%','%5', 'toto %6%hdsfouze_ç'] :
		print( point_string, ParsePointString( point_string ) )

	document = open('../homework/graded_homework.pdf', "rb")

	print(GradeDoc(document))
