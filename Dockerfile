FROM python:3.8  

WORKDIR /usr/src/app  

COPY requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements.txt  

COPY . .  

ENV FLASK_APP=web_script.py  

CMD flask run --host=0.0.0.0
