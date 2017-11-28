ESP32 Micropython MQTT から IBM Cloud に送信サンプル  2017/11/26

ESP32 MQTT Libraryは以下のものを使用した。
https://github.com/micropython/micropython-lib/tree/mqtt/umqtt.simple

ibm cloud mqttのタイムアウト3600秒。　タイムアウト対策はしていない。

IBM Cloud のSettingメモ
-Internet of Things Platform  ==> 組織IDが付与される
 -MQTTで接続するデバイスを登録する
  -device configuration
   -deviceID, device type, password　パスワードはメモること。設定後は表示することができない。

