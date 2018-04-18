# aliyun-sms-alert

Python实现短信发送服务
1. 集成阿里大于短信SDK
2. 监控机房警报信息
3. 定制短信模板发送短信
4. 定制server地址和端口，通过post请求转发给阿里大于


## Environment
Python2.7

## Install service
``` shell
sudo ./install.sh
```

## Setting the config.ini
```
[oem_sms]
access_key = LTAITL5BlzNnTDRn
access_key_secret = rfRlhxOKtdpPmwPmZmvnh0oIdbHNVy
server_host = 0.0.0.0
server_port = 50800
```

## Restart the service
``` shell
sudo service aliyun-sms-alert restart
```

## Uninstall the service
``` shell
sudo ./uninstall.sh
```

## REST
* POST /send_sms: send sms alert
```json
{
  "phone":"10000000",
  "sign_name":"",
  "template_code":"",
  "params":{}
}
```
* POST /setting: set the sms limit to send in one day
```json
{
  "limit":5
}
```
* POST /clear: clear the queue

## Other
* log:/var/log/aliyun-sms-alert/aliyun-sms-alert.log
* config.ini:/etc/opt/aliyun-sms-alert/config.ini
