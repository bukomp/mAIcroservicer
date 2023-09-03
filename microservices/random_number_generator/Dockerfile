FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ADD . /app

RUN python -m unittest cli_test.py && \
    pyinstaller --onefile cli.py && \
    mv dist/cli /usr/local/bin/cli && \
    rm -rf build dist cli.spec

CMD ["python", "web_server.py"]