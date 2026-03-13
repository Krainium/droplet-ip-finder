import requests
import json

# Set your token here
token = 'dop_v1_b168c5df06f62f2f2c58fbb23118cd0b9804af54cd6d54f121c3a06dba7a035d'

# Set the headers, including the Authorization with your token
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {0}'.format(token),
}

# Names of droplets to be deleted
droplet_names = ["droplet-1", "droplet-2", "droplet-3", "droplet-4", "droplet-5", "droplet-6", "droplet-8"]

# Get all droplets
response = requests.get(
    'https://api.digitalocean.com/v2/droplets', 
    headers=headers
)

# Check the response
if response.status_code != 200:
    print('Error: ', response.json())
    exit(1)

droplets = response.json()['droplets']

# Filter the droplets by the specified names
named_droplets = [d for d in droplets if d['name'] in droplet_names]

# Delete each droplet
for droplet in named_droplets:
    delete_response = requests.delete(
        'https://api.digitalocean.com/v2/droplets/{0}'.format(droplet['id']),
        headers=headers
    )

    # If successful, this will print the droplet ID, otherwise it will print an error
    if delete_response.status_code == 204:
        print('Successfully deleted droplet id: ', droplet['id'])
    else:
        print('Error deleting droplet id {0}: '.format(droplet['id']), delete_response.json())
