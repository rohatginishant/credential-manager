import json

data = {
    "jenkins1": {
        "jenkins__url": "http://44.212.71.109:8080/manage/credentials/store/system/domain/_/",
        "auth__username": "admin",
        "auth__password": "1187c4bb500c1cf2595c14fde4f06e0668",
        "select": 0,
        "crumbIssuer": "http://44.212.71.109:8080//crumbIssuer/api/json"
    },
    "jenkins2": {
        "jenkins__url": "http://54.82.246.227:8080/manage/credentials/store/system/domain/_/",
        "auth__username": "admin",
        "auth__password": "1193800ffbb402984f1f6516944ede9731",
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

