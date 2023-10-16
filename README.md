![alt text](https://rightshero.com/public/assets/pp-assets/images/rh-logo.png)

# Overview:

This project is a part of the Rightshero software development team's efforts to handle various software aspects of their service. As a software engineer, the task assigned was to create a dynamic web application with a category and subcategory selection system. The objective was to allow users to choose from a set of categories and subcategories in a user-friendly and interactive manner.

![Alt text](https://raw.githubusercontent.com/Abdelrhmantarek/imgg/main/1.png?token=GHSAT0AAAAAACCJPID27KOT425RLBSIGYLOZJM2WVQ)
![Alt text](https://raw.githubusercontent.com/Abdelrhmantarek/imgg/main/3.png?token=GHSAT0AAAAAACCJPID2L5SWEWSFXJZJBYUWZJM2Y6Q)
![Alt text](https://raw.githubusercontent.com/Abdelrhmantarek/imgg/main/2.png?token=GHSAT0AAAAAACCJPID3T525AFG6PROWSRMEZJM2W4A)

# Project Structure:

'''bash

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

'''

# Getting Started

```
> git clone https://github.com/Abdelrhmantarek/sw_task.git
> cd sw_task
```

```
> docker-compose up --build
```

# Manipulating With Postman

## get_subcategories

![Alt text](https://raw.githubusercontent.com/Abdelrhmantarek/imgg/main/get.png?token=GHSAT0AAAAAACCJPID2YFZWGQIOPBZ2FF5IZJM2RPQ)

## create_subcategories

![Alt text](https://raw.githubusercontent.com/Abdelrhmantarek/imgg/main/create.png?token=GHSAT0AAAAAACCJPID3IAUKOXJKILTJJ74UZJM2R5Q)

## delete_subcategories

![Alt text](https://raw.githubusercontent.com/Abdelrhmantarek/imgg/main/delete.png?token=GHSAT0AAAAAACCJPID225R7JLQ2MSIXXC4MZJM2SEQ)

# Implementation Details

## Database Design:

Database System: PostgreSQL.
Table Design: Utilized a single table to store both categories and subcategories, ensuring a streamlined and efficient database structure.

## Architecture/Code

Code Structure: Followed best practices for code organization, resulting in a clean and maintainable codebase.
MVC Model: Adhered to the Model-View-Controller (MVC) architectural pattern to separate concerns, enhance scalability, and improve code readability.

## Security

Django Security Features: Leveraged built-in Django security features to protect the project against common vulnerabilities.
Secret Key Protection: Implemented security measures to safeguard sensitive information, such as the secret key, to enhance project security.

## Git Usage

Collaborative Workflow: Collaborated on the project using Git and GitHub, enabling version control and well-documented commit messages for maintaining project integrity and facilitating collaboration.

# Summary

The project was executed with excellence, resulting in a dynamic web application that empowers users to intuitively select categories and subcategories
