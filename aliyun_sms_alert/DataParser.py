# -*- encoding: utf-8 -*-

import logging
import time
import json
import const

class DataParser(object):
    @classmethod
    def parse(cls, data):
        if not isinstance(data, dict):
            return None

        try:
            self = cls()
            self._phone_numbers = data[const.PHONE]
            self._sign_name = data[const.SIGN_NAME]
            self._template_code = data[const.TEMPLATE_CODE]
            self._template_param = json.dumps(data[const.PARAMS])

        except:
            logging.exception("Failed to create normalized data.")
            return None

        return self

    @property
    def phone_numbers(self):
        return self._phone_numbers

    @property
    def sign_name(self):
        return self._sign_name

    @property
    def template_code(self):
        return self._template_code

    @property
    def template_param(self):
        return self._template_param

# vim: ts=4 sw=4 sts=4 et:
