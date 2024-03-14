from import_export import resources, fields
from .models import Place
from import_export.widgets import ForeignKeyWidget



class PlaceResource(resources.ModelResource):
    class Meta:
        model = Place
