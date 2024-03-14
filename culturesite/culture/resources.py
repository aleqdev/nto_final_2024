from import_export import resources, fields
from .models import Artifact, Study, ForeignOrganization
from import_export.widgets import ForeignKeyWidget

class ArtifactResource(resources.ModelResource):
    name = fields.Field(
        column_name="name",
        attribute="name"
    )
    owner = fields.Field(
        column_name='owner',
        attribute='owner',
        widget=ForeignKeyWidget(model=Study, field='name')
    )
    class Meta:
        model = Artifact


class ForeignOrganizationResource(resources.ModelResource):
        model = ForeignOrganization
