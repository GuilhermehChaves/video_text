from video_text import convert, recognize, video, remove_files

__version__ = '0.0.1'
__author__ = 'Guilherme Chaves'

def run(complete_video_path, separated_video_directory, audio_directory, name):
  video.separate(complete_video_path, separated_video_directory, name)
  convert.mp4_to_wav(complete_video_path, separated_video_directory, audio_directory, name)
  result = recognize.extract_text(complete_video_path, audio_directory, name )
  video.save_text(name + '.txt', result)

  remove_files.rm(separated_video_directory)
  remove_files.rm(audio_directory)
