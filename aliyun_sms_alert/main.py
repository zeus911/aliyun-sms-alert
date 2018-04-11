# -*- encoding: utf-8 -*-

import logging
import sys
import uuid

from bottle import (post, run, request, error,
                    HTTPError, HTTPResponse, default_app)

import const
import json
from msg_client import msg_client


@post(const.SEND_ALERT_URI)
def send_alert():
    try:
        msg_client.send(request.json)
        return HTTPResponse(status=200)
    except:
        logging.exception("Failed to send alert: %s" % request.json)
        return HTTPError(500)


@error(404)
@error(405)
def ignore_error_page(code):
    pass


def main():
    try:
        msg_client.validate_config()
        run(host=const.SERVER_HOST,
            port=const.SERVER_PORT)
    except:
        logging.exception("Failed to start sms-alert service at %s:%s" %
                          (const.SERVER_HOST, const.SERVER_PORT))
        sys.exit(1)


if __debug__:
    application = default_app()

# vim: ts=4 sw=4 sts=4 et:
