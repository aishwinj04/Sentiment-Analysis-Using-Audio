from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment

# given any format file convert to wav for speech recognition
def to_wav(audiofile):
    audio = AudioSegment.from_file(audiofile) 
    wav_file = f'{audiofile}.wav'
    audio.export(wav_file, format='wav')

    return wav_file

def transcribe(wav_file):
    recognizer = Recognizer()

    # handle resource management 
    with AudioFile(wav_file) as af:
        audio = recognizer.record(af)
    
    # transcribe using Google's web speech api
    text = recognizer.recognize_google(audio)

    return text

