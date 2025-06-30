# Use the official Python image (slim version) as the base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Flask and Gunicorn
RUN pip install flask gunicorn

# Copy the Flask app code and templates into the container
COPY . /app

# Expose port 5000 for the Flask service
EXPOSE 5000

# Command to run the Flask app with Gunicorn
# Gunicorn will listen on 0.0.0.0:5000 and serve our Flask application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
