from django.db import models

# Create your models here.
class Blog(models.Model):

	title = models.CharField(default='文章标题', max_length=50)
	date = models.DateField()
	image = models.ImageField(default='default.png', upload_to='images/')
	# image = models.ImageField(default='default.png', upload_to='images/')
	text = models.TextField(default='文章正文')

	def __str__(self):
		return self.title

	# 处理文字过长，简单来说就是简介的一种，
	def short_text(self):
		return self.text[:60] + '...'
    