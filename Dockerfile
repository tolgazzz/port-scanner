FROM python:3.11.15

WORKDIR /src

COPY requirements.txt . 

#RUN pip install -r requirements.txt

COPY main.py .

CMD [ "python", "main.py" ]