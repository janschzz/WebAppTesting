# Use a lightweight Python base image
FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /app

# Expose port 80 inside the container
EXPOSE 80

# Define environment variables (optional defaults; real values set at runtime)
ENV DB_HOST=localhost
ENV DB_NAME=mydatabase
ENV DB_USER=postgres
ENV DB_PASS=secret
ENV DB_PORT=5432

# Gunicorn command to run the Flask app (named "app" in "app.py", variable "app")
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
