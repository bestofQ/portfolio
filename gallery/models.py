from django.db import models

# Create your models here
# 创建一些模板.


class Gallery(models.Model):
	# CharField 一般不建议写太多字
	description = models.CharField(max_length=100)
