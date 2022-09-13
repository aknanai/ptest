import requests
target_url=""
data_dict={"usename":"admin",
           "password":"blabla"}

response= requests.post(target_url,data=data_dict)
response2=requests.get()
print(response.content)