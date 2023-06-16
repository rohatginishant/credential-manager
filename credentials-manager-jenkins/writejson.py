import json
import boto3

# boto3.setup_default_session(profile_name='n3')
ssm = boto3.client('ssm')

jenkins1_token = ssm.get_parameter(Name='/jenkins1', WithDecryption=True)
jenkins2_token = ssm.get_parameter(Name='/jenkins2', WithDecryption=True)

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
