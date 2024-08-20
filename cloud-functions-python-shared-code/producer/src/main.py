import functions_framework
import os
from google.cloud import pubsub_v1
from security import Security
from market_quotation import MarketQuotation
from datetime import datetime


PROJECT_ID = os.environ.get('PROJECT_ID')
TOPIC_ID = os.environ.get('TOPIC_ID')

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@functions_framework.http
def producer_function(request):
    request_json = request.get_json(silent=True)

    if not request_json:
        return
    
    if 'market_value' not in request_json:
        return
    
    now = str(datetime.now().timestamp()).replace('.', '')

    security = Security('US0378331005', 'Apple')

    market_quotation = MarketQuotation(now, security, request_json['market_value'])

    data = market_quotation.to_json().encode("utf-8")

    publisher.publish(topic_path, data)
    
    return 'Here is the producer A function!'
