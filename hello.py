import speech_recognition as sr
import pyttsx3
import keyboard      

r = sr.Recognizer()

def record_text():
    while True:
        try:
            if keyboard.is_pressed('esc'):  
                print("ESC key pressed, stopping.")
                return None
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening... (Press ESC to stop)")
                audio = r.listen(source, timeout=5, phrase_time_limit=10)

                if keyboard.is_pressed('esc'):  
                    print("ESC key pressed, stopping.")
                    return None

                MyText = r.recognize_google(audio, language='en-US')
                print(f"Recognized: {MyText}")
                return MyText.lower()

        except sr.WaitTimeoutError:
            print("No speech detected within timeout.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Could not understand the audio.")

        if keyboard.is_pressed('esc'):
            print("ESC key pressed, stopping.")
            return None

def output_text(text):
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        text = record_text()
        if text:
            output_text(text)
            speak_text(text)
            print("Wrote text to file and spoke it.")
        elif text is None:
            print("Exiting program.")
            break
