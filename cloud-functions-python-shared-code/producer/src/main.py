import functions_framework
import os
import json
from google.cloud import pubsub_v1

PROJECT_ID = os.environ.get('PROJECT_ID')
TOPIC_ID = os.environ.get('TOPIC_ID')

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@functions_framework.http
def producer_function(request):
    request_json = request.get_json(silent=True)

    if request_json and 'isin' in request_json:
        isin = request_json['isin']

    if request_json and 'price' in request_json:
        price = request_json['price']

    stock_price = {
        'isin': isin,
        'price': price,
    }

    data = json.dumps(stock_price).encode("utf-8")

    publisher.publish(topic_path, data)
    
    return 'Here is the producer A function!'
