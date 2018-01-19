#docker build -t teilon/parts:site ./
#docker run --name parts -p 8000:8000 teilon/parts:site
#docker exec -it parts bash

FROM python:3.6
MAINTAINER teiloncw@gmail.com
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["./manage.py", "runserver"]
