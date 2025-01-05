from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# requires install ffmpeg

# given any format file convert to wav for speech recognition
def to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file) 
    wav_file = f'{audio_file}.wav'
    audio.export(wav_file, format='wav')

    return wav_file

def transcribe(wav_file):
    recognizer = Recognizer()

    # handle resource management 
    with AudioFile(wav_file) as af:
        audio = recognizer.record(af)
    
    # transcribe using Google's web speech api
    text = recognizer.recognize_google(audio) # returns string 

    return text


def analyze_text(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text) # returns dictionary 
    # print(scores)
    mood = ''

    sentiment = scores['compound'] # extract compound value using compound as key
    if(sentiment > 0):
        mood = 'Positive'
    elif(sentiment < 0):
        mood = 'Negative'
        
    return mood 



