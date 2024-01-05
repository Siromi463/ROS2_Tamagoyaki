# mypkg
[![test](https://github.com/Siromi463/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Siromi463/mypkg/actions/workflows/test.yml)

[![test_log](https://github.com/Siromi463/mypkg/actions/workflows/test_log.yml/badge.svg)](https://github.com/Siromi463/mypkg/actions/workflows/test_log.yml)

[![test_rand](https://github.com/Siromi463/mypkg/actions/workflows/test_rand.yml/badge.svg)](https://github.com/Siromi463/mypkg/actions/workflows/test_rand.yml)

[![test_tobinary](https://github.com/Siromi463/mypkg/actions/workflows/test_tobinary.yml/badge.svg)](https://github.com/Siromi463/mypkg/actions/workflows/test_tobinary.yml)

[![test_tohex](https://github.com/Siromi463/mypkg/actions/workflows/test_tohex.yml/badge.svg)](https://github.com/Siromi463/mypkg/actions/workflows/test_tohex.yml)

## 概要

* このパッケージは、ロボットシステム学の課題提出用のものです。
* このリポジトリは、ROS2のパッケージです。
* パッケージ内のノードを使用し、数値変換や解析に役立てることができます。

## トピックについて

* パッケージ内には、chatterという名前のトピックを使用してInt16型整数をパブリッシュ及びサブスクライブするのノードが含まれています。

## ノード

* このパッケージには、以下のノードがあります。
	* talker
	* talker_rand
	* talker_data
	* listener
	* listener_log
	* converter_tobinary
	* converter_tohex
* talker系統は、トピックを通じてデータをパブリッシュします。
* listenerやconverter系統は、パブリッシュされたデータをサブスクライブして、対応した動作を行います。
* 各ノードは、各端末で以下のようにしてターミナルで実行します。(node_name)は対応したノード名へ。
```
ros2 run mypkg (node_name)
```

### talker

* このノードは、約0.5秒刻みで0から順に整数をパブリッシュします。
* このノードは、chatterトピックを通じて、Int16型の整数をパブリッシュします。

#### 実行結果
* 後述するlistenerを利用して、実行結果を見ます。
```
端末1 ros2 run mypkg talker
- - - - - - - - - - - - - - - - - - - - - - - - - - -
端末2 ros2 run mypkg listener
[INFO] [1704344802.411140396] [listener]: Listen: 0
[INFO] [1704344802.891190283] [listener]: Listen: 1
[INFO] [1704344803.391192679] [listener]: Listen: 2
[INFO] [1704344803.891134381] [listener]: Listen: 3
[INFO] [1704344804.391156519] [listener]: Listen: 4
[INFO] [1704344804.890343784] [listener]: Listen: 5
・・・
```
### talker_data

* このノードは、約0.5秒刻みで0から20まで順に整数をパブリッシュします。
* このノードは、chatterトピックを通じて、Int16型の整数をパブリッシュします。

#### 実行結果
* 後述するlistenerを利用して、実行結果を見ます。
```
端末1 ros2 run mypkg talker_data
- - - - - - - - - - - - - - - - - - - - - - - - - - -
端末2 ros2 run mypkg listener
[INFO] [1704344802.411140396] [listener]: Listen: 15
[INFO] [1704344802.891190283] [listener]: Listen: 16
[INFO] [1704344803.391192679] [listener]: Listen: 17
[INFO] [1704344803.891134381] [listener]: Listen: 18
[INFO] [1704344804.391156519] [listener]: Listen: 19
[INFO] [1704344804.890343784] [listener]: Listen: 20
端末2
```
* このノードは、パブリッシュを一定の範囲までに限定したいときに使っています。

### talker_rand

* このノードは、約3秒刻みで0~100の範囲のランダムな整数をパブリッシュします。
* このノードは、chatterトピックを通じて、Int16型の整数をパブリッシュします。

#### 実行結果
* 後述するlistenerを利用して、実行結果を見ます。
```
端末1 ros2 run mypkg talker_rand
- - - - - - - - - - - - - - - - - - - - - - - - - - -
端末2 ros2 run mypkg listener
[INFO] [1704344802.411140396] [listener]: Listen: 65
[INFO] [1704344802.891190283] [listener]: Listen: 24
[INFO] [1704344803.391192679] [listener]: Listen: 49
[INFO] [1704344803.891134381] [listener]: Listen: 82
[INFO] [1704344804.391156519] [listener]: Listen: 46
[INFO] [1704344804.890343784] [listener]: Listen: 51
・・・
```
* このノードは、ランダムなデータに対して、何か動作を行いたいときに使えます。

### listener

* このノードは、サブスクライブした整数を表示します。
* このノードは、chatterトピックを通じて、Int16型の整数をサブスクライブします。
* 実行結果はtalkerの説明でも触れたため省略します。
* talker系統からパブリッシュされたデータをそのまま見たい時に使っています。

### listener_log

* このノードは、サブスクライブした整数を、log.txtというファイルに一時的に保存します。
* このノードは、chatterトピックを通じて、Int16型の整数をサブスクライブします。
* log.txtは、実行のたびに上書きされます。
* log.txtは、一つ目のmypkgディレクトリにあります。

#### 実行結果
* talker_dataからデータをサブスクライブして使ってみます。
```
端末1 ros2 run mypkg talker_data
- - - - - - - - - - - - - - - - - - - - - - - - - - -
端末2 ros2 run mypkg listener_log
Successfully wrote '1' to the file
Successfully wrote '2' to the file
Successfully wrote '3' to the file
Successfully wrote '4' to the file
Successfully wrote '5' to the file
・・・
Successfully wrote '16' to the file
Successfully wrote '17' to the file
Successfully wrote '18' to the file
Successfully wrote '19' to the file
Successfully wrote '20' to the file
端末2
```
また、log.txt内には、以下のようにデータが入ります。
```
$ cat log.txt
1
2
3
・・・
18
19
20
```
* このノードは、センサデータなどを一時保存して、分析したい時などに使えます。

### converter_tobinary

* このノードは、サブスクライブした整数を、2進数に変換し表示します。
* このノードは、chatterトピックを通じて、Int16型の整数をサブスクライブします。
#### 実行結果
* talkerからデータをサブスクライブして使ってみます。
```
端末1 ros2 run mypkg talker
- - - - - - - - - - - - - - - - - - - - - - - - - - -
端末2 ros2 run mypkg converter_tobinary
Received value: 0, Binary: 0000000000000000
Received value: 1, Binary: 0000000000000001
Received value: 2, Binary: 0000000000000010
Received value: 3, Binary: 0000000000000011
Received value: 4, Binary: 0000000000000100
Received value: 5, Binary: 0000000000000101
Received value: 6, Binary: 0000000000000110
・・・
```
* このノードは、2進数でのデータを必要とする場合に使えます。

### converter_tohex

* このノードは、サブスクライブした整数を、16進数に変換し表示します。
* このノードは、chatterトピックを通じて、Int16型の整数をサブスクライブします。
#### 実行結果
* talker_randからデータをサブスクライブして使ってみます。
```
端末1 ros2 run mypkg talker_rand
- - - - - - - - - - - - - - - - - - - - - - - - - - -
端末2 ros2 run mypkg converter_tohex
Received value: 16, Hex: 0010
Received value: 78, Hex: 004e
Received value: 33, Hex: 0021
Received value: 77, Hex: 004d
・・・
```
* このノードは、16進数でのデータを必要とする場合に使えます。

## ローンチファイル
* パッケージ内のローンチファイルを利用すると、複数端末を使わずに、talkerやliatener等を同時に起動することができます。
* パッケージ内には、以下のようなローンチファイルがあります。
	* talk_listen.launch.py
	* rand_talk_listen.launch.py
	* log_talk_listen.launch.py
	* tobinary.launch.py
	* tohex.launch.py
* 各ローンチファイルはターミナルで以下のようにして実行できます。(launch name)には、対応したローンチファイル名をいれてください。
```
$ ros2 launch (launch name).launch.py
```

### talk_listen.launch.py
* talkerとlistenerを同時に起動します。

#### 実行結果
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [899]
[INFO] [listener-2]: process started with pid [901]
[listener-2] [INFO] [1704349769.834639530] [listener]: Listen: 0
[listener-2] [INFO] [1704349770.313751302] [listener]: Listen: 1
[listener-2] [INFO] [1704349770.814175785] [listener]: Listen: 2
[listener-2] [INFO] [1704349771.314088511] [listener]: Listen: 3
[listener-2] [INFO] [1704349771.814215709] [listener]: Listen: 4
[listener-2] [INFO] [1704349772.313868996] [listener]: Listen: 5
```

### rand_talk_listen.launch.py
* talker_randとlistenerを同時に起動します。

#### 実行結果
```
$ ros2 launch mypkg rand_talk_listen.launch.py
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker_rand-1]: process started with pid [922]
[INFO] [listener-2]: process started with pid [924]
[listener-2] [INFO] [1704349890.894765371] [listener]: Listen: 87
[listener-2] [INFO] [1704349893.874198507] [listener]: Listen: 60
[listener-2] [INFO] [1704349896.874164850] [listener]: Listen: 40
[listener-2] [INFO] [1704349899.874280504] [listener]: Listen: 34
[listener-2] [INFO] [1704349902.873772956] [listener]: Listen: 38
```

### log_listen.launch.py
* talker_dataとlistener_logを同時に起動します。

#### 実行結果
```
$ ros2 launch mypkg log_talk_listen.launch.py
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker_data-1]: process started with pid [945]
[INFO] [listener_log-2]: process started with pid [947]
[talker_data-1] [INFO] [1704349963.721264672] [talker_data]: Publishing: "1"
[talker_data-1] [INFO] [1704349964.200585737] [talker_data]: Publishing: "2"
[talker_data-1] [INFO] [1704349964.701223310] [talker_data]: Publishing: "3"
[talker_data-1] [INFO] [1704349965.200708171] [talker_data]: Publishing: "4"
[talker_data-1] [INFO] [1704349965.700977149] [talker_data]: Publishing: "5"
```
* また、listener_logの説明の時と同様、log.txtにデータが保存されます。

### tobinary.launch.py
* talkerとconverter_tobinaryを同時に起動します。

#### 実行結果
```
$ ros2 launch mypkg tobinary.launch.py
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [975]
[INFO] [converter_tobinary-2]: process started with pid [977]
[converter_tobinary-2] Received value: 0, Binary: 0000000000000000
[converter_tobinary-2] Received value: 1, Binary: 0000000000000001
[converter_tobinary-2] Received value: 2, Binary: 0000000000000010
[converter_tobinary-2] Received value: 3, Binary: 0000000000000011
[converter_tobinary-2] Received value: 4, Binary: 0000000000000100
[converter_tobinary-2] Received value: 5, Binary: 0000000000000101
```

### tohex.launch.py
* talkerとconverter_tohexを同時に起動します。

#### 実行結果
```
$ ros2 launch mypkg tohex.launch.py
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [998]
[INFO] [converter_tohex-2]: process started with pid [1000]
[converter_tohex-2] Received value: 0, Hex: 0000
[converter_tohex-2] Received value: 1, Hex: 0001
[converter_tohex-2] Received value: 2, Hex: 0002
・・・
[converter_tohex-2] Received value: 10, Hex: 000a
[converter_tohex-2] Received value: 11, Hex: 000b
[converter_tohex-2] Received value: 12, Hex: 000c
・・・
```

## 必要なソフトウェア
* Python
* ROS2 humble

## テスト環境
* Ubuntu 22.04.2 LTS

## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
* このソフトウェアパッケージ内の一部コードは、以下のリンクから、著者の許諾を得て改変しています。
	* [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
	* © 2023 Siromi463
