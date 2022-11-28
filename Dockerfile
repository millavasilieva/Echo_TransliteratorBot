FROM python:3.9.5
ENV TOKEN='your token'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py