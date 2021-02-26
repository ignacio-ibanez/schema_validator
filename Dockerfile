FROM python:3

WORKDIR /usr/schema_validator/

COPY ./ ./

RUN pip install -r requirements.txt

CMD ["python3", "src/schema_validator.py"]
