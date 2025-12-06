#!/usr/bin/python3
"""This is my doc"""


import requests
import csv


def fetch_and_print_posts():
    fetch = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {fetch.status_code}')
    if fetch.status_code == 200:
        fetchedjson = fetch.json()
        for i in fetchedjson:
            print(i['title'])


def fetch_and_save_posts():
    fetch = requests.get('https://jsonplaceholder.typicode.com/posts')
    if fetch.status_code == 200:
        fetchedjson = fetch.json()
        filteredjson = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in fetchedjson
        ]
        with open('posts.csv', 'w', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(filteredjson)
