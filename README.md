# おでかけプランナー

富山県に住む人や観光客が「どこに行こうか迷ったとき」に使えるおでかけスポット提案Webアプリです。
エリア・同行者・ジャンル・所要時間の4つの条件を選んで、富山県内のおすすめスポットを提案します。
子連れファミリーから一人旅まで、さまざまなシーンに対応したスポットを登録しています。

## 公開URL

https://odesuke-planner.onrender.com

## 機能

- エリア・同行者・ジャンル・所要時間の4条件でスポット検索
- 検索結果の一覧表示
- スポット詳細ページ
- スマホ対応（レスポンシブデザイン）

## 使用技術

| カテゴリ | 技術 |
|------|------|
| フロントエンド | HTML / CSS / JavaScript |
| バックエンド | Python / Flask |
| データベース | SQLite |
| ソース管理 | GitHub |
| 公開 | Render |

## ディレクトリ構成

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

## 実装上の工夫

- 富山県の実在するスポットを23件登録
- 4つの条件を組み合わせた柔軟な検索機能
- スマホで使いやすいシンプルなUI設計

## ローカルでの起動方法

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
