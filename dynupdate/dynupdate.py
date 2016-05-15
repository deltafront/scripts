import datetime
import hashlib
import httplib
import urllib
from configs import user_auth_header_name, pass_value, auth_salt, timestamp_header_name, user_value, site_name
from configs import update_host, update_path, update_port, logging_file_name, logging_level, pass_auth_header_name
import logging
__author__ = 'charlie'

logging.basicConfig(filename=logging_file_name, level=logging_level)


def send_request():
    headers = construct_headers()
    body = urllib.urlencode({"site_name": site_name})
    connection = httplib.HTTPConnection(update_host, update_port)
    connection.request("PUT", update_path, body, headers)
    response = connection.getresponse()
    logging.info("URL: %s:%s/%s" % (update_host, update_port, update_path))
    header_message = ""
    for key in headers.iteritems():
        header_message += "%s=%s" % (key, headers[key])
    logging.debug(header_message)
    logging.info("%s (%s0" % (response.status, response.msg))


def construct_headers():
    timestamp = str(datetime.datetime.now())
    password = get_password(timestamp)
    body_len = len(site_name)
    return {user_auth_header_name: user_value, timestamp_header_name: timestamp, pass_auth_header_name: password,"CONTENT-LENGTH":str(body_len)}


def get_password(timestamp):
    pre_hash = "%s%s%s%s" % (auth_salt, pass_value, user_value, str(timestamp))
    return hashlib.md5(pre_hash).hexdigest

