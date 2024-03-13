from import_export import resources
from .models import Study, TeacherEducation


class StudiesResource(resources.ModelResource):
    class Meta:
        model = Study


class TeacherEducationResource(resources.ModelResource):
    class Meta:
        model = TeacherEducation
