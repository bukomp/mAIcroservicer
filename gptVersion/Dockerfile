FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m unittest

RUN pip install pyinstaller
RUN pyinstaller --onefile -n cli_app cli.py
ENV PATH="/app/dist:${PATH}"

CMD [ "python", "./web_server.py" ]