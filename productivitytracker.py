import time
import psutil
import pygame
from plyer import notification

def detect_game():
    pygame.mixer.init()
    sound_playing = False

    # List of processes associated with games
    game_processes = ["steam.exe"]

    while True:
        # Check if a game is running
        game_running = any(process.name().lower() in game_processes for process in psutil.process_iter(['name']))

        if game_running and not sound_playing:
            start_timer()
            sound_playing = True
        elif not game_running and sound_playing:
            stop_timer()
            sound_playing = False

        time.sleep(1 * 60)  # Check every 5 minutes

def start_timer():
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time >= 1 * 60:  # 1 hour
            play_sound()
            send_notification()

        time.sleep(1 * 60)  # Check every 5 minutes

def stop_timer():
    # Stop the sound and reset the timer
    pygame.mixer.music.stop()

def play_sound():
    # Play a sound (replace 'alarm_clock.mp3' with the path to your sound file)
    pygame.mixer.music.load('C:\\Users\\Basil\\Downloads\\alarm_clock.mp3')
    pygame.mixer.music.play()

def send_notification():
    # Send a desktop notification
    notification.notify(
        title='Game Time Reminder',
        message='You have been gaming for 1 hour. Take a break!',
    )

if __name__ == "__main__":
    detect_game()
