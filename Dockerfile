FROM python:3.10

WORKDIR /app
COPY . /app

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install dependencies, including kaleido
RUN pip install --upgrade pip setuptools \
    && pip install scikit-learn -U kaleido \
    && pip install --no-cache-dir -r requirements.txt

# runs on localhoat and port 8080
EXPOSE 8080
CMD ["python3", "app.py"]