from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Library(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	name = models.CharField(blank=False,null=False,max_length=200,db_index=True)
	description = models.TextField(blank=False,null=False)
	date_created = models.DateTimeField(auto_now=True,null=False,editable=False)
	auther = models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self) -> str:
		return self.name
