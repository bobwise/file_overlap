# python file_overlap.py /path/to/first/file/or/directory /path/to/second/file/or/directory '\$.*?(?=:)' out1.txt out2.txt both.txt .scss True

import sys
import os
import re

path1 = ''
path2 = ''

path1_out = ''
path2_out = ''
both_out = ''

regex = '\$.*?(?=:)'

extension = ''
skip_node_modules = True

def log(val):
    with open("log.txt", 'a') as f:
        f.write("%s\n" % val)

def output(array, filename):
    array.sort()

    with open(filename, 'w') as f:
        for item in array:
            f.write("%s\n" % item)

def searchPath(path, regex):
    found = []

    if os.path.isdir(path):
        for path, subdirs, files in os.walk(path):
            for filename in files:
                if not (len(extension) > 0 and not filename.lower().endswith(extension.lower())) and not (skip_node_modules is True and 'node_modules' in path):
                    for i, line in enumerate(open(os.path.join(path, filename))):
                        for matches in re.findall(regex, line):
                            if matches not in found:
                                found.append(matches)
    else:
        for i, line in enumerate(open(path)):
            for matches in re.findall(regex, line):
                if matches not in found:
                    found.append(matches)
        
    return found

if os.path.isfile("log.txt"):
    os.remove("log.txt")

if len(sys.argv) >= 2:
    path1 = sys.argv[1]

if len(sys.argv) >= 3:
    path2 = sys.argv[2]

if len(sys.argv) >= 4:
    regex = sys.argv[3]

if len(sys.argv) >= 5:
    path1_out = sys.argv[4]

if len(sys.argv) >= 6:
    path2_out = sys.argv[5]

if len(sys.argv) >= 7:
    both_out = sys.argv[6]

if len(sys.argv) >= 8:
    extension = sys.argv[7].lower()

if len(sys.argv) >=9:
    skip_node_modules = sys.argv[8] == 'True'

# TODO - validate args

tokens1 = searchPath(path1, regex)
tokens2 = searchPath(path2, regex)
tokens1.sort()
tokens2.sort()

both = []
tokens1_out = []
tokens2_out = []

for item in tokens1:
    if item in tokens2:
        both.append(item)
    else:
        tokens1_out.append(item)

for item in tokens2:
    if not item in both:
        tokens2_out.append(item)

output(tokens1_out, path1_out)
output(tokens2_out, path2_out)
output(both, both_out)