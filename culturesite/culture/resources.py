from import_export import resources
from .models import Artifact


class ArtifactResource(resources.ModelResource):
    class Meta:
        model = Artifact
