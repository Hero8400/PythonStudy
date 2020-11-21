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

## RasberryPiにgit環境を作成する。

1. gitをインストールする。

   下記のコマンドを入力

   ~~~
   pi@raspberrypi:~ $ sudo apt install git-all
   ~~~

2. Gitの初期化を実行

   下記のコマンドを実行

   ~~~
   pi@raspberrypi:/etc $ cd /etc
   pi@raspberrypi:/etc $ sudo git init
   Initialized empty Git repository in /etc/.git/
   ~~~

3. Gitに自分の情報を教える

   下記のコマンドを実行

   ~~~
   pi@raspberrypi:/etc $ git config --global user.email "*****@***"
   pi@raspberrypi:/etc $ git config --global user.name "******"
   ~~~

4. Gitクローンを実施する。

   今回はGithubに事前にリポジトリを作成して、クローン用URLを取得して実施する。

   gitを使用したフォルダに移動した後、gitクローンを実施

   下記のコマンドを実行

   ~~~
   pi@raspberrypi:/ $ cd ~/Desktop/RaspberryPi_Study
   pi@raspberrypi:~/Desktop/RaspberryPi_Study $ git clone https://github.com/Hero8400/RasberryPi4.git
   ~~~

5. gitコマンドでコミットする。
   
   コミットするファイルをADDする。

   ~~~
   pi@raspberrypi:~/Desktop/RaspberryPi_Study $ git add LED.py
   ~~~

   メッセージを付けてコミットする。

   ~~~
   pi@raspberrypi:~/Desktop/RaspberryPi_Study/RasberryPi4 $ git commit -m"LEDがピコピコするよ"
   ~~~

   コミットが完了したらプッシュする。

   その際、github上のユーザー名とパスワードも入力が必要。

   ~~~
   pi@raspberrypi:~/Desktop/RaspberryPi_Study/RasberryPi4 $ git push
   Username for 'https://github.com':[username]
   Password for 'https://Hero8400@github.com':[pass]
   ~~~
