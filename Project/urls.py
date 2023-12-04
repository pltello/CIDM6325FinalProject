"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from degree_checklist import views, api_views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from degree_checklist.views import (StudentRecordFormView, DegreeRecordFormView, CoreRecordFormView,
                                    UniRecordFormView, DepRecordFormView, MajRecordFormView, FormSuccessView, UploadFormView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('degree_checklist/student_list',
         views.student_list, name='student_list'),
    path('degree_checklist/degree_list',
         views.degree_list, name='degree_list'),
    path('degree_checklist/core_requirement_list',
         views.core_requirement_list, name='core_requirement_list'),
    path('degree_checklist/university_requirement_list',
         views.university_requirement_list, name='university_requirement_list'),
    path('degree_checklist/department_requirements_list',
         views.department_requirements_list, name='department_requirements_list'),
    path('degree_checklist/major_requirements_list',
         views.major_requirements_list, name='major_requirements_list'),
    path('new_student_record', StudentRecordFormView.as_view(),
         name='student_record_form'),
    path('new_degree_record', DegreeRecordFormView.as_view(),
         name='degree_record_form'),
    path('new_core_req_record', CoreRecordFormView.as_view(),
         name='core_req_record_form'),
    path('new_university_record', UniRecordFormView.as_view(),
         name='university_record_form'),
    path('new_department_record', DepRecordFormView.as_view(),
         name='department_record_form'),
    path('new_major_record', MajRecordFormView.as_view(), name='major_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('file_form', views.FileFormView, name='file_form'),
    path('upload_form', UploadFormView.as_view(), name='upload_form'),
    path('api/all_students/', api_views.all_students, name='all_students'),
    path('api/all_degrees/', api_views.all_degrees, name='all_degrees'),
    path('api/all_core_reqs/', api_views.all_core_reqs, name='all_core_reqs'),
    path('api/all_uni_reqs/', api_views.all_uni_reqs, name='all_uni_reqs'),
    path('api/all_dep_reqs/', api_views.all_dep_reqs, name='all_dep_reqs'),
    path('api/all_major_reqs/', api_views.all_major_reqs, name='all_major_reqs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
