from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

if __name__ == '__main__':
    # Make sure the credential has the privilege to access billing info: 
    # https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam
    credentials = GoogleCredentials.get_application_default()
   
    service = discovery.build('cloudbilling', 'v1', credentials=credentials)

    print(service.billingAccounts().list().execute())