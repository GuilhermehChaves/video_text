from setuptools import setup
import video_text

setup(
  name = "video_text",
  version = video_text.__version__,
  packages = ["video_text"],
  include_package_data= True,
  install_requires=["SpeechRecognition>=3.8.1", "moviepy >=1.0.1"],

  author = video_text.__author__,
  author_email = "contato.guilhermehchaves@gmail.com",
  url = "https://github.com/GuilhermehChaves/video_text"
)
