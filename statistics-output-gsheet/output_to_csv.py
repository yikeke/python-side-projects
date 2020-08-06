#coding:utf-8

import json
from datetime import datetime
import requests
import csv
import os
import sys
# from parse_json import earlist_repo_file

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

json_file = '/Users/coco/Documents/GitHub/python-side-projects/statistics-output-gsheet/merged_json_file.json'

with open(json_file) as f:
    contributor_statistics = json.load(f)
    # print(len(contributor_statistics)) result: 100 个 contributor
    # print(len(contributor_statistics[0]["weeks"]))  # Python dictionary: 211 weeks (Jul 24, 2016 – Aug 5, 2020)
    # print(str(contributor_statistics[0]["weeks"][0]["w"]))  # String: the "w" unix timestamp
    total_contributor = len(contributor_statistics)

# Initiate the first row of the gsheet
first_row_values = ['Github ID', 'Contributor Type', 'Avatar URL']

# with open(earlist_repo_file) as f:
with open('/Users/coco/Documents/GitHub/python-side-projects/statistics-output-gsheet/json_file_2.json') as f:
    earlist_repo_commits = json.load(f)

total_weeks = len(earlist_repo_commits[0]["weeks"])
weeks = earlist_repo_commits[0]["weeks"]

for i in range(0, total_weeks):
    week_unix_timestamp = int(earlist_repo_commits[0]["weeks"][i]['w'])
    week = datetime.utcfromtimestamp(week_unix_timestamp).strftime('%Y-%m-%d')
    first_row_values.append(week)

# for i in range(99,-1,-1):
#     print(i) # will print 99-0

csv_file_path = dirname + '/docs-contributor-statistics.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(first_row_values)

    # insert rows of contributor statistics
    for n in range(len(contributor_statistics)-1, -1, -1):  # 倒序 143 contributors
        contributor_values = []
        github_id = contributor_statistics[n]["author"]["login"]
        contributor_type = ''
        avatar_url = contributor_statistics[n]["author"]["avatar_url"]
        contributor_values = [github_id, contributor_type, avatar_url]

        commits = 0
        flag = 1
        for week in weeks: # [0,212)
            # print(week["w"])
            for week_dict in contributor_statistics[n]["weeks"]: # 211
                # week_dict is a dict
                # print(type(week_dict))
                # print(week_dict["c"]) 
                # for values in week_dict.values():
                #     if week["w"] in values:
                if week_dict["w"] == week["w"]:
                    # print(week_dict["c"])
                    commits += week_dict["c"] # last one:
                    flag = 1
                    contributor_values.append(commits)
                    break
                else:
                    flag = 0
            if flag == 0:
                contributor_values.append(commits)

        writer.writerow(contributor_values)

