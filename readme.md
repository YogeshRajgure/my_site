This project is the way of learning and implementing Django step by step.



Important commands in Django:
```cmd
django-admin startproject project-name
python manage.py runserver
python manage.py startapp challenges
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python managy.py collectstatic

python manage.py createsuperuser
eg. [root, root@root.com] 
```
**to show the user-uploaded images and to serve the static files using django-**

settings.py 
```python
MEDIA_ROOT = BASE_DIR 
MEDIA_URL = "/user-media/"
MEDIA_ROOT = BASE_DIR 
MEDIA_URL = "/user-media/"
```
urls.py
```
urlpatterns = [ 
    # urls
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

```