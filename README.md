# Jinja -HTML
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

# Extensions In VS Code
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

# Postgre Setup
https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8

# Proxy
- proxy= requests.get('https://api.ipify.org/?format=json').json()
- requests.get(proxies=proxy)
