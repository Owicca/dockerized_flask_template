FROM python:latest
EXPOSE 5000
WORKDIR /app
ADD . /app
RUN apt update -y && apt upgrade -y && \
      pip install -r requirements.txt
ENV FLASK_APP wsgi.py
CMD ["flask", "run", "--host=0.0.0.0"]
