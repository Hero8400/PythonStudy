# RasberryPi勉強用

## 使用したRasberryPi

RasberryPi 4　8GB Model:B

<br/>

## RasberryPiで日本語入力を可能にする

### インストールするソフト

1. iBus

    様々な言語の入力メソッドを提供する。

2. Mozc

   日本語入力エンジンの1つ

上記の組み合わせにより、日本語入力を可能にする。

### インストール手順

1. 下記のコマンドを実施

   ~~~
   pi@raspberrypi:~ $ sudo apt install ibus-mozc
   ~~~

2. 「続行しますか？[Y/n]」と表示されるので"Y"を入力する。

3. エラーが出ずにインストールが完了したことを確認して再起動を実施。

    <br/>

上記を実施したら、GUI画面の右上にIMEのアイコンが表示される。

## 

## RasberryPiにvimを準備する

1. vimをインストールする。

    ~~~
    pi@raspberrypi:~ $ sudo apt install vim
    ~~~

2. シンタックスハイライトと自動インデントの設定をする。

    ~~~
    pi@raspberrypi:~ $ sudo vi /etc/vim/vimrc
    ~~~

    [シンタックスハイライト]

    ~~~
    syntax on
    ~~~

    [自動インデント機能]

    ~~~
    if has("autocmd")
        filetype plugin indent on
    endif
    ~~~

### aptとapt-getの違いについて

apt-getには脆弱性などの面で問題になっている部分があったが、
aptはそれが改善されている。いわゆる上位互換。