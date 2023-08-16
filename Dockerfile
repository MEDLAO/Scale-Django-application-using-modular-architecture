# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /Project_13_container

# Set the working directory to /Project_13_container
WORKDIR /Project_13_container

# Copy the current directory contents into the container at /Project_13_container
ADD . /Project_13_container/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
