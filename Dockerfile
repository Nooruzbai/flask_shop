# pull official base image
FROM python:3.10.12

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y libffi-dev
RUN apt-get install -y netcat-traditional


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


# copy project
COPY . /usr/src/app/
RUN chmod 777 entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]