from classes import Credentials
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import json
import requests


response = requests.get('http://44.212.71.109:8080/manage/credentials/store/system/domain/_/api/json?tree=credentials[id,description]')
for i in response.json()["credentials"]:
    print(i["id"])

