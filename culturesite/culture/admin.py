from django.contrib import admin

from .models import Artifact, ArtifactOwner


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    pass


@admin.register(ArtifactOwner)
class ArtifactOwnerAdmin(admin.ModelAdmin):
    pass
