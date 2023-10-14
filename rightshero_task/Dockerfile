# Use Python runtime as a parent image
FROM python:3.11

# Set environment variables, now stdout and stderr are being stored in a buffer until a certain
# amount of data is accumulated
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/

RUN pip install -r requirements.txt

