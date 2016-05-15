import httplib
import urllib
from little.bits import log
from little.bits.configs import little_bits_post_url, little_bits_base_url, little_bits_get_url, auth_key

__author__ = 'charlie'

base = little_bits_base_url
headers = {
    "Accept": "application/vnd.littlebits.v2+json",
    "Content-Type": "application/json",
    "Authorization": auth_key
}


def do_post(device_id, percent, duration_ms):
    json = '{"percent:%s,"duration_ms":%s}' % (percent, duration_ms)
    params = json
    endpoint = little_bits_post_url.replace("{id}", device_id)
    log.log("POST Request:\nUrl:\t%s%s\nPercent / Duration\t%s/%s \nHeaders:\t%s" % (
        base, endpoint, str(percent), str(duration_ms), str(headers)))
    return connect(endpoint, "POST", params)


def do_get():
    endpoint = little_bits_get_url
    log.log("GET Request:\nUrl:\t%s%s\nHeaders:\t%s" % (base, endpoint, str(headers)))
    return connect(endpoint, "GET", None)


def connect(endpoint, method, params):
    log.log("Request [method=%s]:\nUrl:\t%s%s\tParams:\t%s\nHeaders:\t%s" % (method,base, endpoint,str(params), str(headers)))
    conn = httplib.HTTPConnection(host=base)
    if params is not None:
        conn.request(method=method, url=endpoint, body=params, headers=headers)
    else:
        conn.request(method=method, url=endpoint, headers=headers)
    response = conn.getresponse()
    out = response.read()
    log.log("Response:\n%s\t[%s]" % (out, str(response.status)))
    conn.close()
    return out
