FROM locustio/locust

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

EXPOSE 8089

CMD ["locust -f /usr/src/app/locustfile.py"]