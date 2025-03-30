import sys
import time

def print_lyrics():
    lines = [
        ("if the world", 0.1),
        ("was born under us", 0.1),
        ("i wish", 0.2),
        ("i knew better ",0.2),
        ("forever and ever ",0.3)
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
