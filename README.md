# django-polls-app-demo
It's for django beginners.

- Download and install python (Global)
- Download and install pip (Global)
  [python get-pip.py]
- install Django (Global)
   [pip install Django]
- install vertualenv 
   [pip install virtualenvwrapper]
- create a new isolated virtualenv
   virtualenv <Name>
- To activate the virtualenv
   run scripts/activate


========================================
-To check whether Django has been installed ?
  [python -m django --version]
- To  create a new project with settings
  [django-admin startproject mysite]
- run the server: python manage.py runserver

===================================================

Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. We�ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:

Change your models (in models.py).
- Run python manage.py makemigrations to create - migrations for those changes
- Run python manage.py migrate to apply those changes to the database.
===================================
python manage.py shell
===================================

===================================
python manage.py test polls
===================================
