#!/usr/bin/python
# coding=utf-8

import fileinput
import re

booth = None

for line in fileinput.input(openhook=fileinput.hook_encoded('utf-8')):
  if 'Introduced' in line:
    booth = re.findall('(.*), Introduced', line)[0]
    continue
  if line == '\n':
    continue
  parts = re.findall(u'(.*?) [-–—] (\$[0-9$.–— -]*),?(.*)', line)[0]
  price = parts[1].strip()
  if price == '$0.00':
    price = ''
  out = '%s,"%s",%s,"%s"' % (booth, parts[0].strip(), price, parts[2].strip())
  print out.encode('utf-8')

