import wave
import math

morse_code_table = {
        "a": ". -",
        "b": "- . . .",
        "c": "- . - .",
        "d": "- . .",
        "e": ".",
        "f": ". . - .",
        "g": "- - .",
        "h": ". . . .",
        "i": ". .",
        "j": ". - - -",
        "k": "- . -",
        "l": ". - . .",
        "m": "- -",
        "n": "- .",
        "o": "- - -",
        "p": ". - - .",
        "q": "- - . -",
        "r": ". - .",
        "s": ". . .",
        "t": "-",
        "u": ". . -",
        "v": ". . . -",
        "w": ". - -",
        "x": "- . . -",
        "y": "- . - -",
        "z": "- - . .",
        }
def letter_to_morse_code(letter):
    return morse_code_table[letter]

def word_to_morse_code(word):
    return [letter_to_morse_code(letter) for letter in word]

def sentence_to_morse_code(sentence):
    return [word_to_morse_code(word) for word in sentence.split(" ")]

def morse_code_time(code):

    dot_length = 0.05 #seconds.
    dash_length = 3 * dot_length
    # gaps are silence

    normal_gap = dot_length 
    letter_gap = 3 * dot_length
    word_gap = 7 * dot_length

    seconds = 0
    for word in code:
        for letter in word:
            if letter == ".":
                seconds += dot_length
            else:
                seconds += dash_length
            seconds += letter_gap
        seconds += word_gap
    
    return seconds

def morse_code_wav_data(code, frequency, frames_per_second):
    data = []
    seconds = morse_code_time(code)
    for frame in range(round(seconds * frames_per_second)):
        time = frame / frames_per_second
        amplitude = math.sin(2 * math.pi * frequency * time)
        data.append(round(amplitude / 255.0))
    return data

def generate_morse_code_audio(name, code):
    frequency = 100
    nchannels = 1
    frames_per_second = 8000
    width = 1
    frames = frames_per_second * morse_code_time(code)
    morse_code_audio = morse_code_wav_data(code, frequency, frames_per_second)
    
    with wave.open(name, mode="wb") as w:
        w.setnchannels(1)
        w.setsampwidth(1)
        w.setframerate(frames_per_second)
        w.writeframes(bytes(morse_code_audio))

    '''
        Create a wave object.
        Transcribe the dashes and dots as beeps of varying sounds.
        Save this into a wav file
    '''
    pass


if __name__ == "__main__":
    print("Enter the text to be converted to a wav file:")
    user_input = "Hello"#input()
    user_input = user_input.lower()
    if user_input == "":
        print("Please enter a non empty string.")
    else:
        morse_code = sentence_to_morse_code(user_input)
        name = "morse-code.wav"
        generate_morse_code_audio(name, morse_code)
        print("Complete")
