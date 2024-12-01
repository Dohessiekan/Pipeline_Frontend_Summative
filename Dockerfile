# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install Flask
RUN pip install Flask

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project directory (including templates) into the container
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run Flask (on all interfaces so it can be accessed outside the container)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
