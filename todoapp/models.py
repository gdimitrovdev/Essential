from django.db import models
from django.contrib.auth import get_user_model

class Todo(models.Model):
	user=models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		related_name='todos',
		null=True
	)
	text=models.CharField(max_length=40)
	complete=models.BooleanField(default=False)
	def __str__(self):
		return self.text
