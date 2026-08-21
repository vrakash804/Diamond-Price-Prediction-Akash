# Use Python 3.11 because the project dependencies require Python 3.9+
FROM python:3.11-slim

# Set the working directory
WORKDIR /service

# Copy the project files
COPY . ./

# Install Python dependencies
RUN pip install -r requirements.txt

# Start the Flask application
CMD python app.py