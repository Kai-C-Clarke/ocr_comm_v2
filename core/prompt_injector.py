import time
import pyautogui
import logging
from core.config import UI_CONFIGS

def inject_prompt(prompt: str, ui: str):
    """Send a prompt to the specified UI target ('ChatGPT' or 'Solas')."""
    try:
        coords = UI_CONFIGS[ui]

        # Focus safe area in the window
        pyautogui.click(*coords["safe_click"])
        time.sleep(0.5)
        pyautogui.press('esc')  # Dismiss emoji or overlay
        time.sleep(0.3)

        # Click into input box
        pyautogui.click(*coords["input_top_left"])
        time.sleep(0.2)

        # Clear previous input
        pyautogui.hotkey('command', 'a')
        pyautogui.press('backspace')
        time.sleep(0.3)

        # Type prompt
        pyautogui.write(prompt, interval=0.03)
        time.sleep(0.3)
        pyautogui.press('enter')

        logging.info(f"✅ Prompt sent to {ui}: {prompt[:60]}...")
    except Exception as e:
        logging.warning(f"❌ Failed to inject prompt to {ui}: {e}")

