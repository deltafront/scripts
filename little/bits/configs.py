import logging

__author__ = 'charlie'

#Headers
accept_header = {"Accept": "application/vnd.littlebits.v2+json"}
content_header = {"Content-Type": "application/json"}
auth_header = {"Authorization": "Bearer "}#TODO

#API endpoints
little_bits_base_url = "http://api-http.littlebitscloud.cc/v2/"
little_bits_post_url="devices/%s/output"
little_bits_get_url = "http://api-http.littlebitscloud.cc/v2/devices/"

#Registered devices
wake_me_device_id = "" #TODO

#Output file for results
log_file = "little.bits.log"
logging_level = logging.DEBUG