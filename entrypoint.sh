#!/bin/bash

# Check if the migrations folder exists
if [ ! -d "migrations" ]; then
    echo "Initializing migrations..."
    flask db init
fi

# Run database migrations
echo "Running migrations..."
flask db upgrade

# Start the Flask app
echo "Starting Flask app..."
flask run --host=0.0.0.0 --port=5001
