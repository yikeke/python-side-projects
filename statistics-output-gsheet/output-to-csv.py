#coding:utf-8

import json
from datetime import datetime
import requests
import csv
import os
import sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

json_file = '/Users/coco/Documents/GitHub/python-side-projects/statistics-output-gsheet/merged_json_file.json'

with open(json_file) as f:
    contributor_statistics = json.load(f)
    # print(len(contributor_statistics)) result: 100 个 contributor
    # print(len(contributor_statistics[0]["weeks"]))  # Python dictionary: 211 weeks (Jul 24, 2016 – Aug 5, 2020)
    # print(str(contributor_statistics[0]["weeks"][0]["w"]))  # String: the "w" unix timestamp

# Initiate the first row of the gsheet
first_row_values = ['Github ID', 'Contributor Type', 'Avatar URL']
total_weeks = len(contributor_statistics[0]["weeks"])
for i in range(0, total_weeks):
    week_unix_timestamp = int(contributor_statistics[0]["weeks"][i]['w'])
    week = datetime.utcfromtimestamp(week_unix_timestamp).strftime('%Y-%m-%d')
    first_row_values.append(week)

# for i in range(99,-1,-1):
#     print(i) # will print 99-0

csv_file_path = dirname + '/docs-contributor-statistics.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(first_row_values)

    # insert rows of contributor statistics
    for n in range(len(contributor_statistics)-1, -1, -1):  # 倒序
        contributor_values = []
        github_id = contributor_statistics[n]["author"]["login"]
        contributor_type = ''
        avatar_url = contributor_statistics[n]["author"]["avatar_url"]
        contributor_values = [github_id, contributor_type, avatar_url]

        commits = 0
        for i in range(0, total_weeks): # [0,221)
            commits = commits + contributor_statistics[n]["weeks"][i]["c"]
            contributor_values.append(commits)

        writer.writerow(contributor_values)
