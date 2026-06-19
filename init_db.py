import sqlite3

conn = sqlite3.connect('spots.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS spots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT,
        genre TEXT,
        companion TEXT,
        duration TEXT,
        description TEXT,
        point TEXT
    )
''')

# サンプルデータ
c.execute('''
    INSERT INTO spots (name, city, genre, companion, duration, description, point)
    VALUES
    ('立山黒部アルペンルート', '立山町', '自然', '家族', '1日',
     '標高3,000m級の山岳観光ルート。雪の大谷が有名。',
     '春の雪の壁は圧巻！子どもも大喜びの絶景スポット'),
    ('富山市ガラス美術館', '富山市', '文化', 'カップル', '2時間',
     '世界的建築家設計の美術館。ガラス作品が美しい。',
     'おしゃれな空間でゆっくり芸術鑑賞できる'),
    ('おわら風の盆', '富山市', '文化', '友人', '半日',
     '毎年9月に開催される伝統的な盆踊りのお祭り。',
     '幻想的な踊りと音楽が心に残る富山の風物詩')
''')

conn.commit()
conn.close()
print('データベースを作成しました！')