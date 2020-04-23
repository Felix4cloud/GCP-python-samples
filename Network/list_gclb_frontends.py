from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)


# Project ID for this request.
project = 'infra-project-220905'
batch = service.new_batch_http_request()
proxies=[]
frontends=[]

def appendProxyLink(request_id,result,exception):
    if 'items' in result:
        for item in result['items']:
            proxies.append(item['selfLink'])

def appendFrontend(request_id,result,exception):
    if 'forwardingRules' in result['items']['global']:
        frontends.extend(result['items']['global']['forwardingRules'])


batch.add(service.targetHttpsProxies().list(project=project,
                                            filter='urlMap:"https://www.googleapis.com/compute/v1/projects/infra-project-220905/global/urlMaps/cdn-lb-lab"'),
                                            callback=appendProxyLink)
batch.add(service.targetHttpProxies().list(project=project,
                                           filter='urlMap:"https://www.googleapis.com/compute/v1/projects/infra-project-220905/global/urlMaps/cdn-lb-lab"'),
                                           callback=appendProxyLink)
batch.execute()



batch = service.new_batch_http_request()
for proxy in proxies:
    batch.add(service.forwardingRules().aggregatedList(project=project,
                                                       filter ='target:"%s"'%(proxy)),
                                                       callback=appendFrontend)
batch.execute()
for frontend in frontends:
    print('IPAddress:',frontend['IPAddress'],'PortRange: ', frontend['portRange'])
