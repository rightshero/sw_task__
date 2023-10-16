![alt text](https://rightshero.com/public/assets/pp-assets/images/rh-logo.png)

# Overview:

This project is a part of the Rightshero software development team's efforts to handle various software aspects of their service. As a software engineer, the task assigned was to create a dynamic web application with a category and subcategory selection system. The objective was to allow users to choose from a set of categories and subcategories in a user-friendly and interactive manner.

![Alt text](image.png)
![Alt text](image-1.png)
![Alt text](image-2.png)

# Project Structure:

sw_task/
├── .dockerignore
├── .env
├── .gitignore
├── commands.txt
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
├── wait_for_db.py
├── base/
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── **init**.py
│ └── **pycache**/
├── categories/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── **init**.py
│ ├── migrations/
│ ├── templates/
│ │ ├── categories.html
│ │ └── stuff/
│ │ ├── footer.html
│ │ ├── head.html
│ │ └── index.html
│ ├── static/
│ ├── css/
│ │ ├── main.css
│ ├── images/
│ │ ├── rightshero.png
│ ├── js/
│ ├── func.js
├── venv/

## Getting Started

> git clone https://github.com/Abdelrhmantarek/sw_task.git
> cd sw_task

> docker-compose up --build

# Notes

# Deliverables
