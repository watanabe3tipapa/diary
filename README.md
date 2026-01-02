# diary_

GitHub を日記帳として使うためのリポジトリです。

## 特徴

-   **日次自動作成**: GitHub Actions により、毎日自動的に日記のテンプレートが作成されます。
-   **ローカル作成**: スクリプトを使用して、ローカル環境でも簡単に日記を作成・編集できます。

## 使い方

### ローカルでの使用

このリポジトリをクローンした後、以下のスクリプトを使用して日記を作成できます。

#### Python スクリプト

```bash
# 今日の日記を作成してエディタで開く
python3 scripts/create_diary.py

# 日付を指定して作成
python3 scripts/create_diary.py --date 2025-01-01
```

#### Shell スクリプト

```bash
# 今日の日記を作成してエディタで開く
./scripts/create_diary.sh

# 日付を指定して作成
./scripts/create_diary.sh diary 2025-01-01
```

### GitHub Actions

`.github/workflows/diary.yml` により、毎日 UTC 00:00 (JST 09:00) に新しい日記ファイルが `diary/` ディレクトリに自動作成されます。

## ライセンス

このプロジェクトは [MIT License](LICENSE) の下でライセンスされています。
