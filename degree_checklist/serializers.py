from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    WTID = serializers.IntegerField()
    FirstName = serializers.CharField()
    LastName = serializers.CharField()
    DegreeName = serializers.CharField()
    DegreeYear = serializers.IntegerField()
    TransferStudent = serializers.BooleanField()
    CoursesCompleted = serializers.CharField()


class DegreeSerializer(serializers.Serializer):
    DegreeName = serializers.CharField()
    DegreeYear = serializers.IntegerField()
    UniversityName = serializers.CharField()
    DepartmentName = serializers.CharField()
    MajorName = serializers.CharField()


class Core_RequirementsSerializer(serializers.Serializer):
    CoreCourseID = serializers.CharField()
    CoreCourseName = serializers.CharField()
    YearsRequired = serializers.IntegerField()


class University_RequirementsSerializer(serializers.Serializer):
    UniversityName = serializers.CharField()
    UniCourseID = serializers.CharField()
    UniCourseName = serializers.CharField()
    YearsRequired = serializers.IntegerField()


class Department_RequirementsSerializer(serializers.Serializer):
    DepartmentID = serializers.CharField()
    DepartmentName = serializers.CharField()
    DepCourseID = serializers.CharField()
    DepCourseName = serializers.CharField()
    YearsRequired = serializers.IntegerField()


class Major_RequirementsSerializer(serializers.Serializer):
    MajorName = serializers.CharField()
    MajCourseID = serializers.CharField()
    MajCourseName = serializers.CharField()
    YearsRequired = serializers.IntegerField()
