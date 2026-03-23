import os
import time
import datetime
from pathlib import Path

import mss
import numpy as np

from src.slide_auto_screenshot.modules import config_loader

cfg_dict = config_loader.get_config()
print(cfg_dict)

class Main:
    def __init__(self):
        self.sct = mss.mss()

        self.running = True

        self.last_screenshot = None
        self.save_count = 0
        
        OUTPUT_DIR_PATH = Path(cfg_dict["OUTPUT_DIR_PATH"])
        OUTPUT_DIR_PATH.mkdir(parents=True, exist_ok=True)

        RUN_OUTPUT_DIR_NAME = datetime.datetime.now().strftime("dir_%Y%m%d_%H%M%S_%f")

        self.RUN_OUTPUT_DIR_PATH = OUTPUT_DIR_PATH / RUN_OUTPUT_DIR_NAME
        self.RUN_OUTPUT_DIR_PATH.mkdir()

    def loop(self):
        while self.running:

            screenshot = self.shot()

            if self.last_screenshot is not None:
                curr = screenshot
                prev = self.last_screenshot

                ratio = self.calc_diff_ratio(prev, curr)
                if ratio > 0.2:
                    self.save_screenshot(screenshot)

            else:
                self.save_screenshot(screenshot)

            time.sleep(1 / cfg_dict["TPS"])
    
    # 全画面を取得して、専用の型に変換し返す。
    def shot(self):
        monitor = self.sct.monitors[cfg_dict["TARGET_DISPLAY_INDEX"]]
        return self.sct.grab(monitor)
        
    # 専用の型でスクリーンショットを保存。
    def save_screenshot(self, screenshot):
        self.last_screenshot = screenshot
        self.save_count += 1

        p = self.RUN_OUTPUT_DIR_PATH / f"screenshot_{self.save_count}.png"

        mss.tools.to_png(screenshot.rgb, screenshot.size, output= p) 

        dt_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"save - {dt_now} - {p}")
        return True

    # 画像の差分を比率にして返す。   
    def calc_diff_ratio(self, curr, prev):

        curr_img = np.array(curr)
        prev_img = np.array(prev)

        # サイズ一致前提（違うならresize必要）
        diff = np.abs(curr_img.astype(int) - prev_img.astype(int))

        pixel_threshold = cfg_dict["PIXEL_DIFF_THRESHOLD"]
        changed_pixels = np.sum(np.any(diff > pixel_threshold, axis=2))
        total_pixels = curr_img.shape[0] * curr_img.shape[1]

        return changed_pixels / total_pixels