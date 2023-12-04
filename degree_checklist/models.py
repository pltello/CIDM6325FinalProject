from django.db import models


class Student(models.Model):
    WTID = models.IntegerField(help_text="WT ID")
    FirstName = models.CharField(max_length=30, help_text="First Name")
    LastName = models.CharField(max_length=30, help_text="Last Name")
    DegreeName = models.CharField(max_length=75, help_text="Degree Name")
    DegreeYear = models.IntegerField(help_text="Degree Year")
    TransferStudent = models.BooleanField(
        default=False, help_text="Transfer Student")
    CoursesCompleted = models.CharField(
        max_length=250, help_text="List of Courses Completed")

    def __str__(self):
        return self.WTID


class Degree(models.Model):
    DegreeName = models.CharField(max_length=75, help_text="Degree Name")
    DegreeYear = models.IntegerField(help_text="Degree Year")
    UniversityName = models.CharField(
        max_length=75, help_text="University Name")
    DepartmentName = models.CharField(
        max_length=75, help_text="Department Name")
    MajorName = models.CharField(max_length=75, help_text="Major Name")

    def __str__(self):
        return self.DegreeName


class Core_Requirements(models.Model):
    CoreCourseID = models.CharField(max_length=10, help_text="Course ID")
    CoreCourseName = models.CharField(max_length=75, help_text="Course Name")
    YearsRequired = models.IntegerField(help_text="List of Years Required")

    def __str__(self):
        return f"{self.CoreCourseID} {self.CoreCourseName}"


class University_Requirements(models.Model):
    UniversityName = models.CharField(
        max_length=75, help_text="University Name")
    UniCourseID = models.CharField(max_length=10, help_text="Course ID")
    UniCourseName = models.CharField(
        max_length=75, help_text="Course Name", null=True)
    YearsRequired = models.IntegerField(help_text="List of Years Required")

    def __str__(self):
        return f"{self.UniCourseID} {self.UniCourseName}"


class Department_Requirements(models.Model):
    DepartmentID = models.CharField(max_length=10, help_text="Department ID")
    DepartmentName = models.CharField(
        max_length=50, help_text="Department Name")
    DepCourseID = models.CharField(max_length=10, help_text="Course ID")
    DepCourseName = models.CharField(
        max_length=75, help_text="Course Name", null=True)
    YearsRequired = models.IntegerField(help_text="List of Years Required")

    def __str__(self):
        return f"{self.DepCourseID} {self.DepCourseName}"


class Major_Requirements(models.Model):
    MajorName = models.CharField(max_length=50, help_text="Major Name")
    MajCourseID = models.CharField(max_length=10, help_text="Course ID")
    MajCourseName = models.CharField(
        max_length=75, help_text="Course Name", null=True)
    YearsRequired = models.IntegerField(help_text="List of Years Required")

    def __str__(self):
        return f"{self.MajCourseID} {self.MajCourseName}"


class UploadFormModel(models.Model):
    file_field = models.FileField(upload_to="files/")
