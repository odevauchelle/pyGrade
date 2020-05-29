from pdfreader import PDFDocument, SimplePDFViewer

##################
#
# BASIC FUNCTIONS
#
##################

def parse_point_string( point_string, point_flags = ('%','%') ):

	try :
		point_string = point_string.split(point_flags[0])[1].split(point_flags[1])[0]

		try :
			points = float( point_string )
			return points, point_string

		except :
			return None, point_string

	except :
		return None, None


def grade_page( page_canvas, verbose = True, point_flags = ('%','%')  ) :

	grade = 0

	for string in page_canvas.strings :

		points, point_string = parse_point_string( string, point_flags = point_flags )

		if not points is None :

			grade += points

			if verbose :
				print( string )

	return grade

def grade_document(document, verbose = False, point_flags = ('%','%') ) :

	doc = PDFDocument( document )
	viewer = SimplePDFViewer( document )

	grade = 0

	for page_number, page in enumerate( doc.pages() ) :

		if verbose :
			print('------------------')
			print('Page:', page_number)

		viewer.navigate( page_number + 1 )
		viewer.render()

		grade += grade_page( viewer.canvas, verbose = verbose, point_flags = point_flags )

	return grade

##################
#
# OPEN FILE
#
##################

document = open('../homework/graded_homework.pdf', "rb")

print(grade_document(document))
