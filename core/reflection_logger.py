# Logging and session metadata
import json
from datetime import datetime
from core.config import REFLECTIONS_FOLDER, RESPONSE_IN, META_FILE

def save_reflection(text: str, prompt: str, frames: int, reason: str, ui: str):
    """Save the reflection and metadata for this exchange."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_tag = datetime.now().strftime("%Y-%m-%d")
    file = REFLECTIONS_FOLDER / f"kai_reflections_{date_tag}_{ui}.txt"

    with open(file, "a") as f:
        f.write(f"[{now}] Prompt to {ui}:\n{prompt}\n\n[{now}] Response:\n{text}\n{'='*40}\n")

    if ui == "ChatGPT":
        with open(RESPONSE_IN, "w") as f:
            f.write(text)

    meta = {
        "timestamp": now,
        "prompt": prompt,
        "frames": frames,
        "stop_reason": reason,
        "ui": ui
    }

    with open(META_FILE, "w") as f:
        json.dump(meta, f, indent=2)
