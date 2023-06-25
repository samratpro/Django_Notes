# Jinja -HTML
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
# Extensions In VS Code
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
# Postgre Setup
```

https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
```
# Proxy
```
- proxy= requests.get('https://api.ipify.org/?format=json').json()
- requests.get(proxies=proxy)
```
# Pythonanywhere
```
https://www.pythonanywhere.com/
https://studygyaan.com/django/host-django-website-application-for-free-in-5-minutes
https://www.pythonanywhere.com/forums/topic/27314/
https://www.youtube.com/watch?v=A6mTN6G-adM

step 1:
# Go Consoles and open console bash
git clone git_repo_link

Step 2:
# navigate folder where have manage.py file

Step 3:
# Create a Virtual Environment, we can change the Python version
mkvirtualenv --python=/usr/bin/python3.7  mysite-virtualenv

Step 4:
workon  mysite-virtualenv
# do this command to ensure the virtual environment has been activated

Step 5:
pip install -r requirements.txt
or install modules

Step 6:
# Go web and Create a Django, web with Manual configuration, also make sure same version python

Step 7:
# Scroll down and go Source code section

Step 8:
"""
Go file section by opening another tab of the browser
Navigate the " project folder " path until manage.py file section
example:
/home/aiwritertools/AiWriterTools/aiwriter (in this directory has manage.py)

copy this path and paste in the Source code: section according to step 7:
"""

Step 9:
# Open WSGI configuration file:
# Paste this code
# Configure path = '/home/aiwritertools/AiWriterTools/aiwriter' and aiwriter.settings
import os
import sys
path = '/home/aiwritertools/AiWriterTools/aiwriter'
if path not in sys.path:
     sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'aiwriter.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

Step 10:
# input Virtualenv: path
"""
Go file section by opening another tab of the browser
Navigate the " .virtualenvs " folder path until bin/ lib/ folder section
example:
/home/aiwritertools/.virtualenvs/mysite-virtualenv (in this directory has bin/ lib/ folder)

copy this path and paste in the Virtualenv: section according to step 7:

Example: 
Virtualenv:
/home/aiwritertools/.virtualenvs/mysite-virtualenv

"""

Step 11 :
Static files:
URL	Directory:
| URL        |   Directory                                           |
| /static/	 |  /home/aiwritertools/AiWriterTools/aiwriter/static	   |
| /media/	   |   /home/aiwritertools/AiWriterTools/aiwriter/media	   |

Step 12:
# go bash console and:
python manage.py makemigrations
python manage.py migrate

Step 13:
Reload: project.pythonanywhere.com

```

