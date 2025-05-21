#Voice Translator

import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os


serach_history = []

def main():
    recog1 = spr.Recognizer()
    mc = spr.Microphone()

    with mc as source:
        print("Speak anything to translate!")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)
        try:
            MyText = recog1.recognize_google(audio).lower()
        except spr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
            return
        except spr.RequestError as e:
            print(f"Request error: {e}")
            return
        
        serach_history.append(MyText)
        translate_and_play(recog1)
        

def translate_and_play(recog1):
    translator = Translator()
    from_lang = 'en'
    to_lang = 'hi'  # Change to voice
    mc = spr.Microphone()

    with mc as source:
        print("Speak a sentence...")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)
        get_sentence = recog1.recognize_google(audio)

        try:
            print("Phrase to be Translated: " + get_sentence)
            text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
            translated_text = text_to_translate.text
            speak = gTTS(text=translated_text, lang=to_lang, slow=False)
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")
        except spr.UnknownValueError:
            print("Unable to Understand the Input")
        except spr.RequestError as e:
            print(f"Unable to provide Required Output: {e}")

if __name__ == "__main__":
    is_running = True
    while is_running:
        print("---------------------------------------------")
        print("1-> Translate English to Hindi\n2-> See the Search History\n3-> Clear the search History\n4-> Exit")
        key = int(input("Enter a Key: "))
        
        if key == 1:
            main()
        elif key == 2:
            print(f"{len(serach_history)} items found in search history:")
            for ele in serach_history:
                print(ele)
            print('\n\n')
        elif key == 3:
            print(f"Search History Deleted. {len(serach_history)} elements deleted.")
            serach_history.clear()
            print('\n\n')
        elif key == 4:
            is_running = False
        else:
            print("Please enter a valid Key!")
            os.system('cls')
