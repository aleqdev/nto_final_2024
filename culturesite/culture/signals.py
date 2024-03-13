from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from education.models import Study
from .models import ArtifactOwner


@receiver(post_save, sender=Study)
def study_created(sender, instance, created, **kwargs):
    if not created:
        return
    
    ArtifactOwner.objects.create(is_study=True, study_id=instance.id)


@receiver(pre_delete, sender=Study)
def study_deleted(sender, instance, using, **kwargs):
    ArtifactOwner.objects.filter(study__id=instance.id).delete()
