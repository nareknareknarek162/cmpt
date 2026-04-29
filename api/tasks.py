from celery import shared_task
from service_objects.services import ServiceOutcome

from api.services.photo.delete import PhotoDeleteService


@shared_task
def delete_photo_task(photo_id, user_id):
    ServiceOutcome(PhotoDeleteService, {"id": photo_id, "user": user_id})
    return None
