#! /usr/bin/python3
import sqlite3
import requests
import time

# Set up the database
conn = sqlite3.connect('github_stats.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stats
             (datetime TEXT, stars INTEGER, forks INTEGER)''')

# Define the GitHub API endpoint and parameters
endpoint = 'https://api.github.com/repos/Significant-Gravitas/Auto-GPT'
headers = {'Accept': 'application/vnd.github.v3+json'}

# Loop indefinitely
while True:
    # Make a request to the GitHub API
    response = requests.get(endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the number of stars and forks
        data = response.json()
        stars = data['stargazers_count']
        forks = data['forks_count']

        # Record the values in the database
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO stats VALUES (?, ?, ?)", (now, stars, forks))
        conn.commit()

        # Wait ten minutes before making the next request
        time.sleep(600)
    else:
        # If the request was unsuccessful, print an error message and wait for 10 minutes before trying again
        print('Error: {}'.format(response.status_code))
        time.sleep(600)
