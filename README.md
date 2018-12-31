# Django Blog :clipboard:
Play with Django framework based on Coding For [*Entrepreneurs tutorials*](https://github.com/codingforentrepreneurs). 

## Preview
 Home| Post Preview | Post Form
  ---|---|---
![alt text](https://github.com/ggeop/Django_blog/blob/master/img/posts-list.PNG) |![alt text](https://github.com/ggeop/Django_blog/blob/master/img/post-preview.PNG) | ![alt text](https://github.com/ggeop/Django_blog/blob/master/img/post-form.PNG)

[*Based on Bootstrap theme:*]https://github.com/BlackrockDigital/startbootstrap-blog-home

## Features
* Responsive
* Admin page (create, update & delete posts)
* Draft posts and future posts
* Search posts
* Dynamic URL rooting + URL slags
* Pagination
* Facebook api for comments + likes

## Requirements
* [*Python 3.x*](https://www.python.org/downloads/release/python-360/)
* [*Django 1.8*](https://docs.djangoproject.com/en/2.1/releases/1.8/)

## Setup Environment
Create virtual env with virtualenv.
Install virtualenv if you don't have installed yet

```bash
pip install virtualenv
```

```bash
# Create python virtual env dir
mkdir py_env

# Create project virtual env
virtualenv py_env

# Install all the project libraries via pip
pip install -r requirements.txt

# Activate the python project env
source py_env/bin/activate
```
## Run Server
```bash
python manage.py runserver
```
