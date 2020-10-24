from moviepy.editor import *
# https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#videofileclip

# def one_video(filename):
#     # clip and concatenate one video
#     # waiting on user: please give one clip...
#     clip1 = VideoFileClip("1.mp4").subclip(0,158) #读取视频1.mp4，并截取0-158秒的内容
#     # waiting on user: please give another clip (enter exit to exit)...
#     clip2 = VideoFileClip("1.mp4").subclip(188.209)  # #读取视频1.mp4，并截取188-209秒的内容
#     # waiting on user: please give another clip (enter exit to exit)...
#     final_clip = concatenate_videoclips([clip1,clip2]) #视频合并
#     final_clip.write_videofile("2.mp4")#视频写入2.mp4

# def videos(dirname):
#     for root, dirs, files in os.walk(dirname, topdown=True):
#         for name in files:
#             full_filepath = os.path.join(root, name)
#             print("Parsing " + full_filepath + "...")
#             one_video(full_filepath)

clip1 = VideoFileClip("/Users/coco/Documents/GitHub/personal-website/一只上进的懒猪/video-clips/02.mp4").subclip(0,158) #读取视频1.mp4，并截取0-158秒的内容
clip2 = VideoFileClip("/Users/coco/Documents/GitHub/personal-website/一只上进的懒猪/video-clips/02.mp4").subclip(188.209)  # #读取视频1.mp4，并截取188-209秒的内容
final_clip = concatenate_videoclips([clip1,clip2]) #视频合并
final_clip.write_videofile("2.mp4")#视频写入2.mp4