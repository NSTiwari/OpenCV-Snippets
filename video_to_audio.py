import speech_recognition as sr 
import moviepy.editor as mp

clip = mp.VideoFileClip(r"video.mp4") 
 
clip.audio.write_audiofile(r"audio.wav")
r = sr.Recognizer()

audio = sr.AudioFile("audio.wav")

with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file) 
