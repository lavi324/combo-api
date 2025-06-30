# Use the official Python image (slim version) as the base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install the required Python packages
# FastAPI for the web framework, uvicorn as the ASGI server, and pymongo for database access
RUN pip install fastapi uvicorn pymongo

# Copy the FastAPI application code into the container
COPY app /app

# Expose port 8000 for the FastAPI service
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn server
# --host 0.0.0.0 is required to make it accessible outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
