FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install seaborn matplotlib

CMD ["python", "Dockwork.py"]