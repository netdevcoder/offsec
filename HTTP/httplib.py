#!/usr/bin/python

import httplib

conn = httplib.HTTPConnection("web_server")
conn.putrequest("GET", "/", skip_host=True)
conn.putheader("Host", "web_server")
conn.endheaders()

res = conn.getresponse()
print res.read()

