# An official Python runtime as a parent image
FROM python:3.8-slim-buster

# Ensure to output everything that's printed inside
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt 

# Copy the current directory contents into the container at /app
COPY . .

# Expose a port that the app will run on
EXPOSE 8000

