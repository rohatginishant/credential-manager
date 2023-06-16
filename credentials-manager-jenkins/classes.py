import requests
import xml.etree.ElementTree as ET
import urllib.parse
import json
from writejson import data





class Credentials:

    def __init__(self, jenkins_url, auth_username, auth_token):
        self.jenkins_url = jenkins_url
        self.auth_username = auth_username
        self.auth_token = auth_token

    def create_username_with_password(self, id, username, password, crumb_url):
        jenkins_url_createfunction = self.jenkins_url + 'createCredentials'
        # crumb_url = 'http://44.212.71.109:8080//crumbIssuer/api/json'
        jenkins_crumb = requests.get(crumb_url)
        crumb = jenkins_crumb.json()["crumb"]
        # print(f"Jenkins crumb data = {jenkins_crumb.json()}")

        Head = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Jenkins_Crumb': crumb
        }

        username_set = username
        id_set = id
        password_set = password

        data = {
            "": "0",
            "credentials": {
                "scope": "GLOBAL",
                "username": username_set,
                "usernameSecret": "false",
                "password": password_set,
                "$redact": "password",
                "id": id_set,
                "description": "description",
                "stapler-class": "com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl",
                "$class": "com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl"
            }
        }

        data = json.dumps(data)

        response = requests.post(
            jenkins_url_createfunction,
            auth = (self.auth_username, self.auth_token),
            headers = Head,
            data = {'json': data}
        )
        if response.status_code == 200:
            print("Credentials created ")
            return "hello , you have created username-password successfully !!! "

    def create_ssh_with_private_key(self, id, description, username, privatekey, usernameSecret, crumb_url):
        jenkins_url_createfunction = self.jenkins_url + 'createCredentials'
        jenkins_crumb = requests.get(crumb_url)
        crumb = jenkins_crumb.json()["crumb"]

        Headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Jenkins_Crumb': crumb
        }

        username_set = username
        id_set = id
        private_key_set = privatekey
        description_set = description
        usernameSecret_set = usernameSecret

        data = {
            "": "3",
            "credentials":{
                "scope": "GLOBAL",
                "id": id_set,
                "description": description_set,
                "username": username_set,
                "usernameSecret": usernameSecret_set,
                "privateKeySource":
                    {
                        "value": "0",
                        "privateKey": private_key_set,
                        "stapler-class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource",
                        "$class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource"
                     },
                "passphrase": "op",
                "$redact": "passphrase",
                "stapler-class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey",
                "$class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey"
            },
        }

        data = json.dumps(data)

        response = requests.post(jenkins_url_createfunction,
                                 auth=(self.auth_username, self.auth_token),
                                 headers=Headers,
                                 data={'json':data})

        if response.status_code == 200:
            print("Credentials created ")
            return "hello , you have created ssh credentials successfully !!! "
    def manage_username_with__password(self, id, new_id, new_name, new_pass,update):
        # id = input("Enter id : ")
        Headers = {
            'Content-Type': 'application/xml'
        }

        jenkins_url_updatefunction = self.jenkins_url + f'credential/{id}/config.xml'
        response2 = requests.get(jenkins_url_updatefunction, auth=(self.auth_username, self.auth_token), headers=Headers)
        data = response2.text
        print(f"data == {data}")

        data = ET.fromstring(data)

        if update == 1:
            id_element = data.find('id')
            id_element.text = new_id

        username_element = data.find('username')
        password_element = data.find('password')


        username_element.text = new_name
        password_element.text = new_pass

        data = ET.tostring(data)

        response3 = requests.post(jenkins_url_updatefunction, auth=(self.auth_username, self.auth_token), headers=Headers,
                                  data=data)
        if response3.status_code == 200:
            print("Updated successfully!!")

    def manage_ssh_with_private_key(self, id, new_id, new_name,new_description,new_key,update):
        # id = input("Enter id : ")
        Headers = {
            'Content-Type': 'application/xml'
        }

        jenkins_url_updatefunction = self.jenkins_url + f'credential/{id}/config.xml'
        response2 = requests.get(jenkins_url_updatefunction, auth=(self.auth_username, self.auth_token), headers=Headers)
        data = response2.text
        print(f"data == {data}")

        data = ET.fromstring(data)

        if update == 1:
            id_element = data.find('id')
            id_element.text = new_id

        username_element = data.find('username')
        description_element = data.find('description')

        username_element.text = new_name
        description_element.text = new_description


        data = ET.tostring(data)

        response3 = requests.post(jenkins_url_updatefunction, auth=(self.auth_username, self.auth_token), headers=Headers,
                                  data=data)
        if response3.status_code == 200:
            print("Updated successfully!!")

    def delete(self, id):
        Headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        jenkins_url_deletefunction = self.jenkins_url + f'credential/{id}/doDelete'
        response3 = requests.post(jenkins_url_deletefunction, auth=(self.auth_username, self.auth_token), headers=Headers)
        return ' Credentials Deleted '

    def get_credentials(self):

        url = self.jenkins_url + 'api/json?tree=credentials[id,description,typeName]'
        response = requests.get(url)
        return response

# url = 'http://44.212.71.109:8080/manage/credentials/store/system/domain/_/'
#
# with open('config.xml', 'r') as file:
#     xml_data = file.read()
#
# obj1 = credentials(url, 'admin', '1187c4bb500c1cf2595c14fde4f06e0668')
# obj1.create('ppppp', 'bbbbbbbbbb', 'ccccccc')
