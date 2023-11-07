#use the Python 3.11 slim base image
FROM python:3.11-slim

#set the working directory inside the container to /app
WORKDIR /app

#copy the current directory source code (/backend) into the container directory (/app)
COPY . /app

#install the required dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#start the web server (uvicorn) at port 8080
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8080

#build and run the docker image
#docker build -t fastapi-service:1.0 .
#docker run -d -p 8080:8080 --name thispersondoesnotexistAPI fastapi-service:1.0
