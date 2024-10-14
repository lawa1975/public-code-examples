# Python Virtual Environment

## Create
```
python -m venv .venv
```

## Activate
Windows using CMD:
```
path\to\venv\Scripts\activate.bat
```
Windows with PowerShell:
```
path\to\venv\Scripts\Activate.ps1
```

## Deactivate
Windows with CMD:
```
path\to\venv\Scripts\deactivate.bat
```

## Visual Code IDE
Enter Shift+Ctrl+P on Windows and Linux (Shift+Cmd+P on macOS) to open the Command Palette and click Python: Select Interpreter > + Enter interpreter path.

# Install dependencies
```
python -m pip install -r requirements.txt
```
or
```
pip install -r requirements.txt
```

# GCP

## Cloud Storage
Create bucket:
```
gcloud storage buckets create gs://shared-code-securities-recording-c3bb5c7b --project=gcp-playground-202401 --default-storage-class=STANDARD --location=europe-west1 --uniform-bucket-level-access
```

## Cloud run functions
Run on local machine with functions framework:
```
functions-framework-python --target producer_a http://127.0.0.1:8080
```

Deploy cloud run function (with Windows-like line breaks):
```
gcloud functions deploy python-shared-code-producer-a ^
--gen2 ^
--runtime=python312 ^
--region=europe-west1 ^
--source=./src ^
--entry-point=producer_a_function ^
--trigger-http ^
--allow-unauthenticated
```

Deploy *producer* function:
```
gcloud functions deploy python-shared-code-producer --gen2 --runtime=python312 --region=europe-west1 --source=./src --entry-point=producer_function --trigger-http --allow-unauthenticated --set-env-vars PROJECT_ID=gcp-playground-202401,TOPIC_ID=example-topic
```

Delete *producer* function:
```
gcloud functions delete python-shared-code-producer --gen2 --region=europe-west1
```

Deploy *consumer-a* function:
```
gcloud functions deploy python-shared-code-consumer-a --gen2 --runtime=python312 --region=europe-west1 --source=./src --entry-point=consumer_a_function --trigger-topic=example-topic --set-env-vars BUCKET_NAME=shared-code-securities-recording-c3bb5c7b
```

Deploy *consumer-b* function:
```
gcloud functions deploy python-shared-code-consumer-b --gen2 --runtime=python312 --region=europe-west1 --source=./src --entry-point=consumer_b_function --trigger-topic=example-topic
```

## Pub/Sub
Create topic:
```
gcloud pubsub topics create example-topic
```

Create subscription:
```
gcloud pubsub subscriptions create example-topic-sub-default --topic=projects/gcp-playground-202401/topics/example-topic
```

Publish message to topic:
```
gcloud pubsub topics publish projects/gcp-playground-202401/topics/example-topic --message="Robbie Williams" --attribute="origin=gcloud-sample,username=gcp,eventTime='2021-01-01T12:00:00Z'"
```

# Data
```json
{
  "isin": "US2441991054",
  "market_value": 71.1115
}
```

# References
- https://cloud.google.com/functions/docs/create-deploy-http-python
- https://cloud.google.com/functions/docs/writing/write-event-driven-functions
- https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create
- https://pypi.org/project/google-cloud-pubsub/
- https://cloud.google.com/functions/docs/configuring/env-var
- https://cloud.google.com/functions/docs/monitoring/error-reporting#functions-errors-log-python
- https://medium.com/analytics-vidhya/how-to-write-and-get-a-json-file-in-google-cloud-storage-when-deploying-flask-api-in-google-app-9121fa936d85
- https://github.com/GoogleCloudPlatform/functions-framework-python/blob/main/README.md
- https://medium.com/google-cloud/setup-and-invoke-cloud-functions-using-python-e801a8633096
- https://www.computerwoche.de/a/virtual-environments-in-python-erklaert,3615103
- https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data