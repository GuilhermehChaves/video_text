def extract_text(video_path, audio_directory, name):
  import speech_recognition as sr
  from moviepy.editor import VideoFileClip

  video = VideoFileClip(video_path)
  times = int((video.duration) / 30)
  is_multiple_of_thirty = isinstance((video.duration / 30), int)

  recognizer = sr.Recognizer()

  result = ''

  for i in range(times):
    audio_path = audio_directory + name + '-' + str(i) + '.wav'
    file = sr.AudioFile(audio_path)
    with file as source:
      audio = recognizer.record(source)

    phrase = recognizer.recognize_google(audio, language = 'pt-BR')
    result += ' ' + phrase + ' \n'
    print('Recognizing...', i)

  if (not is_multiple_of_thirty):
    try:
      audio_path = audio_directory + name + '-' + str(times) + '.wav'
      file = sr.AudioFile(audio_path)
      with file as source:
        audio = recognizer.record(source)

      phrase = recognizer.recognize_google(audio, language = 'pt-BR')
      result += ' ' + phrase + ' \n'
      print('Recognizing...', times)

    except:
      print('Cannot understand this...')

  return result