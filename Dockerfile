# FROM python:3.12
# Use the official Python image as the base image
# Set the working directory to /app
# Copy the current directory contents into the container at /app
# Install any needed packages specified in requirements.txt
# Make port 80 available to the world outside this container
# Define environment variable
# Run app.py when the container launches

FROM python:3.12
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python3", "app.py"]