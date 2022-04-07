FROM python

COPY ./ /telegram-bot
RUN pip install -r /telegram-bot/requirements.txt


CMD [ "python3", "/telegram-bot/webhook.py" ]