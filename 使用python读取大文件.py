# -*- coding: utf-8 -*-

with open(file_path, 'rb') as f:
    while True:
        line = f.readline()
        if buf:
            print(line)
        else:
            break

with open(file_path, 'rb') as f:
    for line in f:
        print(line)
