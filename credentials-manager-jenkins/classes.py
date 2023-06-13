import requests
import xml.etree.ElementTree as ET


class Credentials:

    def __init__(self, jenkins_url, auth_username, auth_token):
        self.jenkins_url = jenkins_url
        self.auth_username = auth_username
        self.auth_token = auth_token

    def create(self, id, username, password, crumb_url):
        jenkins_url_createfunction = self.jenkins_url + 'createCredentials'
        # crumb_url = 'http://44.212.71.109:8080//crumbIssuer/api/json'
        jenkins_crumb = requests.get(crumb_url)
        crumb = jenkins_crumb.json()["crumb"]
        # print(f"Jenkins crumb data = {jenkins_crumb.json()}")

        data = f'''
        <com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
        <scope>GLOBAL</scope>
        <id>{id}</id>
        <username>{username}</username>
        <password>{password}</password>
        </com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>

        '''

        Headers = {
            'Content-Type': 'application/xml',
            'Jenkins_Crumb': crumb
        }
        response = requests.post(jenkins_url_createfunction, auth=(self.auth_username, self.auth_token), headers=Headers,
                                 data=data)
        if response.status_code == 200:
            print("Credentials created ")
            return "hello , you have created successfully !!! "

    def manage(self, id, new_id, new_name, new_pass):
        # id = input("Enter id : ")
        Headers = {
            'Content-Type': 'application/xml'
        }

        jenkins_url_updatefunction = self.jenkins_url + f'credential/{id}/config.xml'
        response2 = requests.get(jenkins_url_updatefunction, auth=(self.auth_username, self.auth_token), headers=Headers)
        data = response2.text
        print(f"data == {data}")

        data = ET.fromstring(data)

        id_element = data.find('id')
        username_element = data.find('username')
        password_element = data.find('password')

        id_element.text = new_id
        username_element.text = new_name
        password_element.text = new_pass
        print(f"{username_element.text},{password_element.text},{id_element.text}")

        data = ET.tostring(data)

        response3 = requests.post(jenkins_url_updatefunction, auth=(self.auth_username, self.auth_token), headers=Headers,
                                  data=data)
        if response3.status_code == 200:
            print("Updated successfully!!")

    def delete(self, id):
        Headers = {
            'Content-Type': 'application/xml'
        }

        jenkins_url_deletefunction = self.jenkins_url + f'credential/{id}/config.xml'
        response3 = requests.delete(jenkins_url_deletefunction, auth=(self.auth_username, self.auth_token), headers=Headers)
        return ' Credentials Deleted '

#
# url = 'http://44.212.71.109:8080/manage/credentials/store/system/domain/_/'
#
# with open('config.xml', 'r') as file:
#     xml_data = file.read()
#
# obj1 = credentials(url, 'admin', '1187c4bb500c1cf2595c14fde4f06e0668')
# obj1.create('ppppp', 'bbbbbbbbbb', 'ccccccc')
