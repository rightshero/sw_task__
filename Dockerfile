# Use an official Python runtime as a parent image
FROM python:3.11.1

# Set environment variables for PostgreSQL
ENV POSTGRES_DB categories_task
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 1234
ENV POSTGRES_HOST localhost
ENV POSTGRES_PORT 5432

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the Django app to listen on
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
