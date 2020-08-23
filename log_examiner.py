#!/usr/bin/env python3

import re, operator, os, csv

errors = {}
users = {}

error_pattern = r'ticky: ERROR ([\w\s\']*) \((.+)\)'
info_pattern = r'ticky: INFO.* \((.+)\)'

with open('syslog.log', 'r') as file:
  for line in file.readlines():
    if re.search(error_pattern, line):
      to_find = re.search(error_pattern, line)
      errors.setdefault(to_find.group(1), 0)
      errors[to_find.group(1)]+=1
      users.setdefault(to_find.group(2), [0,0])[1]+=1
    if re.search(info_pattern, line):
      to_find = re.search(info_pattern, line)
      users.setdefault(to_find.group(1), [0,0])[0]+=1
error_sorted = sorted(errors.items(), key = operator.itemgetter(1), reverse = True)
user_sorted = sorted(users.items(), key = operator.itemgetter(1), reverse=True)
print(error_sorted)
print(user_sorted)

with open('error_message.csv','w') as output:
  writer = csv.writer(output)
  writer.writerow(['Error','Count'])
  writer.writerows(error_sorted)

with open('user_statistics.csv','w') as output:
  writer = csv.writer(output)
  writer.writerow(['Username','INFO','ERROR'])
  for item in user_sorted:
      onerow = [item[0],item[1][0],item[1][1]]
      writer.writerow(onerow)

