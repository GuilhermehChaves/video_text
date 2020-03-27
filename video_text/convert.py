def mp4_to_wav(file_path ,input_directory ,output_directory ,name):
  from moviepy.editor import VideoFileClip
  import os

  if(not os.path.exists(output_directory)):
    os.mkdir(output_directory)

  file = VideoFileClip(os.path.join(file_path))
  times = int((file.duration) / 30)
  is_multiple_of_thirty = isinstance((file.duration / 30), int)

  for i in range(times):
    path = input_directory + name + '-' + str(i) + '.mp4'
    output_path = output_directory + name + '-' + str(i) + '.wav'

    video = VideoFileClip(os.path.join(path))
    video.audio.write_audiofile(os.path.join(output_path))
    video.close()
  
  if (not is_multiple_of_thirty):
    path = input_directory + name + '-' + str(times) + '.mp4'
    output_path = output_directory + name + '-' + str(times) + '.wav'
    video = VideoFileClip(os.path.join(path))
    video.audio.write_audiofile(os.path.join(output_path))
    video.close()
