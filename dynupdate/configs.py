import datetime
import logging

__author__ = 'charlie'

update_host = ""
update_port = 80
update_path= ""
user_auth_header_name = "CG-AUTH-USER"
user_value = "CompanyB"
pass_auth_header_name = "CG-AUTH-PASS"
pass_value = "Gab0ll!S3attl3"
auth_salt = "Ax!a!969"
timestamp_header_name = "CG-TIMESTAMP-HEADER"
logging_file_name = "" % datetime.datetime.now().strftime("")
logging_level = logging.DEBUG
site_name = "CompanyB Raspberry Pi"