import json

from django.db import models
from django.conf import settings
from django.core.serializers import serialize



def upload_update_image(instance, filename):
    return "updates/{users}/{filename}".format(users=instance.user, filename=filename)

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        return serialize('json', qs, fields=('user', 'content', 'image'))

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)
        
class Updates(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()
    
    def __str__(self):
        return self.content or ""

    def serialize(self):
       json_data = serialize("json", [self], fields=('user', 'content', 'image'))
       stuck = json.loads(json_data)
       data = json.dumps(stuck[0]['fields'])
       return data
    
