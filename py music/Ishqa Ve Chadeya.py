import pygame
import time
import os

def play_song_and_lyrics():
    # Check if the song file exists
    song_path =r"C:\Users\ppras\OneDrive\Desktop\py music\Ishqa Ve Chadeya M.mp3"
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
        "Ishqa Ve Chadeya 💫",
        "Tu Kakh Da Ni Sanu 🎶",
        "Ishqa Ve Chadeya 💭",
        "Tu Kakh Da Ni Sanu ❤",
        "Takkde Aa Jinu Oh🥺",
        "Takkda Ni Saanu 💔",
        "Takkde Aa Jinu Oh 🌙",
        "Takkda Ni Saanu 💞",
        "Phirde Aa Jinu 💫",
        "Khayalan Ch Sambhi 🎶",
        "Phirde Aa Jinu 💭",
        "Khayalan Ch Sambhi ❤",
        "Nazran De Vich Vi🥺",
        "Oh Rakhda Nai Sanu 💔",
        "Ishqa Ve Chadeya 🌙",
        "Tu Kakh Da Ni Sanu 💞",
    ]

    print("\n🎧 Now Playing - Ishqa Ve Chadeya ❤\n")
    time.sleep(1)

    # Display lyrics with delay
    for line in lyrics:
        print(f"🎶 {line}")
        time.sleep(2)

    # Wait until the song finishes
    try:
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\n⏹ Playback stopped by user.")

play_song_and_lyrics()