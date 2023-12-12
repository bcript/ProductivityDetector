import time
import psutil
import pygame
from plyer import notification

def detect_game():
    pygame.mixer.init()

    while True:
        # Check if a game is running
        game_running = any("game" in p.name.lower() for p in psutil.process_iter(attrs=['name']))
        
        if game_running:
            start_timer()
        else:
            stop_timer()

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
    # Play a sound (replace 'beep.mp3' with the path to your sound file)
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
