# use an official Python runtime as a parent image
FROM python:3.11-slim

# Sets the working directory
WORKDIR /app

# Install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY /scripts/wait-for-it.sh /scripts/wait-for-it.sh
RUN chmod +x /scripts/wait-for-it.sh

# Expose port 8080 (portainer uses 8000)
EXPOSE 8080

# Run the Django app with Gunicorn
CMD ["gunicorn",  "--bind", "0.0.0.0:8080", "mysite:application"]