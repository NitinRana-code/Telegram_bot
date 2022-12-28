FROM python:3.8
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install python-telegram-bot
RUN pip install openai telepot

CMD python main.py