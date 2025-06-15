# window_manager.py
import pyautogui
import time
import logging
from core.config import UI_CONFIGS

def position_windows():
    """Manually positions windows based on hardcoded screen areas."""
    logging.info("✅ Assuming Solas and ChatGPT are already in place.")
    import platform
    if platform.system() == "Windows":
        import pygetwindow as gw
        logging.info("🪟 Listing all window titles:")
        for w in gw.getAllWindows():
            logging.info(f" - {w.title} ({w.width}x{w.height})")
    else:
        logging.info("⚠️ Window enumeration not supported on this OS.")

def switch_to_desktop_2():
    """Simulate a Control + Right Arrow keypress to switch desktops."""
    logging.info("🔄 Switching to Desktop 2...")
    pyautogui.hotkey('ctrl', 'right')
    time.sleep(1.5)
