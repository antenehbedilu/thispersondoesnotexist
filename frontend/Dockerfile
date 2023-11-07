#use the Python 3.11 slim base image
FROM python:3.11-slim

#set the working directory inside the container to /app
WORKDIR /app

#copy the current directory source code (/backend) into the container directory (/app)
COPY . /app

#install the required dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#start the web server (frontend) at port 8501
CMD streamlit run app.py --server.port=8501 --server.address=0.0.0.0

#build and run the docker image
#docker build -t streamlit-service:1.0 .
#docker run -d -p 8501:8501 --name thispersondoesnotexistApp streamlit-service:1.0
