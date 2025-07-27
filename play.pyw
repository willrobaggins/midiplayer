import pygame

def play_midi(midi_file_path):
    pygame.init()

    try:
        pygame.mixer.music.load(midi_file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error: {e}")

    finally:
        pygame.quit()

if __name__ == "__main__":
    midi_file_path = "output.mid"
    play_midi(midi_file_path)