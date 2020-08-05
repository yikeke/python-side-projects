import os
import json
import requests

def request_json_files(requested_url): # requests is a dict
    json_files_num = len(requested_url)
    for i in range(0, json_files_num):
        request = requests.get(requested_url[i]) # 'https://api.github.com/repos/pingcap/docs-cn/stats/contributors'
        python_data = json.loads(request.text)
        if i == 0:
            cwd = os.getcwd()
            file_path = cwd + '/json_file_1.json'
            base_file=open(file_path,"w")
            json.dump(python_data,base_file,indent=4) # dump 成 json 格式的数据并格式化写入文件
        else:
            merge_json_files()
    return file_path

def merge_json_files():


if __name__ == '__main__':
    requested_url = ['https://api.github.com/repos/pingcap/docs-cn/stats/contributors', 'https://api.github.com/repos/pingcap/docs/stats/contributors', 'https://api.github.com/repos/pingcap/docs-dm/stats/contributors', 'https://api.github.com/repos/pingcap/docs-tidb-operator/stats/contributors']
    print(request_json_files(requested_url))