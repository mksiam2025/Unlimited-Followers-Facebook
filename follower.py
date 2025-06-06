import time
import sys
import os

# Safe color codes (optional fallback if terminal doesn’t support color)
class C:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, delay=0.05, color=C.WHITE, newline=True):
    for ch in text:
        sys.stdout.write(color + ch + C.END)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def progress_bar(duration=20):
    length = 40
    for i in range(length + 1):
        percent = int((i / length) * 100)
        bar = '█' * i + '-' * (length - i)
        sys.stdout.write(f"\r{C.WHITE}Progress: [{bar}] {percent}%{C.END}")
        sys.stdout.flush()
        time.sleep(duration / length)
    print()

def main():
    clear()
    type_print("=" * 60, 0.002, C.CYAN)
    type_print(f"{C.BOLD}{C.GREEN}★ WELCOME TO UNLIMITED FACEBOOK FOLLOWER TOOL ★{C.END}", 0.07)
    type_print("=" * 60, 0.002, C.CYAN)

    time.sleep(1)
    print()
    type_print("How many followers do you want?", 0.06, C.BLUE)
    type_print("[1] 1K   [2] 10K   [3] 100K   [4] 1M", 0.05, C.CYAN)
    choice = input(f"{C.BOLD}Enter amount (1K/10K/100K/1M): {C.END}").strip()

    print()
    type_print("Please enter your Facebook profile URL:", 0.05, C.GREEN)
    url = input(f"{C.BOLD}>> {C.END}").strip()

    print()
    type_print("Thanks for your sharing!", 0.06, C.CYAN)
    type_print("Connecting to Facebook servers...", 0.06, C.BLUE)
    time.sleep(1)

    print()
    progress_bar(duration=20)

    print()
    type_print("Successfully completed your request!", 0.07, C.GREEN)
    time.sleep(1)
    type_print(f"{C.RED}{C.BOLD}YOU ARE FOOL 🤣 THIS WAS A PRANK TOOL!{C.END}", 0.09)

if __name__ == "__main__":
    main()
