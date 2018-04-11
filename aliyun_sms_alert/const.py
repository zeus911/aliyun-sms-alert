# -*- encoding: utf-8 -*-

import ConfigParser
import logging
import sys
import os

def _config_get(config, section, name, default=None):
    try:
        return unicode(config.get(section, name))
    except:
        return default


class _Config(object):
    REGION = "cn-hangzhou"
    PRODUCT_NAME = "Dysmsapi"
    DOMAIN = "dysmsapi.aliyuncs.com"

    CONFIG_PATH = '/etc/opt/aliyun-sms-alert/config.ini'
    CONFIG_SESSION = 'oem_sms'

    LOG_FILE = '/var/log/aliyun-sms-alert/aliyun-sms-alert.log'
    MSG_QUEUE_PATH = '/var/lib/aliyun-sms-alert/messages'
    MSG_QUEUE_TEMPDIR = '/var/lib/aliyun-sms-alert/messages/tempdir'

    SEND_ALERT_URI = '/send_sms'

    PARAMS = u'params'
    PHONE = u'phone'
    SIGN_NAME = u'sign_name'
    TEMPLATE_CODE = u'template_code'
    PARAMS = u'params'

    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__ or name in self.__class__.__dict__:
            raise self.ConstError("Unable to rebind const %s" % name)
        self.__dict__[name] = value

    def __init__(self):
        if not os.path.exists(os.path.dirname(self.LOG_FILE)):
            os.makedirs(os.path.dirname(self.LOG_FILE))
        if not os.path.exists(self.MSG_QUEUE_TEMPDIR):
            os.makedirs(self.MSG_QUEUE_TEMPDIR)
        logging.basicConfig(
            filename=self.LOG_FILE,
            format='%(asctime)s %(levelname)s %(name)s - %(message)s',
            level=logging.INFO)
        config = ConfigParser.SafeConfigParser()
        try:
            config.read(self.CONFIG_PATH)
        except ConfigParser.MissingSectionHeaderError:
            logging.error("[%s] session not existed in config file '%s'" %
                          (self.CONFIG_SESSION, self.CONFIG_PATH))

        self.SERVER_HOST = _config_get(
            config, self.CONFIG_SESSION, 'server_host', '0.0.0.0')

        self.SERVER_PORT = _config_get(
            config, self.CONFIG_SESSION, 'server_port', 50800)

        self.ACCESS_KEY_ID = _config_get(
            config, self.CONFIG_SESSION, 'access_key')

        self.ACCESS_KEY_SECRET = _config_get(
            config, self.CONFIG_SESSION, 'access_key_secret')


sys.modules[__name__] = _Config()

# vim: ts=4 sw=4 sts=4 et:
