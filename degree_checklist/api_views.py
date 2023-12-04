from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (Student, Degree, Core_Requirements,
                     University_Requirements, Department_Requirements,
                     Major_Requirements)
from .serializers import (StudentSerializer, DegreeSerializer, Core_RequirementsSerializer,
                          University_RequirementsSerializer, Department_RequirementsSerializer,
                          Major_RequirementsSerializer)


@api_view()
def all_students(request):
    students = Student.objects.all()
    student_serializer = StudentSerializer(students, many=True)
    return Response(student_serializer.data)


@api_view()
def all_degrees(request):
    degrees = Degree.objects.all()
    degree_serializer = DegreeSerializer(degrees, many=True)
    return Response(degree_serializer.data)


@api_view()
def all_core_reqs(request):
    core_reqs = Core_Requirements.objects.all()
    core_reqs_serializer = Core_RequirementsSerializer(core_reqs, many=True)
    return Response(core_reqs_serializer.data)


@api_view()
def all_uni_reqs(request):
    uni_reqs = University_Requirements.objects.all()
    uni_reqs_serializer = University_RequirementsSerializer(
        uni_reqs, many=True)
    return Response(uni_reqs_serializer.data)


@api_view()
def all_dep_reqs(request):
    dep_reqs = Department_Requirements.objects.all()
    dep_reqs_serializer = Department_RequirementsSerializer(
        dep_reqs, many=True)
    return Response(dep_reqs_serializer.data)


@api_view()
def all_major_reqs(request):
    maj_reqs = Major_Requirements.objects.all()
    maj_reqs_serializer = Major_RequirementsSerializer(
        maj_reqs, many=True)
    return Response(maj_reqs_serializer.data)
