from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'infra-project-220905'  


zone = 'asia-east1-a' 


instance = 'instance1'  

request = service.instances().get(project=project, zone=zone, instance=instance)
response = request.execute()


pprint(response)