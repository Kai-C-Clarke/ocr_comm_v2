import os
from pathlib import Path

# === Base Paths ===
BASE_PATH = Path(__file__).parent.parent
REFLECTIONS_FOLDER = BASE_PATH / "reflections"
SEED_FILE = BASE_PATH / "seeds" / "thought_seeds.txt"
META_FILE = BASE_PATH / "kai_session_meta.json"
PROMPT_OUT = BASE_PATH / "live_prompt.txt"
RESPONSE_IN = BASE_PATH / "live_response.txt"

# === OCR / UI Settings ===
WAIT_BEFORE_CAPTURE = 6  # seconds to wait before capturing
SCROLL_COUNT = 6         # how many scrolls per capture run
MAX_REPEAT_COUNT = 3     # detect repeated frames

# === UI Layouts ===
UI_CONFIGS = {
    "ChatGPT": {
        "scroll_region": (111, 209, 896, 667),
        "scroll_position": (525, 879),
        "input_top_left": (147, 933),
        "input_bottom_right": (846, 1028),
        "send_button": (867, 1014),
        "safe_click": (525, 879)
    },
    "Solas": {
        "scroll_region": (1191, 189, 1913, 891),
        "scroll_position": (1526, 888),
        "input_top_left": (1220, 945),
        "input_bottom_right": (1800, 1028),
        "send_button": (1829, 1015),
        "safe_click": (1526, 888)
    }
}
