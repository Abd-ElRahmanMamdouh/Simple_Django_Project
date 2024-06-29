# Simple Django project

This is a Simple Django project.

## Installation

You can download the repo or clone it using git clone.

```bash
git clone https://github.com/Abd-ElRahmanMamdouh/Simple_Django_Project.git .
```

## Requirements
Create your venv and install the requirements

```bash
pip install -r requirements.txt
```

## Usage

Run migrate and create super user before using.
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Features 
### CRUD Operations Page

Simple CRUD Operations for book table.

### Dynamic URL Parameter Page

Simple page to display Multiplication Table for any given number in the url parameter (?number=1).


### Django Messages with sweet alert
you can go to templates/base/messages.html to edit colors and styling of sweet alert, see more on [Docs](https://sweetalert2.github.io/)

### Pagination ready template
at templates/base/pagination.html you can go to style your pagination nav, and if you have a model with pagination all you gotta do is include that template inside your list template like so, Note you set objects=page_obj if you using pagination in CVB and objects=your_list_varibale if you are using FBV
```html
CBV
{% include "base/pagination.html" with objects=page_obj %}
FBV
{% include "base/pagination.html" with objects=your_list_varibale %}
```

## Useful Tips

I'm using flake8 and black to obtain clean code with Pep-8
create a file called .flake8
and paste these in it

```bash
[flake8]
exclude =
    migrations,
    __pycache__,
    manage.py,
    settings.py
max-line-length = 99
```

To see your mistakes run
```bash
flake8
```

You can go ahead and correct them manually or do it automatically with black like this

```bash
black path/to/file.py
```

# Happy Coding