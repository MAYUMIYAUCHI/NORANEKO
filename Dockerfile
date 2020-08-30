# ベースとするDockerイメージを指定
FROM python:3.7-alpine

# リアルタイムでログを見れるように環境変数を指定
ENV PYTHONUNBUFFERD 1

# ローカルのrequirements.txtをコンテナにコピー
COPY ./requirements.txt /requirements.txt

# requirements.txtに従ってパッケージを一括でインストール
RUN pip install -r /requirements.txt

# Djangoプロジェクトを置くディレクトリをコンテナ上に作成
RUN mkdir /noranekoproject

# コンテナ上の作業するディレクトリを変更
WORKDIR /noranekoproject

# ローカルのprofiles-rest-apiディレクトリをコンテナにコピー
COPY ./noranekoproject /noranekoproject

# アプリケーションを実行するためのユーザを作成する
# -D：Don't assign a password
RUN adduser -D user

# ユーザをrootから変更
USER user