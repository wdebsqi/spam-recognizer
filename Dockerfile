FROM python:3
COPY /app /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD [ "python3", "train_model.py" ]
CMD [ "python3", "app.py" ]