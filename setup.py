# -*- encoding: utf-8 -*-

from distutils.core import setup

config = {
    'author': 'Zhanlong Yang',
    'author_email': 'yangzhanlong@scutech.com',
    'name': 'aliyun-sms-alert',
    'version': '0.0.1',
    'description': 'Aliyun SMS alert service',
    'packages': ['aliyun_sms_alert',
        'aliyun_sms_alert/aliyunsdkdysmsapi',
        'aliyun_sms_alert/aliyunsdkdysmsapi/request',
        'aliyun_sms_alert/aliyunsdkdysmsapi/request/v20170525'],
    'scripts': ['bin/aliyun-sms-alert'],
    'data_files': [
        ('/etc/init', ['upstart/aliyun-sms-alert.conf']),
        ('/etc/opt/aliyun-sms-alert', ['config/config.ini'])
    ]
}

setup(**config)

# vim: ts=4 sw=4 sts=4 et:
