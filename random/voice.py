from gtts import gTTS
import os

# The text you want to convert to speech
text = 'Eurekaion'

# Set up gTTS object
tts = gTTS(text=text, lang='en', slow=False)

# Save the converted audio to a file
audio_file = "eurekaion.mp3"
tts.save(audio_file)

print(f"The audio file was successfully created: {audio_file}")

# Play the audio file, uncomment the line below if you're on Windows
# os.system(f'start {audio_file}')

# For macOS, uncomment the line below
# os.system(f'afplay {audio_file}')

# For Linux, uncomment the line below
# os.system(f'mpg321 {audio_file}')
