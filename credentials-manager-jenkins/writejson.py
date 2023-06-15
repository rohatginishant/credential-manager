import json
import boto3

# boto3.setup_default_session(profile_name='n3')
ssm = boto3.client('ssm')

jenkins1_token = ssm.get_parameter(Name='/jenkins1', WithDecryption=True)
jenkins2_token = ssm.get_parameter(Name='/jenkins2', WithDecryption=True)
print(jenkins1_token['Parameter']['Value'])
print(jenkins2_token['Parameter']['Value'])

# jenkins_url = 'http://44.212.71.109:8080/manage/credentials/store/system/domain/_/'
# jenkins_auth_username = 'admin'
# jenkins_auth_token = '1187c4bb500c1cf2595c14fde4f06e0668'

data = {
    "jenkins1": {
        "jenkins__url": "http://44.212.71.109:8080/manage/credentials/store/system/domain/_/",
        "auth__username": "admin",
        "auth__password": jenkins1_token['Parameter']['Value'],
        "select": 0,
        "crumbIssuer": "http://44.212.71.109:8080//crumbIssuer/api/json"
    },
    "jenkins2": {
        "jenkins__url": "http://54.82.246.227:8080/manage/credentials/store/system/domain/_/",
        "auth__username": "admin",
        "auth__password": jenkins2_token['Parameter']['Value'],
        "select": 0,
        "crumbIssuer": "http://54.82.246.227:8080//crumbIssuer/api/json"
    },
    "jenkins3": {
        "jenkins__url": "http://example.com/jenkins3",
        "auth__username": "admin3",
        "auth__password": "password3",
        "select": 0,
        "crumbIssuer": "http://54.82.246.227:8080//crumbIssuer/api/json"
    }
}

# Writing the dictionary to a JSON file
with open("cred.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# with open("cred.json", "r") as json_file:
#     data = json.load(json_file)
#
# # Add a new dictionary to the data
# new_jenkins = {
#     "jenkins4": {
#         "jenkins_url": "http://example.com/jenkins4",
#         "auth_username": "admin4",
#         "auth_password": "password4"
#     }
# }
# data.update(new_jenkins)
