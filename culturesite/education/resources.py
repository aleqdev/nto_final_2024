from import_export import resources, fields
from .models import Study, TeacherEducation


class StudiesResource(resources.ModelResource):
    name = fields.Field(
        column_name='Наименование',
        attribute='name')
    descrition = fields.Field(
        column_name="Описание",
        attribute="descrition"
    )
    class Meta:
        model = Study


class TeacherEducationResource(resources.ModelResource):
    class Meta:
        model = TeacherEducation
