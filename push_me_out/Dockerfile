# Fetch Python3.7.7
FROM python:3.7.7-stretch

# Set Environment Variable PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

# Set Working Directory
WORKDIR /code

# Copy project into /code/
COPY . /code/

# Navigate to /code
RUN cd /code

# Install requirements
RUN pip install -r requirements.txt

