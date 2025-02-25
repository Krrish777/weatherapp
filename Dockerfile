FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt install -y python3-flask
RUN apt install -y python3-requests
RUN apt install -y python3-bs4
RUN mkdir /app
RUN mkdir /app/templates
COPY app.py app.py
COPY templates/index.html /app/templates/index.html
COPY templates/result.html /app/templates/result.html
CMD python3 app.py
EXPOSE 5000