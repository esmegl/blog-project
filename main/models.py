from django.db import models

class Category(models.Model):
	category = models.CharField(max_length=250)

	def __str__(self) -> str:
		return self.category

class Blog(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=250)
	description = models.TextField(max_length=2000)
	imageURL = models.URLField(null=True, blank=True, max_length=2000)
	# comments = models.CharField(max_length=2000)
	# stars = models.IntegerField()

	def __str__(self) -> str:
		return self.title