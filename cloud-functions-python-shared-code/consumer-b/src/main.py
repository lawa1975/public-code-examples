import functions_framework
import base64
import logging
import os
from google.cloud import logging as gcp_logging
from shared_code.model import MarketQuotation

LOG_LEVEL = logging._nameToLevel.get(os.environ.get('LOG_LEVEL'), logging.INFO)
BUCKET_NAME = os.environ.get('BUCKET_NAME')

gcp_logging.Client().setup_logging(log_level=LOG_LEVEL)
logger = logging.getLogger()

@functions_framework.cloud_event
def consumer_b_function(cloud_event):
    logger.info("Starting consumer_b_function...")

    decoded_data = base64.b64decode(cloud_event.data["message"]["data"]).decode()
    logger.debug(f"Consumer B message data: {decoded_data}")

    market_quotation = MarketQuotation.from_cloud_event(cloud_event)
    isin = market_quotation.security.isin
    logger.info(f"ISIN: {isin}")
