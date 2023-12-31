# robosys2023
[![test](https://github.com/Siromi463/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Siromi463/mypkg/actions/workflows/test.yml)

[![test](https://github.com/Siromi463/mypkg/actions/workflows/test_num.yml/badge.svg)](https://github.com/Siromi463/mypkg/actions/workflows/test_num.yml)

## 概要

* このパッケージは、ロボットシステム学の課題提出用のものです。
* パッケージ内にはtalk_listen.launch.py、num_talk_listen.launch.pyというローンチファイルがあります。
* パッケージ内の各talkerノードは、countupトピックを通じてデータを送信しています。

## ローンチファイルの使い方

### talk_listen.launch.py

* talkerノードとlistenerノードを使用。
	* 約0.5秒刻みで1から順に整数を表示
* 以下で実行

```
$ ros2 launch mypkg talk_listen.launch.py
```

#### 実行結果
```
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [1268]
[INFO] [listener-2]: process started with pid [1270]
[listener-2] [INFO] [1704016992.502905041] [listener]: Listen: 0
[listener-2] [INFO] [1704016992.984026432] [listener]: Listen: 1
[listener-2] [INFO] [1704016993.482726319] [listener]: Listen: 2
[listener-2] [INFO] [1704016993.983468875] [listener]: Listen: 3
[listener-2] [INFO] [1704016994.482763648] [listener]: Listen: 4
[listener-2] [INFO] [1704016994.982897496] [listener]: Listen: 5
．．．
```

### num_talk_listen.launch.py

* 使用ノードは以下
	* talker_rand.py	:0~100のランダムな整数を生成
	* listener_rand.py	:生成された整数を表示
	* listener_even.py	:生成された整数が奇数か偶数か表示
	* listener_prime.py	:生成された整数が素数かどうか表示
* 以下で実行
```
$ ros2 launch mypkg num_talk_listen.launch.py
```
#### 実行結果
```
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker_rand-1]: process started with pid [1291]
[INFO] [listener_rand-2]: process started with pid [1293]
[INFO] [listener_even-3]: process started with pid [1295]
[INFO] [listener_prime-4]: process started with pid [1297]
[listener_prime-4] [INFO] [1704017027.392035125] [listener_prime]: not prime
[listener_even-3] [INFO] [1704017027.437674385] [listener_even]: even
[listener_rand-2] [INFO] [1704017027.437674396] [listener_rand]: received: 76
[listener_prime-4] [INFO] [1704017030.366375485] [listener_prime]: not prime
[listener_even-3] [INFO] [1704017030.366255028] [listener_even]: even
[listener_rand-2] [INFO] [1704017030.366481629] [listener_rand]: received: 42
．．．
```

## ノードを個別で立ち上げる場合
* 例：端末１でtalker端末2でlistenerを立ち上げる。
```
端末1 $ ros2 run talker.py
端末2 $ ros2 run listener.py
```
* 各ノードを各端末で立ち上げよう！


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
