from django import forms
from .models import (Student, Degree, Core_Requirements,
                     University_Requirements, Department_Requirements,
                     Major_Requirements, UploadFormModel)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['WTID', 'FirstName', 'LastName', 'DegreeName',
                  'DegreeYear', 'TransferStudent', 'CoursesCompleted']


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ['DegreeName', 'DegreeYear',
                  'UniversityName', 'DepartmentName', 'MajorName']


class CoreForm(forms.ModelForm):
    class Meta:
        model = Core_Requirements
        fields = ['CoreCourseID', 'CoreCourseName', 'YearsRequired']


class UniForm(forms.ModelForm):
    class Meta:
        model = University_Requirements
        fields = ['UniversityName', 'UniCourseID',
                  'UniCourseName', 'YearsRequired']


class DepForm(forms.ModelForm):
    class Meta:
        model = Department_Requirements
        fields = ['DepartmentID', 'DepartmentName', 'DepCourseID',
                  'DepCourseName', 'YearsRequired']


class MajForm(forms.ModelForm):
    class Meta:
        model = Major_Requirements
        fields = ['MajorName', 'MajCourseID',
                  'MajCourseName', 'YearsRequired']


class UploadForm(forms.Form):
    file_upload = forms.FileField()


class UploadForm2(forms.ModelForm):
    class Meta:
        model = UploadFormModel
        fields = "__all__"
