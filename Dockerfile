# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . /app

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh


# Ensure entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Set the entrypoint script to start Flask and apply migrations
ENTRYPOINT ["/app/entrypoint.sh"]

# Expose port 5001 for Flask app
EXPOSE 5001
