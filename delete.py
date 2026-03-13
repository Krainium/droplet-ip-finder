import requests
import json


token = 'dop_v1_b168c5df06f62f2f2c58fbb23118cd0b9804af54cd6d54f121c3a06dba7a035d'


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {0}'.format(token),
}


droplet_names = ["droplet-1", "droplet-2", "droplet-3", "droplet-4", "droplet-5", "droplet-6", "droplet-8"]


response = requests.get(
    'https://api.digitalocean.com/v2/droplets', 
    headers=headers
)


if response.status_code != 200:
    print('Error: ', response.json())
    exit(1)

droplets = response.json()['droplets']


named_droplets = [d for d in droplets if d['name'] in droplet_names]


for droplet in named_droplets:
    delete_response = requests.delete(
        'https://api.digitalocean.com/v2/droplets/{0}'.format(droplet['id']),
        headers=headers
    )

    
    if delete_response.status_code == 204:
        print('Successfully deleted droplet id: ', droplet['id'])
    else:
        print('Error deleting droplet id {0}: '.format(droplet['id']), delete_response.json())
