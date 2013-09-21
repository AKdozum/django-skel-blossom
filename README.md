# django-skel-blossom

（日本の）VPS向けdjango-skelフォーク

## Install

必要なもの

* pip
* django 1.5
* bower

あると良いもの

* sass

## Get Start

主に通常と違う部分の紹介

### プロジェクトの作成

    $ django-admin.py startproject --template=[path_or_uri] [project_name]
    $ cd [project_name]

### .gitignore が含まれています

    $ git init
    $ git add .
    $ git commit -m "first commit"

### 依存するソフトウェアのインストール

必要なものが増えたら，適宜 ``reqs`` 以下を更新します．

    $ pip install -r reqs/dev.txt
    $ cd [project_name]/assets
    $ bower install

### アプリケーションの作成

``apps`` 以下に配置します．

    $ mkdir [project_name]/apps/[app_name]
    $ python manage.py startapp [app_name] [project_name]/apps/[app_name]

### 404.html, 500.html の作成

テンプレートを ``make`` でレンダリングします．

    $ cd [project_name]/templates
    $ make

### デプロイの参考

    $ git clone [repository]
    $ cd [project_name]
    $ pip install -r reqs/prod.txt
    $ cd [project_name]/assets
    $ bower install
    $ cd ../templates
    $ make
    $ cd ..
    $ ./manage.py collectstatic
    $ # プロジェクトに合わせていろいろ

