FROM python
MAINTAINER Tommaso perondi "tommaso.perondi@delirium.dev"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 9090

# exectute start up script
#ENTRYPOINT ["/entrypoint.sh"]

CMD ["uwsgi", "--ini", "/app/app.ini"]