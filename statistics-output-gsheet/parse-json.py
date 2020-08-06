import os
import sys
import json
import requests

# json模块常用的四个函数
# 1 import json
# 2 json.load() # 将一个存储在文件中的json对象（str）转化为相对应的python对象
# 3 json.loads() # 将一个json对象（str）转化为相对应的python对象
# 4 json.dump() # 将python的对象转化为对应的json对象（str),并存放在文件中
# 5 json.dumps() # 将python的对象转化为对应的json对象（str)

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

def request_json_files(requested_url): # requested_url is a dict
    json_files_num = len(requested_url)
    json_file_list = []
    for i in range(0, json_files_num):
        request = requests.get(requested_url[i]) # 'https://api.github.com/repos/pingcap/docs-cn/stats/contributors'
        python_data = json.loads(request.text)  # python_data is a python list
        new_json_filepath = dirname + '/json_file_' + str(i) + '.json'
        new_json_file=open(new_json_filepath,"w")
        json.dump(python_data,new_json_file,indent=4)
        new_json_file.close
        json_file_list.append(new_json_filepath)
    return json_file_list

def merge_json_files(base_file_path, append_file_path):
    # This function is specifically for merging the json files from 'https://api.github.com/repos/org-name/repo-name/stats/contributors' requests.
    # The two json files must have the same keys "total", "weeks", "author".
    with open(append_file_path, 'r') as append_file:
        append_file_content = json.load(append_file)
        append_file_len = len(append_file_content)
    with open(base_file_path, 'r') as base_file:
        base_file_content = json.load(base_file)
        base_file_len = len(base_file_content)
    for i in range(0, append_file_len): # Start reading through append_file's key
        for j in range(0, base_file_len):
            # if the author from append_file = the author from base_file
            if append_file_content[i]["author"]["login"] == base_file_content[j]["author"]["login"]:
                # reset "total"
                base_file_content[j]["total"] = int(base_file_content[j]["total"]) + int(append_file_content[i]["total"])
                # reset "weeks"
                base_weeks = len(base_file_content[j]["weeks"])
                append_weeks = len(append_file_content[i]["weeks"])
                #print(append_weeks)
                for m in range(0, base_weeks): # [0,221)
                    for n in range(0, append_weeks):
                        # if the week from append_file = the week from base_file
                        if append_file_content[i]["weeks"][n]["w"] == base_file_content[j]["weeks"][m]["w"]:
                            base_file_content[j]["weeks"][m]["a"] = int(base_file_content[j]["weeks"][m]["a"]) + int(append_file_content[i]["weeks"][n]["a"])
                            base_file_content[j]["weeks"][m]["d"] = int(base_file_content[j]["weeks"][m]["d"]) + int(append_file_content[i]["weeks"][n]["d"])
                            base_file_content[j]["weeks"][m]["c"] = int(base_file_content[j]["weeks"][m]["c"]) + int(append_file_content[i]["weeks"][n]["c"])

    # Write the merging changes to the base file
    try:
        # print(base_file_path)
        with open(base_file_path, 'w') as f:
            json.dump(base_file_content, f, indent=4)
            #print(json.dumps(base_file_content))
    except Exception as e:
        print(Exception,":",e)
        print("failed to output!")

    # os.remove(append_file_path)

if __name__ == '__main__':
    # Generate several json files according to the requests
    requested_url = ['https://api.github.com/repos/pingcap/docs-cn/stats/contributors', 'https://api.github.com/repos/pingcap/docs/stats/contributors', 'https://api.github.com/repos/pingcap/docs-dm/stats/contributors', 'https://api.github.com/repos/pingcap/docs-tidb-operator/stats/contributors']
    json_file_list = request_json_files(requested_url)
    # print(json_file_list)

    # Create the final version of json file to be merged in
    base_file_path = dirname + '/merged_json_file.json'
    with open(base_file_path, 'w') as f1:
        with open(dirname + '/json_file_1.json', 'r') as f2:
            copy_content = json.load(f2)
            json.dump(copy_content, f1)

    # Check the number of json files and merge them to base_file_path
    for n in range(1,len(json_file_list)): # n = [1, 4)
        append_file_path = json_file_list[n]
        merge_json_files(base_file_path, append_file_path)





################# Deprecated code
# def request_json_files(requested_url): # requested_url is a dict
#     json_files_num = len(requested_url)
#     cwd = os.getcwd()
#     for i in range(0, json_files_num):
#         if i == 0:
#             request = requests.get(requested_url[i]) # 'https://api.github.com/repos/pingcap/docs-cn/stats/contributors'
#             python_data = json.loads(request.text)
#             base_file_path = cwd + '/json_file.json'
#             base_file=open(base_file_path,"w")
#             json.dump(python_data,base_file,indent=4) # dump 成 json 格式的数据并格式化写入文件
#             base_file.close
#         else:
#             request = requests.get(requested_url[i]) # 'https://api.github.com/repos/pingcap/docs-cn/stats/contributors'
#             python_data = json.loads(request.text)
#             append_file_path = cwd + '/json_file_2.json'
#             append_file=open(append_file_path,"w")
#             json.dump(python_data,append_file,indent=4)
#             append_file.close
#             #merge_json_files(base_file_path, append_file_path)
#             merge_json_files('/Users/coco/Documents/GitHub/python-side-projects/json_file.json', '/Users/coco/Documents/GitHub/python-side-projects/json_file_2.json')
#     return type(base_file_path)

# def merge_json_files(base_file_path, append_file_path):
#     # This function is specifically for merging the json files from 'https://api.github.com/repos/org-name/repo-name/stats/contributors' requests.
#     # The two json files must have the same keys "total", "weeks", "author".
#     with open(base_file_path) as base_file:
#         base_file_content = json.load(base_file)
#         base_file_len = len(base_file_content)
#     with open(append_file_path) as append_file:
#         append_file_content = json.load(append_file)
#         append_file_len = len(append_file_content)
#     for i in range(0, append_file_len): # 开始遍历 append_file 的 key
#         for j in range(0, base_file_len):
#             # if the author from append_file = the author from base_file
#             if append_file_content[i]["author"]["login"] == base_file_content[j]["author"]["login"]:
#                 # reset "total"
#                 base_file_content[j]["total"] = int(base_file_content[j]["total"]) + int(append_file_content[i]["total"])
#                 # reset "weeks"
#                 base_weeks = len(base_file_content[j]["weeks"])
#                 append_weeks = len(append_file_content[i]["weeks"])
#                 for m in range(0, base_weeks): # [0,221)
#                     for n in range(0, append_weeks):
#                         # if the week from append_file = the week from base_file
#                         if append_file_content[i]["weeks"][n]["w"] == base_file_content[j]["weeks"][m]["w"]:
#                             base_file_content[i]["weeks"][m]["a"] = int(base_file_content[i]["weeks"][m]["a"]) + int(append_file_content[j]["weeks"][n]["a"])
#                             base_file_content[i]["weeks"][m]["d"] = int(base_file_content[i]["weeks"][m]["d"]) + int(append_file_content[j]["weeks"][n]["d"])
#                             base_file_content[i]["weeks"][m]["c"] = int(base_file_content[i]["weeks"][m]["c"]) + int(append_file_content[j]["weeks"][n]["c"])

#     # Write the merging changes to the base file
#     with open(base_file_path, 'r+') as f:
#         f.seek(0)        # <--- should reset file position to the beginning.
#         json.dump(base_file_content, f, indent=4)
#         f.truncate()     # remove remaining part

#     os.remove(append_file_path)

#     return append_weeks, base_weeks
