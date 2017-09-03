import requests
import argparse
import re
from getpass import getpass

parser = argparse.ArgumentParser(description='Set ES Cluster Restart Settings')
parser.add_argument("es", help="ES host:port")
parser.add_argument("action", help="start or stop")
parser.add_argument("-s", "--ssl", action='store_true', help="Requires SSL")
parser.add_argument("-a", "--auth", action='store_true', help="Basic Auth")
parser.add_argument("-n", "--name", help="Template Name")

headers = {'Content-Type': 'application/json'}

args = parser.parse_args()
uname = ''
upass = ''

if args.auth:
   print "Enter Username: "
   uname = raw_input()
   print "Enter Password: "
   upass = getpass()

if args.ssl:
   host = "https://"+args.es
else:
   host = "http://"+args.es

if args.action == "stop":
   data = '{ "persistent": { "cluster.routing.allocation.enable": "none" } }'
   setting = host+"/_cluster/settings"
   r = requests.put(setting, headers=headers, data=data, verify=False, auth=(uname, upass))
   print "Routing disable: \n" + r.text
   setting = host+"/_flush/synced"
   r = requests.post(setting, headers=headers, data=data, verify=False, auth=(uname, upass))
   print "Sync Flush: \n" + r.text

if args.action == "start":
   data = '{ "persistent": { "cluster.routing.allocation.enable": "none" } }'
   setting = host+"/_cluster/settings"
   r = requests.put(setting, headers=headers, data=data, verify=False, auth=(uname, upass))
   print "Routing enabled: \n" + r.text
