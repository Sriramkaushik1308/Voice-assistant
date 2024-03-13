import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use microphone as source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust the recognizer sensitivity for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Use Google Speech Recognition to convert audio to text
        text = recognizer.recognize_google(audio)

        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None

if __name__ == "__main__":
    text = speech_to_text()
    if text:
        # Do something with the recognized text
        pass
