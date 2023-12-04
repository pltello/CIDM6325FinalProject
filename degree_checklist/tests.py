from django.test import TestCase

from .models import (Student, Degree, Core_Requirements,
                     University_Requirements, Department_Requirements,
                     Major_Requirements)


# simple unittest

class TestSimpleComponent(TestCase):
    def test_basic_sum(self):
        assert 1+1 == 2

# testing models


class TestStudentModel(TestCase):
    def test_student_model(self):
        student = Student.objects.create(WTID='1123900', FirstName='Penelope', LastName='Tello',
                                              DegreeName='M.S. Computer Information Systems and Business Analytics', DegreeYear=20232024, TransferStudent=False, CoursesCompleted='CIDM6351')
        self.assertIsInstance(student, Student)


class TestDegreeModel(TestCase):
    def test_degree_model(self):
        degree = Degree.objects.create(DegreeName='Accounting B.B.A', DegreeYear=20232024, UniversityName='Engler College of Business',
                                       DepartmentName='Accounting, Economics, and Finance', MajorName='Accounting')
        self.assertIsInstance(degree, Degree)


class TestCoreRequirementsModel(TestCase):
    def test_core_reqs_model(self):
        core_reqs = Core_Requirements.objects.create(
            CoreCourseID='ANSC1319', CoreCourseName='Principles of Animal Scienc', YearsRequired=20232024)
        self.assertIsInstance(core_reqs, Core_Requirements)


class TestUniRequirementsModel(TestCase):
    def test_uni_reqs_model(self):
        uni_reqs = University_Requirements.objects.create(
            UniversityName='Engler College of Business', UniCourseID='BUSI1301', UniCourseName='Business Principles', YearsRequired=20232024)
        self.assertIsInstance(uni_reqs, University_Requirements)


class TestDeptRequirementsModel(TestCase):
    def test_dept_reqs_model(self):
        dept_reqs = Department_Requirements.objects.create(DepartmentID='BBA', DepartmentName='Bachelor of Business Administration',
                                                           DepCourseID='ACCT2301', DepCourseName='Principles of Financial Accounting', YearsRequired=20232024)
        self.assertIsInstance(dept_reqs, Department_Requirements)


class TestMajRequirementsModel(TestCase):
    def test_maj_reqs_model(self):
        maj_reqs = Major_Requirements.objects.create(
            MajorName='Accounting', MajCourseID='ACCT3311', MajCourseName='Federal Tax Accounting I', YearsRequired=20232024)
        self.assertIsInstance(maj_reqs, Major_Requirements)
