import digitalocean
import os
import ipaddress
import time
import sys
from builtins import input

def check_ip(ip):
    for i in range(136, 139):
        if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(f"137.184.{i}.0/24"):
            return True
    return False

def create_droplet(name, project_name):
    droplet = digitalocean.Droplet(token="dop_v1_b168c5df06f62f2f2c58fbb23118cd0b9804af54cd6d54f121c3a06dba7a035d",
                                   name=name,
                                   region="nyc1",
                                   image="ubuntu-18-04-x64",
                                   size_slug="s-1vcpu-1gb",
                                   project=project_name)  # Add project parameter
    droplet.create()
    return droplet

def get_droplet_ip(droplet):
    while True:
        actions = droplet.get_actions()
        for action in actions:
            action.load()
            if action.status == "completed":
                droplet.load()
                return droplet.ip_address
        print(f"Waiting for droplet {droplet.name} to become active...")
        time.sleep(10)
    return None

def create_droplets():
    project_name = input("Enter the project name: ")
    droplets = []
    for i in range(1, 9):
        droplet = create_droplet(f"droplet-{i}", project_name)
        droplets.append(droplet)
    return droplets

def delete_droplets(droplets):
    for droplet in droplets:
        print(f"Deleting droplet: {droplet.name}")
        droplet.destroy()

def main():
    while True:
        droplets = create_droplets()
        for droplet in droplets:
            ip = get_droplet_ip(droplet)
            print(f"Droplet: {droplet.name}, IP: {ip}")
            if ip and check_ip(ip):
                with open("live.txt", "w") as f:
                    f.write(ip)
                print("Found valid IP:", ip)
                sys.exit(0)
        delete_droplets(droplets)

if __name__ == "__main__":
    main()
