import sys
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("./media/Alan Walker - Unity (Lyrics) ft. Walkers.mp3")
pygame.mixer.music.play()

def print_lyrics():
    lines = [
        ("In the dark of night", 0.1),
        ("The stars light up the sky", 0.1),
        ("We see them flying free", 0.1),
        ("That's just like you and me", 0.1),
        ("Everyone is lonely sometimes", 0.1),
        ("But I would walk a thousand miles to see your eyes", 0.1),
        ("You are not alone, we are family", 0.1),
        ("Hold me, let's escape all this reality", 0.1),
        ("You are my symphony", 0.1),
        ("By your side, we are unity", 0.1),
        ("You are my energy", 0.1),
        ("My guiding light, we are unity", 0.1),
        ("We are unity", 0.1),
        ("(We are, we are)", 0.1),
        ("We are unity", 0.1),
        ("Although the rain might pour", 0.1),
        ("A thunder starts to roar", 0.1),
        ("The lightning wakes the wave", 0.1),
        ("But through it, we are brave", 0.1),
        ("Everyone is lonely sometimes", 0.1),
        ("But I would walk a thousand miles to see your eyes", 0.1),
        ("You are not alone, we are family", 0.1),
        ("Hold me, let's escape all this reality", 0.1),
        ("You are my symphony", 0.1),
        ("By your side, we are unity", 0.1),
        ("You are my energy", 0.1),
        ("My guiding light, we are unity", 0.1),
        ("We are unity", 0.1),
        ("(We are, we are)", 0.1),
        ("We are unity", 0.1),
        ("We are unity", 0.1),
        ("You are my symphony (we are)", 0.1),
        ("By your side (we are unity)", 0.1),
        ("You are my energy (we are)", 0.1),
        ("My guiding light (we are unity)", 0.1),
        ("We are unity (unity, unity)", 0.1),
        ("We are unity", 0.1)
    ]
    
    delays = [0.6, 0.7, 1.0]  # Ensure the delays list matches the number of lines

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        print('')  # Move to the next line after printing a full line
        if i < len(delays):  
            time.sleep(delays[i])  # Apply delay between lines

print_lyrics()
