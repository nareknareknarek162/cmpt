from celery import shared_task

from models_app.models import Photo
from models_app.models.photo.fsm import State


@shared_task
def delete_photo_task(photo_id):
    photo = Photo.objects.get(id=photo_id)
    if photo.state == State.ON_DELETE:
        photo.delete()
