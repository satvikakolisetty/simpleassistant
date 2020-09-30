#!/usr/bin/python3

print("content-type: text/html")
print()

import os
import subprocess as sp
import cgi
field = cgi.FieldStorage()
value=field.getvalue('stop')
#cmd = "sudo docker stop {}".format(stop)
output=sp.getstatusoutput("sudo docker stop " + value)
status=output[0]
ans=output[1]
if status == 0:
   print("container stopped")
   print(ans)
else:
   print("pl.. check errors in {}".format(ans))
