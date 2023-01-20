# Django Project Template

The clean, fast and right way to start a new Django `1.10.1` powered website.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv venv
$ source venv/bin/activate
```
To close virtual environment type `deactivate` just by hitting <kbd>Enter<kbd>
```bash
$ pip install -r https://github.com/prabhu1122/Login_Auth_Django/blob/main/requirements.txt
```
You may want to change the name `projectname`.

```bash
$ django-admin startproject `_project_name`

$ cd _project_name/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `_project_name/settings.py` for core settings.
* Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.