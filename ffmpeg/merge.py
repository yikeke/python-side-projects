# coding=utf-8
import os
import glob

path = '/Users/coco/Downloads/video/test'

ffmpeg_dir = input('请输入 ffmpeg 解压后的目录：')



for filename in os.listdir(path):
    if (filename.endswith(".mp4")): #or .avi, .mpeg, whatever.
        os.getcwd(filename)


# for filename in os.listdir(path):
#     if (filename.endswith(".mp4")): #or .avi, .mpeg, whatever.
#         ts_file = filename.strip(".mp4") + '.ts'
#         os.chdir(ffmpeg_dir)
#         os.system("ffmpeg -i {0} -vcodec copy -acodec aac -vbsf h264_mp4toannexb {1}".format(os.path.join(path,filename),os.path.join(path,ts_file)))

# for filename in os.listdir(path):
#     if (filename.endswith(".ts")): #or .avi, .mpeg, whatever.
#         ts.append(os.path.join(path,filename)) # "concat:1.ts|2.ts|3.ts|4.ts"

# command = "concat:" + "|".join(ts)
# print(command)
# os.chdir(ffmpeg_dir)
# # 拼接 ts 并导出最终 mp4 文件
# os.system("ffmpeg -i {0} -acodec aac -vcodec copy -absf aac_adtstoasc -movflags +faststart {1}".format(command,os.path.join(path,'merge.mp4')))
# # 删除过程中生成的 ts 文件
# # os.remove(*.ts)

# size 相加是一致的：ffmpeg -i "concat:test/cut.ts|test/02.ts" -acodec aac -vcodec copy -absf aac_adtstoasc combine.mp4

# ffmpeg -i "'concat:/Users/coco/Downloads/video/test/02-39-200.ts|/Users/coco/Downloads/video/test/02-20-180.ts'" -acodec aac -vcodec copy -absf aac_adtstoasc combine.mp4

# ffmpeg -i "concat:/Users/coco/Downloads/video/test/02-39-200.ts|/Users/coco/Downloads/video/test/02-20-180.ts" -acodec aac -vcodec copy -absf aac_adtstoasc combine.mp4