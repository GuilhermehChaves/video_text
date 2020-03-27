from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

def separate(input_path:str, output_directory:str, name:str):
  if(not os.path.exists(output_directory)):
    os.mkdir(output_directory)

  video = VideoFileClip(input_path)
  times = int((video.duration) / 30)
  init_time = 0
  final_time = 30

  is_multiple_of_thirty = isinstance((video.duration / 30), int)

  for i in range(times):
    ffmpeg_extract_subclip(input_path, init_time, final_time, targetname=output_directory +name+"-"+str(i)+".mp4")
    init_time += 30
    final_time += 30
    video.close()

  if (not is_multiple_of_thirty):
    video = VideoFileClip(input_path)
    rest = int(video.duration - (times * 30))
    init_rest_time = times * 30
    final_rest_time = init_rest_time + rest

    ffmpeg_extract_subclip(input_path, init_rest_time, final_rest_time, targetname=output_directory+name+"-"+str(times)+".mp4")
    video.close()

def save_text(name, content):
  archive = open(name, 'w', encoding="utf8")
  archive.writelines(content)
  archive.close()
