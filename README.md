# Table of Content:
```
1 Jinja -HTML  
2 Extensions In VS Code  
3 Postgre Setup  
4 Proxy  
5 Pythonanywhere Setup docs link  
6 Pythonanywhere Setup Guide  
7 Django Cpanel Setup Guide
8 Django Setup in VPS
```

## Jinja -HTML
```
- Required Plugin : Django
- 
{
  "python.jediEnabled": false,
  "files.autoSave": "afterDelay",
  "editor.suggestSelection": "first",
  "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
  "editor.minimap.enabled": true,
  "editor.largeFileOptimizations": false,
  "html.format.indentInnerHtml": true,
  "html.format.indentHandlebars": true,
  "emmet.includeLanguages": {
    "django-html": "html"
  },
  "[django-html]": {

  },
  "files.associations": {
    "*.html": "html"
  }
}
```
## Extensions In VS Code
```
1. Bootstrap 5 Quick Snippets (https://marketplace.visualstudio.com/items?itemName=AnbuselvanRocky.bootstrap5-vscode)
2. Django (https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
3. Django Snippets (https://marketplace.visualstudio.com/items?itemName=bibhasdn.django-snippets)
4. isort (https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
5. JavaScript (ES6) code snippets (https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets)
6. Live Server (https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
7. Pylance (https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
8. Python
9. Python Indent (https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
10. SQLite Viewer
11. vscode-icons (https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)
```
## Postgre Setup
```

https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
```
## Proxy
```
- proxy= requests.get('https://api.ipify.org/?format=json').json()
- requests.get(proxies=proxy)
```
## Pythonanywhere Setup docs link
```
https://www.pythonanywhere.com/
https://studygyaan.com/django/host-django-website-application-for-free-in-5-minutes
https://www.pythonanywhere.com/forums/topic/27314/
https://www.youtube.com/watch?v=A6mTN6G-adM
```
## Pythonanywhere Setup Guide

### Step 1: Consoles
```
# Go Consoles and open console bash
git clone git_repo_link
```
### Step 2:
```
# navigate folder in console bash where have " manage.py " file with " cd " command and checking with " ls "
```
### Step 3: Consoles
```
# Create a Virtual Environment in console bash where has " manage.py " file, we can change the Python version
mkvirtualenv --python=/usr/bin/python3.7  mysite-virtualenv
```
### Step 4: Consoles
```
workon  mysite-virtualenv
# do this command to ensure the virtual environment has been activated in console bash 
```
### Step 5: Consoles
```
pip install -r requirements.txt
or install modules
```
### Step 6: Web
```
# from another " browser tab " Go web from the menu and Create a Django, web with Manual configuration, also make sure same version python
```
### Step 7: Web
```
# Scroll down and go Source code section after creating Django
```
### Step 8: Files then Web
```
# Go file section by opening another " tab of the browser "
# Navigate the " project folder " path until manage.py file section
example:
/home/aiwritertools/AiWriterTools/aiwriter (in this directory has manage.py)

# copy this path and paste it into the Source code: section according to step 7, where created Django section from " Menu > Web ":
```

### Step 9: Web
```
# Open WSGI configuration file:
# Paste this code
# Configure these ,  path = '/home/aiwritertools/AiWriterTools/aiwriter' and aiwriter.settings

import os
import sys
path = '/home/aiwritertools/AiWriterTools/aiwriter'
if path not in sys.path:
     sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'aiwriter.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
### Step 10: Files then Web
```
# input Virtualenv: path
# Go file section by opening another tab of the browser
# Navigate the " .virtualenvs " folder path until bin/ lib/ folder section
example:
/home/aiwritertools/.virtualenvs/mysite-virtualenv (in this directory has bin/ lib/ folder)

# copy this path and paste in the Virtualenv: section according to step 7:

Example: 
Virtualenv:
/home/aiwritertools/.virtualenvs/mysite-virtualenv
```
### Step 11 : Files then Web
```
Static files:
----------------------------------------------------------------------
| URL        |   Directory                                           |
----------------------------------------------------------------------
| /static/	 |  /home/aiwritertools/AiWriterTools/aiwriter/static	   |
| /media/	   |   /home/aiwritertools/AiWriterTools/aiwriter/media	   |
```
### Step 12: Console
```
# go bash console and:
python manage.py makemigrations
python manage.py migrate
```
### Step 13: Web
```
Reload: project.pythonanywhere.com

```
#  Django Cpanel Setup Guide
### Step 1: Manage Shell
```
from " Manage SSH " enable Enable " SSH access " to Activate the " Terminal "
" Terminal " will have in Advanced section
```
### Step 2: Setup Python App
```
>>> Go " Setup Python App " section >
>>> Create Application >
>>> Python Version (3.7 is suitable) >
>>> Application root ( That folder will have " Django Files " unknown name can be to create new one) >
>>> Application URL ( Select the domain/subdomain name ) >
>>> Application startup file ( Keep blank ) >
>>> Application Entry point ( Keep blank ) >
```
### Step 3: Terminal & Virtual Environment
```
>>> Copy the " Virtual Environment " path from the Django App section after creating (according to step 2)
    example path: source /home/toolwqve/virtualenv/aiapp/3.7/bin/activate && cd /home/toolwqve/aiapp
>>> Paste the path in the terminal to activate " Virtual Environment "
    example: ((aiapp:3.7))    ----- here aiapp is folder name and 3.7 is the python version
