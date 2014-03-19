#!/usr/bin/python
# coding=utf-8

import csv
import fileinput
import json
import re

def utf_8_encoder(unicode_csv_data):
  for line in unicode_csv_data:
    yield line.encode('utf-8')

reader = csv.reader(utf_8_encoder(fileinput.input(openhook=fileinput.hook_encoded('utf-8'))))
reader.next()  # skip header

booths = []
cur_booth = None
last_booth_num = None

for line in reader:
  (booth_num, booth_name, food, price, notes, cat) = line
  if booth_num != last_booth_num:
    if cur_booth:
      booths += [cur_booth]
    cur_booth = { 'num': booth_num, 'name': booth_name, 'items': [] }
    last_booth_num = booth_num
  veg = 'Vegetarian' in notes
  ddp = 'DDP' in notes
  stein = '*' in notes
  cur_booth['items'] += [{
    'desc' : food,
    'price': price,
    'cat': cat,
    'veg': veg,
    'ddp': ddp,
    'stein': stein,
  }]
booths += [cur_booth]

print json.dumps(booths)
