import base64
import json
from security import Security


class MarketQuotation:
  
  def __init__(self, timestamp, security, market_value):
    # unix epoch timestamp
    self.timestamp = timestamp
    # security
    self.security = security
    # market value in USD
    self.market_value = market_value

  @staticmethod
  def from_cloud_event(cloud_event):
    decoded_data = base64.b64decode(cloud_event.data["message"]["data"]).decode()
    return MarketQuotation.from_json(decoded_data)

  @staticmethod
  def from_json(input_json):
    input_dict = json.loads(input_json)

    timestamp = input_dict['timestamp']
    market_value = input_dict['market_value']
    security = Security.from_dict(input_dict['security'])
    
    return MarketQuotation(timestamp, security, market_value)

  def to_json(self):
    data = {
        'timestamp': self.timestamp,
        'security': self.security.to_dict(),
        'market_value': self.market_value
    }   
    return json.dumps(data)