```
### Step 4: Install Django and Setup Django
```
>>> pip install django
>>> django-admin startproject projectname .
>>> django-admin startapp appname
```
### Step 5: Make Sure the path and setup passenger_wsgi.py

>>> Delete everthing from this file and paste:
```
from aiwriter.wsgi import application
```
( here aiwriter is project name, wsgi is file name, application is variable name from wsgi file 
>>> This file will works alternative, python manage.py runserver
>>> Also make sure setting.py:
``` ALLOWED_HOSTS = ["*"] ```# approx 28 line
>>> Now "Restart App (according to step 2) " reload and browse domain to see Django welcome page

### Step 6: Upload Project Files
```
Upload all local project files:
>>> Project Folder
    setting.py
    urls.py
>>> app folder
```
### Step 7: Database Migration
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
>>> Then "Restart App (according to step 2) " reload and browse the domain to see Django Project
```


#  Django Setup Guide VPS (aaPanel)
(aapanel alternatives : https://www.cloudpanel.io/blog/vps-management/)
### Step 1: Install OS
```
Install OS:
Restart os : Debian / Ubuntu
Select new password

open Cmd : get ip root access:
>>> ssh root@ip_address -p 22   (Enter)
>>> type and enter password

Update System
>>> sudo apt-get update -y && sudo apt-get upgrade -y (Enter)
>>> sudo apt-get autoremove
>>> reboot

```
### Step 2: Install aaPanel
```
Install aaPanel For ubuntu and Befina
>>> wget -O install.sh http://www.aapanel.com/script/install-ubuntu_6.0_en.sh && sudo bash install.sh aapanel (Enter)
(https://www.aapanel.com/new/download.html#install)

Login ip will come :
aaPanel Internet Address: http://62.8.86.183:8888/fcaeefb5
aaPanel Internal Address: http://10.0.2.15:8888/fcaeefb5
username: dmog1pfi
password: 7c9ef0e0

>>> bt (for aapanel options in CLI)
>>>
A reference : https://techviewleo.com/install-and-use-aapanel-on-debian-linux/?expand_article=1
( all commands is here, all option has in CLI)

```



### Step 3: Qucick Install EngineX / nginx Server
```
Here, a popup will come to install server database, etc

```
### Step 4: Install Pythom 
Reference : https://forum.aapanel.com/d/13338-python-manager-deploy-djangoblog
```
First install the git tool to clone the DjangoBlog project:
(RedHat|CentOS：)
yum install git -y

(Debian|Ubuntu：)
apt-get update
apt-get install git -y

Clone the DjangoBlog project:
cd /www/wwwroot/
git clone https://github.com/liangliangyy/DjangoBlog
```
1. Check file Permission
   ```
   cd /www/wwwroot/
   ls -ld
   or
   ls -ld 'dirname'
   ```
   example:
   ```
   output : drwxrwxr-x 15 www-data www-data 4096
   1st d - indicates directory
   2nd rwx (owner) means the owner (www-data) has read, write, and execute permissions.
   3rd rwx (group) means the group (www-data) has read, write, and execute permissions.
   4th r-x (others) means others have read and execute permissions, but not write permissions.
   15: The number of hard links to the directory.
   www-data www-data: The owner and group of the directory, respectively.
   4096: The size of the directory in bytes.
   ```
   Fix Permission:
   ```
   sudo chmod -R u+w /www/wwwroot/targeted_dir_name
   Delete : - /www/wwwroot/IP_ADDRESS/.user.ini
   Restart nginx Server:
   sudo systemctl restart nginx
   sudo service nginx restart

   It can do also from aapanel
   ```

2.Install Python 3.8.12 or other


3.Add DjangoBlog project
Parameter Description:
```
Name：-------- Give your project a name
Path：-------- Select the root directory of the project,Select the previously cloned directory
Version：------ Choose the python version your project needs,Choose Python Version 3.8.12 here
Framework：--------- The project project framework, my project here is Flask, so choose django
Startup mode：-------Choose gunicorn here, You can switch other options according to your needs
startuo file/dir：-----diango select the project directory to start
Port：-------DjangoBlog defaults to `8000`
Run user：-----Start with `root` privileges
commands ----------- ' Blank '
Install module now：-----When adding a project, install the required modules according to the documentation of the project root directory requirements.txt.
Start with the sys：Configure startup for the project
```

### Step 5: DataBase, Domain & CSRF Fix
create a postgre database
then
```
We never use vritual evn here, we have to use main enviroment, that will create system when install django app
cc594d1425a1eecd52879965ff4c600f_venv/bin/pip install psycopg2

setting.py

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME':  'aiproject',
       'USER': 'aiproject',
       'PASSWORD': 'D3PKHjmPeYjMES4Z',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}

also change:
ALLOWED_HOSTS = ['*','app.domain.com']
CSRF_TRUSTED_ORIGINS = [
    'https://app.domain.com'
]

```

### Start Database operation
// Where have manage.py
```
8658305af42d6efded53c296d677d3ba_venv/bin/python3 manage.py makemigrations                ### 8658305af42d6efded53c296d677d3ba_venv is envirromnent here
8658305af42d6efded53c296d677d3ba_venv/bin/python3 manage.py migrate

8658305af42d6efded53c296d677d3ba_venv/bin/python3 manage.py createsuperuser
8b2c22c93ab3f63b80ec5360ff498393_venv/bin/python3 manage.py migrate

8658305af42d6efded53c296d677d3ba_venv/bin/python3 manage.py collectstatic --noinput
8b2c22c93ab3f63b80ec5360ff498393_venv/bin/python3 manage.py migrate

```
## Ensure 8000 port from security section
```
if missing add there
```

### Restart App check 
http://ap_address:8000/ and you can see the 

### Mapping with Domain URL
```
1. First change Domain/Subdomain DNS IP With VPS IP
2. Then from Application > Map > add domain
3. In Security section add : 8000 port with TCP/UDP protocol  (it is for IP)
4. And redirect IP with main domain

```


