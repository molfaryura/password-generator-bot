FROM python:3.10

ADD telegram_bot.py .

ENV BOT_TOKEN = 'token'

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python3", "telegram_bot.py"]
