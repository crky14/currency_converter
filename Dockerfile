FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 ./currency_converter_api.py
