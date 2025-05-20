import http.client
import requests
from requests.auth import HTTPBasicAuth
import json
import certifi
certifi.where()
'C:\\Program Files\\Common Files\\SSL\\cert.pem'

#Paloalto Rules automation backend

#ca_bundle_path = 'C:\\Program Files\\Common Files\\SSL\\AmazonRootCA.pem'


#Get Bearer Token ID

url = 'https://artcb.jfrog.io/artifactory/ai-vita-models/mobilenet/onnx/1.0.0/mobilenet_v2_feature_1.40_224.onnx'

payload = {
    'grant_type': 'client_credentials'
}
headers = {
  'Accept': 'application/x-www-form-urlencoded'
}


urlsec= 'https://www.airbnb.com'

#response = requests.request("get", url, auth=HTTPBasicAuth(username, password), headers=headers, data=payload, verify=ca_bundle_path)
urlsec= 'https://www.airbnb.com'
response = requests.request("GET", url)


print(response.text)



