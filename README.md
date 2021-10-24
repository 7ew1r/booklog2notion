# Booklog2Notion

ブクログからエクスポートした CSV ファイルを Notion でインポートできる形式に変換します

## Environment

- Windows 10
- Python 3.10.0

## Usage

1. ブクログの[エクスポート](https://booklog.jp/export) サイトで本棚を CSV ファイルをダウンロードする

2. `main.py` と同じディレクトリに CSV ファイルを配置し、以下のコマンドを実行する

```
python main.py [file_name]
```

3. 生成された `new.csv` を Notion でインポートする
