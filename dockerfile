# Use the official Python image.
FROM python:3.10-alpine

# Set the working directory.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY app/APP . 

# Install any needed packages specified in pyproject.toml
RUN pip install poetry


# Run main.py when the container launches
CMD ["python", "app/main.py"]
