import pyautogui
import pyperclip
import subprocess
import time
import json
import os
import sys
import re


# --- Load Config ---
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

CHROME_PATH = config["chrome_path"]
YOUTUBE_CHANNEL_NAME = config["youtube_channel_name"]
YOUTUBE_VIDEOS_URL = f"https://www.youtube.com/@{YOUTUBE_CHANNEL_NAME}/videos"
NAVER_CAFE_ID = config["naver_cafe_id"]
NAVER_CAFE_MANAGE_GATE_EDITOR_URL = f"https://cafe.naver.com/ManageGateEditor.nhn?clubid={NAVER_CAFE_ID}"

WAIT_TIME_FOR_YOUTUBE = config["wait_time_for_youtube"]
WAIT_TIME_FOR_WEB = config["wait_time_for_web"]
WAIT_TIME_FOR_INPUT = config["wait_time_for_input"]


def click_image(image_name, confidence=0.9, timeout=10):
    """Locate and click image on screen within timeout."""
    print(f"Looking for: {image_name}")
    start = time.time()
    while time.time() - start < timeout:
        location = pyautogui.locateCenterOnScreen(f"images/{image_name}", confidence=confidence)
        if location:
            pyautogui.moveTo(location)
            pyautogui.click()
            return True
        time.sleep(0.5)
    print(f"[ERROR] Couldn't find image: {image_name}")
    return False

def launch_chrome():
    print("Launching Chrome...")
    subprocess.Popen([CHROME_PATH])
    time.sleep(WAIT_TIME_FOR_WEB)  # Wait for Chrome to load

def open_youtube_and_copy_url():
    pyperclip.copy(YOUTUBE_VIDEOS_URL)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(WAIT_TIME_FOR_YOUTUBE)

    # Click kebab menu via image
    if not click_image("kebab_menu.png"): sys.exit("[ERROR] Kebab menu not found")
    time.sleep(WAIT_TIME_FOR_INPUT)

    # Click '공유'
    if not click_image("share_button.png"): sys.exit("[ERROR] Share button not found")
    time.sleep(WAIT_TIME_FOR_INPUT)

    # Click '복사'
    if not click_image("copy_button.png"): sys.exit("[ERROR] Copy button not found")
    time.sleep(WAIT_TIME_FOR_INPUT)

    # URL should now be in clipboard
    return pyperclip.paste()


def update_cafe_main_page(new_url):
    pyautogui.hotkey('ctrl', 't')
    time.sleep(WAIT_TIME_FOR_INPUT)

    pyperclip.copy(NAVER_CAFE_MANAGE_GATE_EDITOR_URL)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(WAIT_TIME_FOR_WEB)

    if not click_image("html_checkbox.png"): sys.exit(1)
    time.sleep(WAIT_TIME_FOR_INPUT)

    # Go to line 5 and replace
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    html = pyperclip.paste()

    new_embed_url = convert_to_embed_url(new_url)
    modified_html = re.sub(
        r'src="https:\/\/www\.youtube\.com\/embed\/[a-zA-Z0-9_\-]+(\?[^"]*)?"',
        f'src="{new_embed_url}"',
        html
    )

    # Paste the modified HTML back
    pyperclip.copy(modified_html)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(WAIT_TIME_FOR_INPUT)

    pyautogui.press('tab')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')

def convert_to_embed_url(url):
    """Convert normal YouTube URL to embeddable format."""
    video_id_match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_\-]{11})", url)
    if video_id_match:
        video_id = video_id_match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    else:
        print("[ERROR] Could not extract video ID from URL.")
        return url  # fallback (but will break iframe)
    

if __name__ == "__main__":
    launch_chrome()
    print("Getting latest YouTube video...")
    video_url = open_youtube_and_copy_url()
    print("Latest video:", video_url)
    print("Updating Naver Cafe...")
    update_cafe_main_page(video_url)
    print("Update complete.")
