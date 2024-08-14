import functions_framework
import base64

@functions_framework.cloud_event
def consumer_b_function(cloud_event):
    decoded_data = base64.b64decode(cloud_event.data["message"]["data"]).decode()
    print("Consumer B message data: " + decoded_data)
