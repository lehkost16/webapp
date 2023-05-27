FROM python

EXPOSE 5000

WORKDIR /app

COPY requirments.txt /app
RUN pip install -r requirments.txt

COPY app.py /app
CMD python app.py
