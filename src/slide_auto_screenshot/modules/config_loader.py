import json
import os
from pathlib import Path
from src.slide_auto_screenshot import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_PATH = BASE_DIR / "config.json"


def load_config_json():
    if not os.path.exists(CONFIG_PATH):
        print("config.json None")
        return {}

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            print("config.json 読み込み完了")
            return json.load(f)
    except Exception:
        # 壊れてても落とさない
        print("config.json 壊れてる")
        return {}


def get_config():
    config_json = load_config_json()

    return {
        "TPS": config_json.get("tps", config.TPS),
        "PIXEL_DIFF_THRESHOLD": config_json.get(
            "pixel_diff_value_threshold", config.PIXEL_DIFF_VALUE_THRESHOLD,
        ),
        "TARGET_DISPLAY_INDEX": config_json.get(
            "target_display_index", config.TARGET_DISPLAY_INDEX
        ),
        "OUTPUT_DIR_PATH": config_json.get(
            "output_dir_path", config.OUTPUT_DIR_PATH
        ),
    }