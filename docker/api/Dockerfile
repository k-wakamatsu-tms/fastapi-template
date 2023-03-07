# ベースイメージを指定
FROM python:3.10-bullseye

# 作業ディレクトリを指定
WORKDIR /workspace
# ソースコードをコンテナ内にコピー
COPY requirements.txt .

# 必要なパッケージをインストール
# パッケージリストの更新、gitのインストール、不要なファイルの削除
RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# パッケージをインストール
RUN pip install -U pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt

# コンテナ起動時に実行するコマンドを指定
# CMD ["python", "app.py"]

