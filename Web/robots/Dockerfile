# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app/src
WORKDIR /app

# Copy the contents of the src folder to /app/src in the container
COPY ./app .

# Expose the port that the app runs on
EXPOSE 8000

# Run the Python script when the container launches
ENTRYPOINT ["python3", "server.py"]
