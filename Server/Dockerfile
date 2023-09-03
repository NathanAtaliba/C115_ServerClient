FROM python:3

WORKDIR /Server

ENV client = pymongo.MongoClient("mongodb://localhost:27017/")
 
EXPOSE 8000

RUN pip install pymongo

COPY . .

# Run the application.
CMD ["python", "server.py"]
