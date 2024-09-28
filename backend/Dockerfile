# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any Python dependencies
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
