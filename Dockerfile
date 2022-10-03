FROM python:3.10-slim-buster

# Install Requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY app/ /
COPY model/vinegar.pkl /vinegar.pkl

EXPOSE 80

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]