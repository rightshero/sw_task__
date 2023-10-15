# Software Engineer Task Assessment

# Overview

This project represents the successful completion of the Rightshero Software Engineer Task Assessment.
I've crafted a dynamic category selection system that utilizing Postgresql as the database, adhering to the MVC pattern,
and implementing robust security measures through middlewares.

# Installation & Usage
To set up the project and run it locally, follow these steps:

- 1- Clone this repository to your local machine
- 2- Access the Dockerfile in the project directory.
- 3- Build the Docker container by running the following command:
```
docker-compose build
```
- 4- Once the build process is complete, start the container using the following command:
```
docker-compose up
```
- 5- The application is now running, and you can access it in your web browser at [localhost:8000](http://127.0.0.1:8000/)
- 6- You can access the admin panel at [localhost:8000/admin](http://127.0.0.1:8000/). I've created a ready superuser with the following credentials:
  - Username: admin
  - Password: admin
- 7- Alternatively, you can create a new superuser for a better overview of the application and database. Use the following command: Please note that you should run this command in another terminal while the application is running
```
docker-compose run web python manage.py createsuperuser
```
- 8- Accessing the Admin Panel will allow you to have a better overview over the DB and create as many parent categories as needed ( a parent category is a category with no parent ) and see the generated subcategories.
- 9- I've also created two parent categories to get you started with trying out the app right away.
     


# Technology Stack

This app is built using the following technologies:

- **Django**: A Python web framework.

- **PostgreSQL**: A relational database management system.

# Deployment and Infrastructure

- **Docker**:  The application is containerized using Docker, providing an efficient and consistent deployment environment.

## Database Design

This project's database design follows a simple and efficient approach to accommodate an unlimited level of 
subcategories for a parent category. I achieve this by using a single table with a foreign key relationship to itself.

This design allows for a parent category to have multiple subcategories, and subcategories can, in turn, have their 
own subcategories, creating a hierarchy of categories with an unlimited number of levels.

By using this self-referencing foreign key relationship, the database can efficiently represent and retrieve
hierarchical category structures.

# Security

While this application may not include user authentication, I've implemented several security measures to ensure its 
robustness and protect against common web security threats. Here are some of the security middlewares 
provided by Django that I've utilized:

- **SecurityMiddleware:** This middleware helps enforce several security best practices.

- **SessionMiddleware:** Although there's no user authentication in this simple app, SessionMiddleware is used to manage user sessions securely. It ensures that session data is stored securely and handles session management.

- **CommonMiddleware:** CommonMiddleware provides security features such as clickjacking protection and secure HTTP headers.

- **CsrfViewMiddleware:** Cross-Site Request Forgery (CSRF) protection, even in applications without user authentication. CsrfViewMiddleware safeguards against CSRF attacks by adding a unique token to forms and ensuring that form submissions match this token.

- **XFrameOptionsMiddleware:** This middleware helps prevent clickjacking attacks by setting X-Frame-Options headers, which control whether the application can be embedded in an iframe.

By incorporating these security middlewares, I've taken steps to fortify the application's security posture, making it resilient to a range of common web vulnerabilities.

# Testing

- TestCase class is used to wright unit testing for the views. and you can run tests by using the command:
```
docker-compose run web python manage.py test categories_app
```

# Conclusion

Thank you for reviewing my Rightshero Software Engineer Task Assessment. I look forward to your feedback and appreciate the opportunity to demonstrate our skills.