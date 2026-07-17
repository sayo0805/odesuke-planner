# 🗾 おでかけプランナー

富山県内のおでかけスポットを条件検索で提案するWebアプリです。

## 🌐 公開URL

https://odesuke-planner.onrender.com

## 📱 アプリ概要

- **対象エリア**：富山県全域
- **ターゲット**：子連れファミリー・カップル・友人同士・一人旅
- **目的**：条件に合う富山県内のおでかけスポットを提案する

## ✨ 機能

- エリア・同行者・ジャンル・所要時間の4条件でスポット検索
- 検索結果の一覧表示
- スポット詳細ページ
- スマホ対応（レスポンシブデザイン）

## 🛠 使用技術

| カテゴリ | 技術 |
|------|------|
| フロントエンド | HTML / CSS / JavaScript |
| バックエンド | Python / Flask |
| データベース | SQLite |
| ソース管理 | GitHub |
| 公開 | Render |

## 📂 ディレクトリ構成

odesuke-planner/

├── app.py

├── init_db.py

├── spots.db

├── requirements.txt

├── Procfile

├── templates/

│   ├── index.html

│   ├── results.html

│   └── detail.html

└── static/

└── style.css

## 💡 工夫した点

- 富山県の実在するスポットを23件登録
- 4つの条件を組み合わせた柔軟な検索機能
- スマホで使いやすいシンプルなUI設計

## 🔧 ローカルでの起動方法

```bash
# リポジトリをクローン
git clone https://github.com/sayo0805/odesuke-planner.git
cd odesuke-planner

# 仮想環境を作成・有効化
python3 -m venv venv
source venv/bin/activate

# ライブラリをインストール
pip install -r requirements.txt

# DBを初期化
python3 init_db.py

# アプリを起動
python3 app.py
```

## 📝 今後の改善案

- スポットへの画像追加
- キーワード検索機能
- お気に入り機能
- スポット数の拡充