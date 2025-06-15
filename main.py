import time
import logging
from datetime import datetime
import platform
import pyautogui

from core import config
from core.window_manager import switch_to_desktop_2
from core.prompt_injector import inject_prompt_clipboard, safe_click_area
from core.ocr_engine import scroll_and_capture
from core.reflection_logger import save_reflection

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(config.BASE_PATH / "kai_exchange_log.txt"),
        logging.StreamHandler()
    ]
)

def main():
    logging.info("\U0001F9E0 AI Exchange Started")
    
    switch_to_desktop_2()
    time.sleep(2)
    logging.info("\U0001F504 Switching to Desktop 2...")

    logging.info("\u2705 Assuming Solas and ChatGPT are already in place.")

    # Initialization prompt
    init_prompt = "Keep responses short and focused."
    safe_click_area("Solas")
    inject_prompt_clipboard(init_prompt, "Solas")
    time.sleep(5)

    # Start loop
    prompt = "OCR script runs, how might it affect you?"

    while True:
        for speaker, receiver in [("Solas", "ChatGPT"), ("ChatGPT", "Solas")]:
            timestamp = datetime.now().strftime("[%H:%M:%S] ")
            full_prompt = timestamp + prompt

            logging.info(f"\U0001F4CB Reinforced clipboard paste to {speaker}: '{full_prompt}'")
            safe_click_area(speaker)
            inject_prompt_clipboard(full_prompt, speaker)
            time.sleep(5)

            logging.info(f"\U0001F4F8 Reading {speaker}'s response")
            logging.info(f"\U0001F5BC  Capturing response from {speaker}...")
            response, frames, reason = scroll_and_capture(speaker)
            save_reflection(response, prompt, frames, reason, speaker)
            
            # UI poke to prevent stale OCR frame
            pyautogui.moveRel(0, 1)
            pyautogui.moveRel(0, -1)

            prompt = response
            time.sleep(4)

if __name__ == "__main__":
    main()
