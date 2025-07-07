# 🎤 Speech-to-Text Transcription Web App

This is a simple Python Flask web application that converts uploaded `.wav` audio files into text using the Google Speech Recognition API.

Designed as a beginner-friendly internship project, it focuses on basic file upload and transcription — all handled in a clean and minimal interface.

## 📌 Project Features

- Upload a `.wav` audio file
- Transcribes speech to text using Google API
- Clean and simple UI with inline HTML
- Fully beginner-friendly code (one file)
- Easy to understand and run

📁 Files in This Repository
File	 -  Description
app.py - 	Main Python Flask application
sample.wav -	Test audio file for transcription

🌐 Transcribe in Hindi, Gujarati, or Any Language
By default, this app uses English (en-US).

To transcribe in other languages, just change this line in app.py
text = r.recognize_google(audio)

To One Of These : Simple example for you to make it easy 

text = r.recognize_google(audio, language='hi-IN')  # Hindi
text = r.recognize_google(audio, language='gu-IN')  # Gujarati
text = r.recognize_google(audio, language='mr-IN')  # Marathi
text = r.recognize_google(audio, language='ta-IN')  # Tamil
text = r.recognize_google(audio, language='bn-IN')  # Bengali


Thank You Mini Simple Project by Umang Ghoghari from C.K Pithawala College Surat 

OUTPUT :

SCREEN SHOT 1 :
<img width="1910" height="429" alt="Image" src="https://github.com/user-attachments/assets/e7dc78f3-6b9a-433b-b59c-87bfa79dc26f" />


SCREEN SHOT 2 FINAL OP: UMANG GHOGHARI
<img width="1918" height="529" alt="Image" src="https://github.com/user-attachments/assets/c0c30755-d3e9-4e9b-9f1f-f77e46a70589" />








