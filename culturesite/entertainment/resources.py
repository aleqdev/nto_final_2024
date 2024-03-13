from import_export import resources
from .models import Place


class PlaceResource(resources.ModelResource):
    class Meta:
        model = Place
