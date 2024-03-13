from import_export import resources
from .models import Studies, TeacherEducation

class StudiesResource(resources.ModelResource):
    class Meta:
        model = Studies

class TeacherEducationResource(resources.ModelResource):
    class Meta:
        model = TeacherEducation