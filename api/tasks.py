from celery import shared_task

from models_app.models import Photo


@shared_task
def delete_photo_task(photo_id):
    Photo.objects.get(id=photo_id).delete()
    return None
