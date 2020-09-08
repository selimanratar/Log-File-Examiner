#!/usr/bin/env python3

import re, operator, os, csv

errors = {}
users = {}


#Creating the regular expressions to look for in the file
error_pattern = r'ticky: ERROR ([\w\s\']*) \((.+)\)'
info_pattern = r'ticky: INFO.* \((.+)\)'


# MacOS update. Since it is system.log for Mac and syslog.log for Linux and some other names for various Linux distributions, using
# an input would allow the script to work in different OSs.
os_name = input("What is your OS?")


if os_name == "MacOS":
  osdependent_log = "system.log"
elif os_name == "Linux"
  os_dependent_log = "syslog.log"

else:
  print("This script can only work for Linux or MacOS")

#Opening and searching the system log file for user activity and error messages

with open(os_dependent_log, 'r') as file:
  for line in file.readlines():
    if re.search(error_pattern, line):
      to_find = re.search(error_pattern, line)
      errors.setdefault(to_find.group(1), 0)
      errors[to_find.group(1)]+=1
      users.setdefault(to_find.group(2), [0,0])[1]+=1
    if re.search(info_pattern, line):
      to_find = re.search(info_pattern, line)
      users.setdefault(to_find.group(1), [0,0])[0]+=1

# Sorting the findings to find the most common errors and most active users      
error_sorted = sorted(errors.items(), key = operator.itemgetter(1), reverse = True)
user_sorted = sorted(users.items(), key = operator.itemgetter(1), reverse=True)
print(error_sorted)
print(user_sorted)

#Writing the error results to a .csv file
with open('error_message.csv','w') as output:
  writer = csv.writer(output)
  writer.writerow(['Error','Count'])
  writer.writerows(error_sorted)

  
#Writing the user results to a .csv file
with open('user_statistics.csv','w') as output:
  writer = csv.writer(output)
  writer.writerow(['Username','INFO','ERROR'])
  for item in user_sorted:
      onerow = [item[0],item[1][0],item[1][1]]
      writer.writerow(onerow)

