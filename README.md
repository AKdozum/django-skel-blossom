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

必要な Python のパッケージが増えたら，適宜 ``reqs`` 以下を更新します．

    $ pip install -r reqs/dev.txt

また，JavaScript と CSS は bower で管理しています．
初期状態では， normalize.css と jquery の latest が指定されています．

    $ cd [project_name]/assets
    $ bower install # bower.json の dependencies が [project_name]/assets/bower へ

ダウンロード先を変えたい場合は
``[project_name]/assets/.bowerrc`` を変更してください．

### アプリケーションの作成

``[project_name]/apps`` 以下に配置されます．

    $ ./manage.py startapp [app_name]

``-s``, ``--skel`` オプションで
``app-skel`` ディレクトリ内のテンプレートを指定できます．

### 404.html, 500.html の作成

テンプレートを ``make`` でレンダリングします．

    $ cd [project_name]/templates
    $ make

その他静的に生成したいテンプレートには ``./manage render`` を利用できます．

### Sass, CoffieeScript とか

参考: [COMPRESS_PRECOMPILERS - Django Compressor 1.3 documentation](http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_PRECOMPILERS)

### DEBUG = True でログに色が着きます

楽しい！！ ✌('ω'✌ )三✌('ω')✌三( ✌'ω')✌

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

