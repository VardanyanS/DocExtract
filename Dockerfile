# Base image
FROM python:3.8

# Set working directory
WORKDIR /DocExtract

# Copy project files to the working directory
COPY . /DocExtract

# Install project dependencies
RUN pip install -r requirements.txt

# Specify the command to run your application
CMD ["python", "app.py"]