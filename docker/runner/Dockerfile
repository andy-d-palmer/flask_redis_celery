# Use base python image with python 3
FROM python:3.6

# Create app directory
RUN mkdir /app
WORKDIR /app

# Add requirements.txt to the image
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
