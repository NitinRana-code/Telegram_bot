FROM python:3.8
COPY . .
RUN pip install python-telegram-bot

CMD python main.py