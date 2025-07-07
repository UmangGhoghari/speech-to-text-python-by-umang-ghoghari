from flask import Flask, request, render_template_string
import speech_recognition as sr

app = Flask(__name__)

html = '''
<h1>🎤 Speech to Text</h1>
<form method="POST" enctype="multipart/form-data">
    <p>Upload WAV File:</p>
    <input type="file" name="audio" required>
    <br><br>
    <button type="submit">Convert</button>
</form>
{% if text %}
    <h2>Text:</h2>
    <p>{{ text }}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    if request.method == 'POST':
        audio_file = request.files['audio']
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
    return render_template_string(html, text=text)

if __name__ == '__main__':
    app.run(debug=True)
