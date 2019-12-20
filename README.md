1、创建一个新的app的时候你需要迁移你的app到数据库
语法：python manage.py makemigrations
2、执行你的迁移
语法：python manage.py migrate
3、进入admin的界面，但是你会发现需要你输入用户名和密码这个时候你就需要添加用户名和密码
语法：python manage.py createsuperuser
usrname:q
password:tjq123456
4、model中的信息传递到html
