from midiutil import MIDIFile 
import pygame

BPM = 180

def text_to_midi(input_file, output_file):
    with open(input_file, 'r') as file:
        notes_text = file.read().lstrip('\n').split()
    spaces_text = []
    current_spaces = 0

    with open(input_file, 'r') as file:
        for line in file:
            for char in line:
                    if char.isspace():
                        current_spaces += 1
                    elif not current_spaces == 0:
                        spaces_text.append(current_spaces)
                        current_spaces = 0

            if not current_spaces == 0:
                spaces_text.append(current_spaces)

    midi = MIDIFile(1)
    midi.addTempo(0, 0, BPM) 

    channel = 0
    time = 0
    n = 0
    duration = 1
    
    for note_text in notes_text:
        notes_array = []
        if len(spaces_text) >> 0 and n < len(spaces_text):
            duration = spaces_text[n]
        else:
            duration = 1

        if time < 512:
            current_note = ""
            b_check = False
            for char in note_text:
                if char.isalpha() and not char == 'b':
                    char = char.upper()
                    if current_note:
                        notes_array.append(current_note)
                    current_note = char
                else:
                    current_note += char

            if current_note:
                notes_array.append(current_note)

            for note in notes_array:
                midi.addNote(channel, 0, note_to_midi_pitch(note), time, duration, 255)
            
            time += duration
            n += 1

    with open(output_file, 'wb') as midi_file:
        midi.writeFile(midi_file)

def note_to_midi_pitch(note):
    note_mapping = {'Cb': 11, 'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'E#': 5, 'Fb': 4, 
                'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11,'B#': 0}
    if note[-1].isdigit():
        note_name = note[:-1]
        octave = int(note[-1])
    else:
        note_name = note[:]
        octave = 3

    if len(note) >= 4 or len(note) == 0 or note == 'b':
        result_to_file("Looks like the notes you wanted to play weren't formatted properly. Sorry about that.")
        exit()

    midi_pitch = note_mapping[note_name] + (octave + 2) * 12
    return midi_pitch

def result_to_file(result):
    file = open("chat_result.txt", "w")
    file.write(result)
    file.close()

def play_midi(midi_file_path):
    pygame.init()

    try:
        pygame.mixer.music.load(midi_file_path)
        print("Now playing: " + midi_file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error: {e}")

    finally:
        pygame.quit()

if __name__ == "__main__":
    input_file = "input_notes.txt"
    output_file = "output.mid"
     
    try:
        text_to_midi(input_file, output_file)
    except Exception as e:
        result_to_file("Looks like the notes you wanted to play weren't formatted properly. Sorry about that.")
        print(e)
        exit()
    result_to_file("Nice little ditty. I liked that. Cool stuff.")
    midi_file_path = "output.mid"
    play_midi(midi_file_path)
   