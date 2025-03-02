import threading
import time
import sys

try:
    import termios
    import tty
except ImportError:
    print("This script is designed for Linux/macOS and may not work on Windows.")
    sys.exit(1)

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def log_keystrokes():
    with open("keylog.txt", "a") as log_file:
        while True:
            key = get_key()
            log_file.write(key)
            log_file.flush()
            if key == "\x03":  # Stop on Ctrl+C
                break

def main():
    print("Keylogger started. Press Ctrl + C to stop.")
    try:
        log_keystrokes()
    except KeyboardInterrupt:
        print("\nStopping keylogger...")

if __name__ == "__main__":
    main()
