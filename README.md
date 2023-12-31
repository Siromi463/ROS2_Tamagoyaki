# robosys2023
[![test](https://github.com/Siromi463/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Siromi463/mypkg/blob/main/.github/workflows/test.yml)

[![test](https://github.com/Siromi463/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Siromi463/mypkg/blob/main/.github/workflows/test_num.yml)

## 概要

* このパッケージは、ロボットシステム学の課題提出用のものです。
* パッケージ内にはtalk_listen.launch.py、num_talk_listen.launch.pyというローンチファイルがあります。

## インストール方法


１．ターミナル内でリポジトリをクローンする。
```
$ git clone https://github.com/Siromi463/mypkg.git
```

２．インストールされているか確認。(mypkgが表示されていればOK)
```
$ ls
mypkg
```

３．使ってみよう！

## 使い方

###talk_listen.launch.py

* talkerノードとlistenerノードを使用。
	* 約0.5秒刻みで1から順に整数を表示
* 以下で実行
```
$ ros2 run mypkg talk_listen.launch.py
```

###num_talk_listen.launch.py

* 使用ノードは以下
	* talker_rand.py	:0~100のランダムな整数を生成
	* listener_rand.py	:生成された整数を表示
	* listener_even.py	:生成された整数が奇数か偶数か表示
	* listener_prime.py	:生成された整数が素数かどうか表示
* 以下で実行
```
$ ros2 run mypkg num_talk_listen.launch.py
```

## 必要なソフトウェア
* Python
* ROS2 humble

## テスト環境
* Ubuntu 22.04.2 LTS

## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
	* © 2023 Siromi463

* このソフトウェアパッケージ内の一部コードは、以下のリンクから、著者の許諾を得て改変しています。
	* [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
	* © 2022 Ryuichi Ueda
