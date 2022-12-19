import sys
import openai
import googletrans
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyaudio
import time
import wave


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "input.wav"

# OpenAI API Keys
openai.api_key = "YOUR_OPENAI_API_KEY"

# Create GUI
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('ਪੰਜਾਬੀ ਏ.ਆਈ.')
window.setGeometry(400, 300, 400, 300)

# Record button
def record():
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")

    max = int(RATE / CHUNK * RECORD_SECONDS)
    # Maximum should be equivalent to max
    progress.setMaximum(max)
    progress.setMinimum(0)
    progress.setValue(0)
    frames = []

    for i in range(0, max):
        progress.setValue(i+1)
        data = stream.read(CHUNK)
        frames.append(data)
        # print(int(i))
    print("finished recording")


    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


btn = QPushButton(window)
btn.setText('ਰਿਕਾਰਡ')
btn.clicked.connect(record)
btn.move(10, 15)

progress = QProgressBar(window)
progress.setGeometry(10, 40, 380, 25)

# Input field
label = QLabel(window)
label.setText("ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਆਪਣਾ ਸਵਾਲ ਦਰਜ ਕਰੋ:")
label.move(10, 75)
serifFont = QFont("Times", 20)
question = QLineEdit(window, font=serifFont)
question.setFixedWidth(1000)
question.move(10, 90)

# Erase button
def erase():
    question.setText('')
    question.setFocus()

btn_erase = QPushButton(window)
btn_erase.setText('🗑')
btn_erase.clicked.connect(erase)
btn_erase.move(935, 90)

# Submit button
def submit():
    # Get user input question
    q = question.text()

    # Send to OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=q + "Explain like I'm 5 and be honest, truthful and elaborate. Also end at punctuation marks. Use simple vocabulary.",
        max_tokens=1000,
        temperature=0.7,
        frequency_penalty=0.2,
        top_p=0.9
    )

    # Get answer
    answer_text = response['choices'][0]['text']
    print(answer_text)

    # Translate answer to Punjabi
    translator = googletrans.Translator()
    translated_answer = translator.translate(answer_text, dest='pa')

    # Output answer to gui
    answer.setText(translated_answer.text)



btn = QPushButton(window)
btn.setText('ਜਮ੍ਹਾਂ ਕਰੋ')
btn.move(10, 130)
btn.clicked.connect(submit)

# Output field
answer_label = QLabel(window)
answer_label.setText("ਪੰਜਾਬੀ ਵਿੱਚ ਜਵਾਬ:")
answer_label.move(10, 165)
serifFont = QFont("Times", 20)
answer = QTextEdit(window, width=80, font=serifFont)
answer.setFixedWidth(1000)
answer.setFixedHeight(400)
answer.move(10, 400)
answer.setGeometry(10, 180, 300, 160)

import requests
import vlc

# Define function to read out loud
def read_out_loud():
    # Get text from answer widget
    text = answer.toPlainText()


    apikey = 'YOUR_NARAKEET_API_KEY'
    voice = 'Navneet'
    text = text
    url = f'https://api.narakeet.com/text-to-speech/m4a?voice={voice}'

    options = {
        'headers': {
            'Accept': 'application/octet-stream',
            'Content-Type': 'text/plain',
            'x-api-key': apikey,
        },
        'data': text.encode('utf8')
    }

    with open('output.mp3', 'wb') as f:
        f.write(requests.post(url, **options).content)

    # Create vlc media player object
    audio = vlc.MediaPlayer("output.mp3")

    # Start playing audio
    audio.play()


# Add a button to read out the answer
btn_speak = QPushButton(window)
btn_speak.setText('🔊 ਪੰਜਾਬੀ ਵਿੱਚ ਸੁਣੋ')
btn_speak.move(10, 557)
# Connect button to function
btn_speak.clicked.connect(read_out_loud)


# Show window
window.showMaximized()
sys.exit(app.exec_())