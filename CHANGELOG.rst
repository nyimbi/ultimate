
Changelog
=========

{{ cookiecutter.version }} ({{ '<TODAY>' if cookiecutter.release_date == 'today' else cookiecutter.release_date }})
------------------

* First release on PyPI.


History
========

So there I was learning Django, and fantastic though it was, there was just way too much biolerplate to write.
So I decided that I would create a template for future django apps that would limit the boring stuff, and remove me from
having to work on plumbing and focus on the business requirements. In researching this I came across cookiecutter and the famous
cookiecutter-django. I bethought myself to modify this, taking in all the best practices that I could find in other implementations,
and thus the "Ultimate-Cookiecutter-Django" was born.

All credit to those on whose giant shoulders I stand.
- cookiecutter-django
- cookiecutter-djangopackage
- django-application-template
- cookiecutter-pylibrary


This is still very much a work in progress, and still has a ways to go

TODO
====
- Auto generate multiple apps
- Auto generate models in those apps
- Create a CRUD infrastructure for each app
- Create a sleek home page
