# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN echo "CyberBlitz{lzbJhNIfmkShNqkIgoccr468JSyWsr3Zju}" > /root/flag.txt

# Copy the Django project files into the working directory
COPY . /app/

EXPOSE 4444

# Expose the port that the Django development server will run on
EXPOSE 8000

# Define the command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
