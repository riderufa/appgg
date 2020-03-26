FROM python:3.7.6

ENV PORT 8081

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app/app.py /app/app.py
COPY ./app/main.py /app/main.py
COPY ./app/config.py /app/config.py
COPY ./app/view.py /app/view.py
COPY ./app/templates/index.html /app/templates/index.html

ENTRYPOINT ["python"]

CMD ["main.py"]