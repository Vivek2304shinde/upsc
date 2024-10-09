from gtts import gTTS

def generate_audio_summary(text, filename="output.mp3"):
    """Generates an audio summary of the given text"""
    tts = gTTS(text)
    tts.save(filename)
    print(f"Audio summary saved as {filename}")
