import requests

url = 'http://ug-project-sid.herokuapp.com/data/add'
myobj = {"Cordinate":"200:200"}

x = requests.post(url, data = myobj)

print(x.text)
