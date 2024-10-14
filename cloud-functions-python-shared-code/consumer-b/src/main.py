import functions_framework
import base64
#from shared_code.model import MarketQuotation


@functions_framework.cloud_event
def consumer_b_function(cloud_event):
    decoded_data = base64.b64decode(cloud_event.data["message"]["data"]).decode()
    print(f"Consumer B message data: {decoded_data}")

#   market_quotation = MarketQuotation.from_cloud_event(cloud_event)
#    isin = market_quotation.security.isin
#    print(f"ISIN: {isin}")
