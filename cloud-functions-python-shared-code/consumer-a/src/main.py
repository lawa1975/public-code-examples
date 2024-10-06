import functions_framework
import os
from google.cloud import storage
from shared_code.model import MarketQuotation


BUCKET_NAME = os.environ.get('BUCKET_NAME')

@functions_framework.cloud_event
def consumer_a_function(cloud_event):
    market_quotation = MarketQuotation.from_cloud_event(cloud_event)
    isin = market_quotation.security.isin
    timestamp = market_quotation.timestamp

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(f"market_quotations/{isin}/quotation_{isin}_{timestamp}.json")
    blob.upload_from_string(data=market_quotation.to_json(), content_type='application/json')
