# use an official Python runtime as a parent image
FROM python:3.11-slim

# Sets the working directory
WORKDIR /app

# I dont know if this works but it was suggested in the community page 
RUN echo 'nameserver 8.8.8.8' >/etc/resolve.conf

# Install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (portainer uses 8000)
EXPOSE 8080

# Run the Django app with Gunicorn
CMD [" gunicorn",  "--bind", "0.0.0.0:8080", "djangoJournalApp:application"]