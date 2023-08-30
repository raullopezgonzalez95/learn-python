from pygame import mixer
from gtts import gTTS

def main():
   tts = gTTS('hello')
   tts.save('output.mp3')
   mixer.init()
   mixer.music.load('output.mp3')
   mixer.music.play()
   
if __name__ == "__main__":
   main()