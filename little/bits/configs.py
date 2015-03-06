import logging

__author__ = 'charlie'

#Auth
auth_key = "Bearer 57c2c4033382c94bf8a87930073cf49e3aaf0c25dc5acc4db7e549b540e9fba7"

#API endpoints
little_bits_base_url = "api-http.littlebitscloud.cc"
little_bits_post_url="/v2/devices/00e04c1e81b6/output"
little_bits_get_url = "v2/devices/"

#Registered devices
wake_me_device_id = "00e04c1e81b6" #TODO

#Output file for results
log_file = "little.bits.log"
logging_level = logging.DEBUG