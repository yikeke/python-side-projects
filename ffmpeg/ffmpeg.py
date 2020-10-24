# coding=utf-8
import os

# video dir
path = '/Users/coco/Downloads/video/test'
# 在 video dir 里新建个 video-clips 文件夹，存放剪切出的视频
os.mkdir(os.path.join(path,'video-clips'))

ffmpeg_dir = input('请输入 ffmpeg 解压后的目录：')

for filename in os.listdir(path):
    if (filename.endswith(".mp4")): #or .avi, .mpeg, whatever.
        print("Parsing " + filename + "...")
        input_file = os.path.join(path,filename)
        start_time = input('请输入剪切起始时间：')
        stop_time = input('请输入剪切结束时间：')
        output_file = filename.strip(".mp4") + '-' + start_time + '-' + stop_time + ".mp4"
        os.chdir(ffmpeg_dir)
        os.system("ffmpeg -ss {2} -to {3} -accurate_seek -i {0} -c copy -avoid_negative_ts 1 {1}".format(input_file,output_file,start_time,stop_time))
    else:
        continue

ask = input('你是否想合并刚刚剪切出的所有视频？y or n')
if ask == 'y':
    print()


# # FFmpeg提取与合并命令使用小结 | Shaun's Space https://cniter.github.io/posts/6315717b.html
# # （1）快速提取video.mp4从第一分钟开始持续两分钟的视频，即到第三分钟，并将提取结果输出为cut.mp4
# ffmpeg -ss 00:01:00 -i video.mp4 -to 00:02:00 -c copy cut.mp4
# # （2）快速提取video.mp4从第一分钟开始持续两分钟的视频，即到第三分钟，并将提取结果输出为cut.mp4
# ffmpeg -ss 00:01:00 -i video.mp4 -t 00:02:00 -c copy cut.mp4
# # （3）快速提取video.mp4从第一分钟开始到第二分钟的视频，并将提取结果输出为cut.mp4
# ffmpeg -ss 00:01:00 -i video.mp4 -to 00:02:00 -c copy -copyts cut.mp4
# # （4）精确提取video.mp4从第一分钟开始到第二分钟的视频，并将提取结果输出为cut.mp4
# ffmpeg -i video.mp4 -ss 00:01:00 -to 00:02:00 -c copy cut.mp4
# # （5）精确提取video.mp4从第一分钟开始持续两分钟的视频，即到第三分钟，并将提取结果输出为cut.mp4
# ffmpeg -i video.mp4 -ss 00:01:00 -t 00:02:00 -acodec copy -vcodec copy cut.mp4
# # （6）快速提取video.mp4从第三分钟开始持续60秒的视频，即到第四分钟，并将提取结果输出为cut.mp4
# ffmpeg -ss 00:03:00 -i '/Users/coco/Documents/GitHub/personal-website/一只上进的懒猪/video-clips/02.mp4' -t 60 -c copy -avoid_negative_ts 1 cut.mp4