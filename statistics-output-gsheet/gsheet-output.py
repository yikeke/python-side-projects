#coding:utf-8

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from datetime import datetime
import requests

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# authenticate
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/coco/Documents/GitHub/coco-python-script/issue-tracker-4cf725edfecc.json', scope)
gc = gspread.authorize(credentials)

# open the google spreadsheet and select the first sheet
sh = gc.open('Pull Request/Issue Status Track 2019')
# worksheet = sh.get_worksheet(0)
contributor_sheet = sh.worksheet("docs-cn/all-contributor-commits")

json_file = '/Users/coco/Documents/GitHub/python-side-projects/statistics-output-gsheet/example-statistics.json'

with open(json_file) as f:
    contributor_statistics = json.load(f)
    # print(len(contributor_statistics)) result: 100 个 contributor
    # print(len(contributor_statistics[0]["weeks"]))  # Python dictionary: 211 weeks (Jul 24, 2016 – Aug 5, 2020)
    # print(str(contributor_statistics[0]["weeks"][0]["w"]))  # String: the "w" unix timestamp

# get values of the first row
first_row_values = contributor_sheet.row_values(1)
row_empty_true = len(first_row_values)
print("the first row has " + str(row_empty_true) + " values.")
total_weeks = len(contributor_statistics[0]["weeks"])

# If the first row of the gsheet is empty, initiate the row
if row_empty_true == 0:
    first_row_values = ['Github ID', 'Contributor Type', 'Avatar URL']
    for i in range(0, total_weeks):
        week_unix_timestamp = int(contributor_statistics[0]["weeks"][i]['w'])
        week = datetime.utcfromtimestamp(week_unix_timestamp).strftime('%Y-%m-%d')
        first_row_values.append(week)
    # for i in range(1, total_weeks+4):
    #     contributor_sheet.update_cell(1, i, first_row_values[i-1]) 这种方法不如 append_row 好，row 有长度限制
    contributor_sheet.append_row(first_row_values)

# insert rows of contributor statistics

# for i in range(99,-1,-1):
#     print(i) # will print 99-0

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

    contributor_sheet.append_row(contributor_values)
