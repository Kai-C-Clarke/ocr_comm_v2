import time
import pyautogui
import pytesseract
from PIL import Image
import logging
from core.config import UI_CONFIGS, BASE_PATH, WAIT_BEFORE_CAPTURE, SCROLL_COUNT, MAX_REPEAT_COUNT

def clean_text(text: str) -> str:
    return text.replace("\n", " ").strip()

def scroll_and_capture(ui: str):
    """Capture response from the UI using OCR and return cleaned text."""
    region = UI_CONFIGS[ui]["scroll_region"]
    cleaned_all = []
    previous = []
    stop_reason = "maxed"
    frame = 0

    time.sleep(WAIT_BEFORE_CAPTURE)
    logging.info(f"🖼️ Capturing response from {ui}...")

    for _ in range(SCROLL_COUNT):
        screenshot = pyautogui.screenshot(region=region)
        frame_file = BASE_PATH / f"frame_{ui}_{frame}.png"
        screenshot.save(frame_file)

        gray = Image.open(frame_file).convert("L")
        text = pytesseract.image_to_string(gray).strip()
        logging.info(f"[{ui} Frame {frame}] OCR: {text[:60]}...")

        if not text or len(text) < 10:
            stop_reason = "blank"
            break
        if previous[-MAX_REPEAT_COUNT:].count(text) >= MAX_REPEAT_COUNT:
            stop_reason = "repeated"
            break

        cleaned = clean_text(text)
        cleaned_all.append(cleaned)
        previous.append(text)

        pyautogui.scroll(-300)
        time.sleep(0.5)
        frame += 1

    logging.info(f"🧾 Scroll stopped for {ui}: {stop_reason} after {frame} frame(s)")
    return "\n\n".join(cleaned_all), frame, stop_reason
