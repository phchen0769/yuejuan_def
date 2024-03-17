# yuejuan_drf
# logs 目录为日志文件以及uwsgi和nginx运行时产生的临时文件。
# supervisor.conf 为supervisord工作时的配置文件
# uwsgi.ini 为uwsgi的配置文件 
# repositories 为alpine国内源文件
# requirements.txt为项目需要安装的依赖包


# 注意：容器完成后，需要把.devcontainer/cache.py替换/usr/lib/python3.10/site-packages/django/views/decorators/cache.py文件,用以支持xadmin
# 测试适用环境python3.10，django4.1

# 运行数据库
#### ARM
# docker run -d --name Mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -v /Volumes/Extreme\ SSD/github/db:/var/lib/mysql mariadb:latest

# Intel
# docker run -d --name Mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -v /Volumes/myOS/Users/fedorov/Documents/GitHub/db:/var/lib/mysql mariadb:latest

# 运行项目
# python manage.py runserver 