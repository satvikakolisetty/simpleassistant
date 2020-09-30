#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

x = cgi.FieldStorage()

osname=x.getvalue("name")
imgname=x.getvalue("imgname")


cmd = " sudo docker run -dit --name {} {}".format(osname,imgname)
output = sp.getstatusoutput( cmd)

status = output[0]
ans = output[1]

if status == 0:
   print("os launched named {} using image {}".format(osname,imgname))
else:
   print("some error ; {}".format(ans))


