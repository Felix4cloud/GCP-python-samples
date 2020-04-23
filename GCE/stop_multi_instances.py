from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'infra-project-220905'
batch = service.new_batch_http_request()
response = []
batch = service.new_batch_http_request(callback=lambda request_id, result, exception: response.append(result))
batch.add(service.instances().stop(project=project, zone='asia-east1-a', instance='instance'))
batch.add(service.instances().stop(project=project, zone='asia-east1-a', instance='instance-1'))
batch.execute()
pprint(response)