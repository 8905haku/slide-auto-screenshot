## 🧾 What is this
プレゼンテーションのスライドを自動でスクリーンショットを行い、  
指定した ディレクトリに保存するソフトウェアです。

プレゼン内容を後から見返したい人向けのツールです。


## 🚀 Getting Started

`launch.py` を実行するだけで起動します。

```bash
python launch.py
```

## ⚙️ Configuration
config.example.json をコピーし、onfig.json にリネーム、そして各値を編集。  
### 要素
---
    "tps": "更新速度",

    "pixel_diff_value_threshold" : "検知する変化の大きさ",

    "target_display_index" : "スクショする指定のディスプレイのインデックス,

    "output_dir_path" : "どこにスクショしたがぞうを保存するか"
---

## ⚠️ 注意

### 他のウィンドウで画面を隠さない。
スクショしたい画面は常に表示しておく必要があります。

### 設定ファイル
config.json の Keyは変更しないことをお勧めします。  
変更すると参照されなくなります。  

---