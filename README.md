# pyGrade

Count points in annotated PDF documents to help with assignment grading.

## Usage

Use  [Xournal](http://xournal.sourceforge.net/) or any other PDF editor to grade the document, and save it as a PDF document. Points should appear as `%2%` or `%-1.5%` in the annotated [document](./homework/graded_homework.pdf).

```python
import pyGrade as grd
document = open('../homework/graded_homework.pdf', "rb")
print( grd.GradeDoc(document) )
```
```console
>>> 6.0
```
