# -*- encoding: utf-8 -*-

import json
import logging
import requests
import time

import const
from DataParser import DataParser
from threading import Thread
from pqueue import Queue as FifoDiskQueue

import sys
import uuid
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT


try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    pass
except Exception as err:
    raise err


class _MsgClient(object):
    def __init__(self):
        self._acs_client = AcsClient(const.ACCESS_KEY_ID, const.ACCESS_KEY_SECRET, const.REGION)
        self._smsRequest = SendSmsRequest.SendSmsRequest()
        region_provider.add_endpoint(const.PRODUCT_NAME, const.REGION, const.DOMAIN)
        self._data_queue = FifoDiskQueue(
            const.MSG_QUEUE_PATH, tempdir=const.MSG_QUEUE_TEMPDIR)
        worker = Thread(name='send_sms_alert', target=self._do_send)
        worker.daemon = True
        worker.start()

    def send(self, data):
        self._data_queue.put_nowait(json.dumps(data))

    @staticmethod
    def validate_config():
        if const.ACCESS_KEY_ID == "" or const.ACCESS_KEY_SECRET == "":
            raise ValueError(
                "Failed to get access_key or access_key_secret from: %s" % const.CONFIG_PATH)

    def _do_send(self):
        while True:
            try:
                data = json.loads(self._data_queue.get())
                normalized_data = DataParser.parse(data)
                if normalized_data is None:
                    logging.error("Failed to send sms alert, invalid data: %s" % data)
                    self._data_queue.task_done()
                    continue

                res = self.send_sms(normalized_data)
                logging.info("Succeeded to send sms alert, Response: %s" % res)
                self._data_queue.task_done()
            except:
                logging.exception("Unexpected exception.")

    def send_sms(self, normalized_data):
        self._smsRequest.set_TemplateCode(normalized_data.template_code)
        if normalized_data.template_param is not None:
            self._smsRequest.set_TemplateParam(normalized_data.template_param)

        business_id = uuid.uuid1()
        self._smsRequest.set_OutId(business_id)
        self._smsRequest.set_SignName(normalized_data.sign_name)
        self._smsRequest.set_method(MT.POST)
        self._smsRequest.set_accept_format(FT.JSON)
        self._smsRequest.set_PhoneNumbers(normalized_data.phone_numbers)
        smsResponse = self._acs_client.do_action_with_exception(self._smsRequest)
        return smsResponse


msg_client = _MsgClient()

# vim: ts=4 sw=4 sts=4 et:
