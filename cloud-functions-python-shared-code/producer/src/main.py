import functions_framework
import logging
import os
from google.cloud import pubsub_v1
from google.cloud import logging as gcp_logging

from datetime import datetime
from shared_code.model import MarketQuotation, Security

LOG_LEVEL = logging._nameToLevel.get(os.environ.get('LOG_LEVEL'), logging.INFO)
PROJECT_ID = os.environ.get('PROJECT_ID')
TOPIC_ID = os.environ.get('TOPIC_ID')

KNOWN_SECURITIES = {
    'US0378331005': 'Apple',
    'US2441991054': 'Deere & Co.',
    'US37045V1008': 'General Motors Company',
    'US67066G1040': 'NVIDIA Corp.',
    'US7134481081': 'PepsiCo, Inc.'
}

gcp_logging.Client().setup_logging(log_level=LOG_LEVEL)
logger = logging.getLogger()

def is_valid_input(json):
    return json and 'market_value' in json and 'isin' in json

def stringify_timestamp(posix_timestamp):
    return str(posix_timestamp).replace('.', '').ljust(16, '0')

@functions_framework.http
def producer_function(request):
    logger.info("Starting producer_function...")
  
    request_json = request.get_json(silent=True)

    if not is_valid_input(request_json):
        return 'Bad Request', 400
    
    isin = request_json['isin'].strip().upper()
    name = KNOWN_SECURITIES.get(isin)

    if name is None:
        return 'Not Found', 404

    market_quotation = MarketQuotation(
        stringify_timestamp(datetime.now().timestamp()),
        Security(isin, name),
        request_json['market_value'])

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)
    message = market_quotation.to_json().encode("utf-8")
    publisher.publish(topic_path, message)

    logger.info(f"Message published: {message}")

    return 'OK'
