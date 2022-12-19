# Punjabi-AI
A Python program to create a GUI that takes a user's question in English, uses OpenAI's completion API to generate an answer, translates it to Punjabi, and reads it aloud.

### Language: 

- Python

### Flow diagrams:

### Requirements:

- [OPENAI API key](https://beta.openai.com/account/api-keys)
-[Narakeet API key

### Libraries:

- googletrans
- openai
- PyQt5
- pyaudio
- requests
- sys
- time
- vlc
- wave

### API:

- [narakeet-api](https://www.narakeet.com/docs/automating/)
- [openai-api](https://openai.com/api/)


### Functions:

1. def read_out_loud()
2. def record()
3. def erase()
4. def submit()

### Procedures:

1.  Create a GUI with a text field to enter a question, a submit button, a record button, and a read aloud button.
2.  Connect the record button to a function to record a wave file with PyAudio.
3.  Connect the submit button to a function to send the question to OpenAI's completion API, generate an answer, and translate it to Punjabi.
4.  Connect the read-aloud button to a function to use the NaraKeet API to create an audio file of the translated Punjabi answer.
5.  Output the answer to the GUI and play the audio file.

### Resource:

1. YouTube:

[https://www.youtube.com/watch?v=8QGqT3cJ4ps](https://www.youtube.com/watch?v=8QGqT3cJ4ps)


2. GitHub

[https://github.com/narakeet/text-to-speech-api-python-example/blob/main/tts.py](https://github.com/narakeet/text-to-speech-api-python-example/blob/main/tts.py)

3. GeeksForGeeks

[https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/](https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/)

### Additional notes:

Note: Change lines 19 and 145 of qt-punjabi-ai.py to the proper OPENAI API key and Narakeet API key respectively.
