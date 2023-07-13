### prerequisite
## pip install praw

import praw
import requests
import os
import hashlib
import shutil

#Reddit info of user 
reddit = praw.Reddit(client_id='Id Client', client_secret='Secret pass Client', username='Username', password='Password user', user_agent='User agent')

#user name redditor
username = input("Enter username: ")
user = reddit.redditor(username)

# creation folder
if not os.path.exists(username):
    os.makedirs(username)

#Check post user
for submission in user.submissions.new(limit=None):
    if submission.url.endswith(('.jpg', '.jpeg', '.png')):
        # Image recuperation
        response = requests.get(submission.url)
        image_content = response.content

        # check hash file
        hash_object = hashlib.sha256(image_content)
        hex_dig = hash_object.hexdigest()

        # check if file is already exist
        existing_file = False
        for file_name in os.listdir():
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                with open(file_name, 'rb') as f:
                    existing_file_content = f.read()
                existing_file_hash = hashlib.sha256(existing_file_content).hexdigest()
                if existing_file_hash == hex_dig:
                    existing_file = True
                    break

        if existing_file:
            print(f"A  duplicate file with the same hash{hex_dig} already exist, skip the download...")
            continue

        print(f"Download image {hex_dig}...")

        # Write image
        file_path = os.path.join(username, f'{hex_dig}.jpg')
        with open(file_path, 'wb') as f:
            f.write(image_content)