import requests
import datetime as dt

# TODO 1: Create a user;
pixela_Endpoint = 'https://pixe.la/v1/users'
TOKEN = 'q1a2w3s4e4d5r6f6t7g7y8h8u9j9k9i0'
USERNAME = 'jrashmi1'

pixela_configs = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}

# create_user = requests.post(url=pixela_Endpoint,json=pixela_configs)
# print(create_user.json(),'\n',create_user.text)

# TODO 2: Create a graph

graph_Endpoint = f"{pixela_Endpoint}/{USERNAME}/graphs"

requests_header = {
    'X-USER-TOKEN':TOKEN
}

graph_id = 'graph1'
graph_configs = {
    'id':graph_id,
    'name':'python learning tracker',
    'unit':'hours',
    'type':'float',
    'color':'shibafu',
    'timezone':'Asia/Kolkata'
}

# create_graph = requests.post(url=graph_Endpoint,json=graph_configs,headers=requests_header)
# # print(create_graph.json())
# print(create_graph.text)
#{"message":"Success.","isSuccess":true}

# TODO 3: Get the graph:
# https://pixe.la/v1/users/jrashmi1/graphs/graph1.html

# TODO 4: Post value to the graph
today = dt.datetime.today().strftime('%Y%m%d')
post_a_pixel_config ={
    'date':today,
    'quantity':'2.5',
}

# post_a_pixel = requests.post(url=f"{graph_Endpoint}/{graph_id}",json=post_a_pixel_config,headers=requests_header)
# print(post_a_pixel.json(),'\n',post_a_pixel.text)

# TODO 5: Delete a pixel
# delete_a_pixel = requests.delete(f"{graph_Endpoint}/{graph_id}/20250426",headers=requests_header)
# print(delete_a_pixel.json(),delete_a_pixel.text)

update_pixel_configs = {
    'quantity':'5.5'
}
# TODO 6: Update a pixel
update_a_pixel = requests.put(url=f"{graph_Endpoint}/{graph_id}/{today}",json=update_pixel_configs,headers=requests_header)
print(update_a_pixel.json(),update_a_pixel.text)