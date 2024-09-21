# 启动项目
```shell
python manage.py runserver  8002
daphne -b 127.0.0.1 -p 8002 websocket_rollibit.asgi:application

```

# 同步数据库
```shell
python manage.py makemigrations
python manage.py migrate
```

# 安装依赖
```shell
pip install -r requirements.txt
```

# 构造requirements.txt
```shell
pip freeze > requirements.txt
```

# 报错处理
```shell
set DJANGO_SETTINGS_MODULE=websocket_rollibit.settings
```

