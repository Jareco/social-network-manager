# Use an official Python runtime as a parent image
FROM python:3.6


# Add file to image for later use
ADD requirements.txt /requirements.txt

# Use pip to install dependencies
RUN pip install --trusted-host pypi.python.org -r /requirements.txt

COPY ./src /app/


# Run app.py when the container launches
CMD ["python", "/app/app.py"]
