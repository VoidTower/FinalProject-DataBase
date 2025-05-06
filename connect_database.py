# connect_database.py

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
import json

# Get base directory (the current folder)
base_dir = os.path.dirname(os.path.abspath(__file__))

#  Load secrets from the JSON file in the current folder
with open(os.path.join(base_dir, "netflix_project-token.json")) as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

#  Load the secure connect zip from the same folder
cloud_config = {
    'secure_connect_bundle': os.path.join(base_dir, "secure-connect-netflix-project.zip")
}

# Connect to Cassandra
auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

print("Connected to Cassandra!")

__all__ = ['session']