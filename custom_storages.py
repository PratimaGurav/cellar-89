"""
Defines the storage location for static and
media files for production
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
# pylint: disable=W0223


class StaticStorage(S3Boto3Storage):
    """
    Sets the storage location for static files on AWS
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Sets the storage location for media files on AWS
    """
    location = settings.MEDIAFILES_LOCATION
