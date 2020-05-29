from pdfreader import PDFDocument
from pdfrw import PdfReader

file_path = '../homework/graded_homework.pdf'

document = open( file_path, "rb")

doc = PDFDocument(document)

print(document.name)
print(doc.__dict__)

reader = PdfReader(file_path)

print(reader.Info)
