import httplib
import urllib
from little.bits import log
from little.bits.configs import accept_header, content_header, auth_header, little_bits_post_url, little_bits_base_url, little_bits_get_url

__author__ = 'charlie'

base = little_bits_base_url
headers = dict()
headers.update(accept_header)
headers.update(content_header)
headers.update(auth_header)


def do_post(device_id, percent, duration_ms):
    json = '{"percent:"%s","duration_ms":"%s"}' % (percent, duration_ms)
    params = urllib.urlencode(json)
    endpoint = little_bits_post_url % device_id
    log.log("Url:\t%s%s\nPercent / Duration\t%s/%s \nHeaders:\t%s" % (base, endpoint, str(percent), str(duration_ms), str(headers)))
    connect(endpoint, "POST", params)


def do_get():
    endpoint = little_bits_get_url
    log.log("Url:\t%s%s\nHeaders:\t%s" % (base, endpoint, str(headers)))
    connect(endpoint, "GET", None)


def connect(endpoint, method, params):
    conn = httplib.HTTPConnection(base)
    conn.request(method, endpoint, params, headers)
    response = conn.getresponse()
    log.log("Response:\n%s\t[%s]" % (response.msg, str(response.status)))
