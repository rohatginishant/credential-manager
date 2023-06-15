import requests
import xml.etree.ElementTree as ET


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

        Headers = {
            'Content-Type': 'application/xml',
            'Jenkins_Crumb': crumb
        }


        data = f'''
        <com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
        <scope>GLOBAL</scope>
        <id>{id}</id>
        <username>{username}</username>
        <password>{password}</password>
        </com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
    
        '''
        response = requests.post(jenkins_url_createfunction, auth=(self.auth_username, self.auth_token),
                                 headers=Headers,
                                 data=data)

        if response.status_code == 200:
            print("Credentials created ")
            return "hello , you have created username-password successfully !!! "

    def create_ssh_with_private_key(self, id, description,username, privatekey,usernameSecret, crumb_url):
        jenkins_url_createfunction = self.jenkins_url + 'createCredentials'
        jenkins_crumb = requests.get(crumb_url)
        crumb = jenkins_crumb.json()["crumb"]

        Headers = {
            'Content-Type': 'application/xml',
            'Jenkins_Crumb': crumb
        }


        data = f'''
        <com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey plugin="ssh-credentials@305.v8f4381501156">
        <scope>GLOBAL</scope>
        <id>{id}</id>
        <description>{description}</description>
        <username>{username}</username>
        <usernameSecret>{usernameSecret}</usernameSecret>
        <privateKeySource class="com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource">
        <privateKey>
           {privatekey}
        </privateKey>
        </privateKeySource>
        </com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey>

        '''
        response = requests.post(jenkins_url_createfunction, auth=(self.auth_username, self.auth_token),
                                     headers=Headers,
                                     data=data)

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
