from speech_recognition import Recognizer, AudioFile

def process_audio(audiofile):
    recognizer = Recognizer()

    # handle resource management 
    with AudioFile(audiofile) as af:
        audio = recognizer.record(af)
    
    # transcribe using Google's web speech api
    text = recognizer.recognize_google(audio)

    return text



        
