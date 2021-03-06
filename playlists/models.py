from django.db import models
import uuid
# Create your models here.
from libraries.models import Library
class playlist(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,null=False,editable=False)
	name = models.CharField(blank=False,null=False,max_length=200)
	description = models.TextField(null=True,blank=True)
	date_created = models.DateTimeField(auto_now=True,null=False,editable=False)
	library = models.ForeignKey(Library,related_name="playlist",on_delete=models.CASCADE)
	def __str__(self)->str:
		return self.name