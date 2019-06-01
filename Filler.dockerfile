FROM python:3.6

RUN pip install --trusted-host pypi.python.org mysql-connector

COPY ./filler /filler/

CMD ["python", "/filler/filler.py"]
