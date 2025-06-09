# Desktop and window positioning logic
import os
import time
import pywinctl as gw
import logging

def switch_to_desktop_2():
    """Switch to Desktop 2 using AppleScript."""
    try:
        os.system("""
        osascript -e 'tell application "System Events"
            key down control
            key code 124
            key up control
        end tell'
        """)
        time.sleep(1.5)
    except Exception as e:
        logging.warning(f"❌ Desktop switch failed: {e}")

def position_windows():
    """Align ChatGPT and Solas windows side by side."""
    try:
        chatgpt_windows = gw.getWindowsWithTitle('ChatGPT')
        solas_windows = gw.getWindowsWithTitle('Solas')

        if not chatgpt_windows or not solas_windows:
            raise RuntimeError("❌ Could not find both ChatGPT and Solas windows.")

        kai = chatgpt_windows[0]
        solas = solas_windows[0]

        kai.moveTo(0, 0)
        kai.resizeTo(960, 1080)
        solas.moveTo(960, 0)
        solas.resizeTo(960, 1080)

        logging.info("✅ Windows positioned successfully.")
    except Exception as e:
        logging.warning(f"❌ Window layout failed: {e}")
