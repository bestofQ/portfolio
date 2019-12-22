from django.db import models

# Create your models here
# 创建一些模板.


class Gallery(models.Model):
	# CharField 一般不建议写太多字
	# description = models.CharField(max_length=100)
	description = models.CharField(default='这里写关于作品的简介' ,max_length=100)
	title = models.CharField(default='作品标题' ,max_length=50)
	# 图片更新到哪里 保存到media的目录下
	image = models.ImageField(default='default.png', upload_to='images/')
	# image = models.ImageField(default='default.png', upload_to='D:/GB/portfolio/images/')

	# 改变标题
	def __str__(self):
		return self.title
