import pygame
import time
import os

def play_song_and_lyrics():
    # Check if the song file exists
    song_path =r"C:\Users\ppras\OneDrive\Desktop\py music\Nakshatra Kaalgejje M.mp3"
    if not os.path.exists(song_path):
        print(f"Error: '{song_path}' not found.")
        return

    # Initialize pygame mixer
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(song_path)
    except pygame.error as e:
        print(f"Error loading song: {e}")
        return

    pygame.mixer.music.play()

    lyrics = [
        "Nakshatra Kaalgejje 💫",
        "Mattanthe Aa Lajje 🎶",
        "Ottare, Naagaraholeya 💭",
        "Navilu Kundange ❤",
        "Poorna Chandra🌙",
        "Kayya Bale🥺",
        "Ardha Chandra,Mungurule 💔",
        "Himada bindu, Kannugale 🌙",
        "Nanna Baala... 💞"
    ]

    print("\n🎧 Now Playing - Nakshatra Kaalgejje ❤\n")
    time.sleep(7)

    # Display lyrics with delay
    for line in lyrics:
        print(f"🎶 {line}")
        time.sleep(3)

    # Wait until the song finishes
    try:
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\n⏹ Playback stopped by user.")

play_song_and_lyrics()