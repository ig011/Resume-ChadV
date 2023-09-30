# Pull the Python base image 
FROM python:3.9.18-slim-bullseye

# Set working directory
WORKDIR /code

# Install PDF utility to convert HTM to PDF using Webkit
RUN apt-get update && apt-get install wkhtmltopdf -y

# Copy requirements.txt file to install necessary dependencies
COPY ./requirements.txt /code/requirements.txt

# Upgrade pip and install all the dependencies from requirements.txt file
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the current directory
COPY ./ /code

# Run python to generate the resume
ENTRYPOINT ["python", "main.py", "--build"]
