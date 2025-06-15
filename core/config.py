from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent
REFLECTIONS_FOLDER = BASE_PATH / "reflections"
META_FILE = BASE_PATH / "kai_exchange_meta.json"

WAIT_BEFORE_CAPTURE = 10

UI_CONFIGS = {
    "Solas": {
        "input_top_left": (1230, 950),
        "send_button": (1829, 1018),
        "read_area_top_left": (1196, 240),
        "read_area_bottom_right": (1884, 800),
        "safe_click": ((1536, 936), (1536, 936)),
        "scroll_region": (1196, 260, 1884, 750),
    },
    "ChatGPT": {
        "input_top_left": (183, 958),
        "send_button": (832, 1025),
        "read_area_top_left": (150, 206),
        "read_area_bottom_right": (873, 862),
        "safe_click": ((410, 920), (410, 920)),
        "scroll_region": (150, 206, 873, 862),
    }
}
