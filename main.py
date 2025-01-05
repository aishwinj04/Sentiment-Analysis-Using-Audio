from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment

# brew install ffmpeg

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
    text = recognizer.recognize_google(audio)

    return text


def main():


    audio_file = 'assets/greatgatsby01.mp3'
    wav_file = to_wav(audio_file)


    to_text = transcribe(wav_file)
    print(to_text)  # output delayed based on size of file


if __name__ == '__main__':
    main()
