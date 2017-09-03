import requests
import argparse
import re
from getpass import getpass

parser = argparse.ArgumentParser(description='Set ES Index Shards')
parser.add_argument("es", help="ES host:port")
parser.add_argument("index", help="Index name (logstash-*")
parser.add_argument("shards", help="Number of shards")
parser.add_argument("-s", "--ssl", action='store_true', help="Requires SSL")
parser.add_argument("-a", "--auth", action='store_true', help="Basic Auth")
parser.add_argument("-n", "--name", help="Template Name")

args = parser.parse_args()
uname = ''
upass = ''

if args.auth:
   print "Enter Username: "
   uname = raw_input()
   print "Enter Password: "
   upass = getpass()

if args.name is None:
   template_name = re.sub('[*-]','',args.index)
else:
   template_name = args.name

if args.ssl:
   host = "https://"+args.es+"/_template/"+template_name+"?pretty"
else:
   host = "http://"+args.es+"/_template/"+template_name+"?pretty"

print host

template = '{"template": "'+args.index+'","settings": { "number_of_shards": '+args.shards+'}}'
headers = {'Content-Type': 'application/json'}

r = requests.put(host, headers=headers, data=template, verify=False, auth=(uname, upass))

print r.text
