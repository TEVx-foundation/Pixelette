from django.db import models
import uuid

class History(models.Model):
	dateCreated = models.DateTimeField(auto_now_add = True)
	dateModified = models.DateTimeField(auto_now = True)
	primaryKey = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

	pixel = models.ImageField(upload_to='general/files/', blank = True, null = True)
	data = models.CharField(max_length = 1000, default="HistoryDataServiceProvider")
	link = models.CharField(max_length = 150, default="HistoryLinkServiceProvider")