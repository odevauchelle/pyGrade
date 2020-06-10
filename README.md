# pyGrade

Count points in annotated PDF documents to help with assignment grading.

## Usage

Use [Xournal](http://xournal.sourceforge.net/) or any other PDF editor ([Xournal++](https://github.com/xournalpp/xournalpp) for Mac OSX & Windows)
 to grade the document, and save it as a PDF document. Points should appear as `%2%` or `%-1.5%` in the annotated [document](./homework/graded_homework_khalo_rivera.pdf).

```python
import pyGrade as grd

document = open('../homework/graded_homework_khalo_rivera.pdf', "rb")
print( grd.GradeDoc(document) )
```
```console
>>> 6.0
```

## Identify students

Let us first load a [list of the students](../students/students.json) that attend the class:
```python
import json

with open('../students/students.json') as the_file :
    students = json.load(the_file)
```

Hopefully, the authors of the homework mention their names in the first page of the document. We may then identify them:

```python
for i in grd.IdentifyStudent( students, document, expected_number_of_students = 2 ) :
    print( students[i]['lastname'] )
```
```console
>>> Kahlo
>>> Rivera
```
## Requirements

- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
- [pdfreader](https://pypi.org/project/pdfreader/)
- [pyPDF2](https://pypi.org/project/PyPDF2/)

```console
# pip install fuzzywuzzy pdfreader pyPDF2
```
