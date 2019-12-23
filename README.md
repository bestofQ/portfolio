1、创建一个新的app的时候你需要迁移你的app到数据库
语法：python manage.py makemigrations
2、执行你的迁移
语法：python manage.py migrate
3、进入admin的界面，但是你会发现需要你输入用户名和密码这个时候你就需要添加用户名和密码
语法：python manage.py createsuperuser
usrname:q
password:tjq123456
4、model中的信息传递到html

2019/12/22
1、models中的文件改变需要及时更新到数据库中，不然会出错
2、imagefield中的upload_to 需要的是绝对路径，相对的会出错
3、需要添加一个媒体的url和媒体的根目录media 在setting中
# 媒体url
MEDIA_URL = '/media/'
# 文件路径
# MEDIA_ROOT = 'media'
# 路径合成 媒体的根目录 下面可有有很多子目录 images,music等等
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
4、需要显示所上传的图片需要在主url中添加：
from django.conf.urls.static import static
from django.conf import settings
&&&&&&&&&&&&
urlpatterns = [
    path('xx/',xx.xx),
    path('xx/',xx.xx),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	# static(url, path)

2019/12/23
1、创建一个新的blog app
python manage.py startapp blog
2、在主settings中配置你的app 'blog'
3、在models.py中创建你的模板
4、在admin.py中注册你的model
5、然后进行数据转移