from django.urls import path
from . import views

urlpatterns = [
	path('', views.blog_Page),
	# <int:blog_id>/ 网站的后面是数字 ex: xxx/blog/1
	path('<int:blog_id>/', views.blog_text),
]