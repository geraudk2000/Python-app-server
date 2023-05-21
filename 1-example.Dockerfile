FROM python:3.11.3

COPY main.py .

ENTRYPOINT [ "python3", "main.py" ]
