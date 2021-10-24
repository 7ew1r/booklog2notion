
import sys
import csv

if not (len(sys.argv) == 2):
    print('ファイル名がありません')
    exit(1)

file_name = sys.argv[1]

# ファイルオープン
# サービスID, アイテムID, 13桁ISBN, カテゴリ, 評価, 読書状況, レビュー, タグ, 読書メモ(非公開), 登録日時, 読了日, タイトル, 作者名, 出版社名, 発行年, ジャンル, ページ数
with open(file_name, 'rt', encoding='shift_jis') as csv_file:
    reader = csv.reader(csv_file)
    data = [row for row in reader]

# 不正な日付データを削除 (Notion クラッシュ対策)
# 0000-00-00 00:00:00
data = [[item.replace('0000-00-00 00:00:00', '') for item in row] for row in data]

# タイトルカラムを左端に
for row in data:
    row[0], row[11] = row[11], row[0] 

# ヘッダー行を追加
header = ['タイトル', 'アイテムID', '13桁ISBN', 'カテゴリ', '評価', '読書状況', 'レビュー', 'タグ', '読書メモ(非公開)', '登録日時', '読了日',  'サービスID' ,'作者名', '出版社名', '発行年', 'ジャンル', 'ページ数']
data.insert(0, header)

# ファイル出力
with open("new.csv", mode='w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
