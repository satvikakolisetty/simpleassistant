#!/usr/bin/python3

print("content-type: text/html")
print()

import os
import subprocess as sp
import cgi
field = cgi.FieldStorage()
value=field.getvalue('x')
output=sp.getstatusoutput("sudo " + value)
status=output[0]
ans=output[1]

if status == 0:
   print(ans)
else:
   print("pl.. check errors in {}".format(ans))
