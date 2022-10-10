# -*- coding: utf-8 -*-
# --------------------
# code by Fgaoxing
# Github: https://github.com/Fgaoxing/find-same-file
# Version 1.0
# Please observe MIT agreement
#  --------------------
# Call print_ same(path)
# Path is the path, followed by the folder/
# The returned dictionary format can be directly traversed
# --------------------

import os
import sys
import hashlib


def process_bar(percent, start_str='', end_str='', total_length=0):  # progress bar
    bar = '' + '\033[93m\u2588\033[0m' * int(percent * total_length) + ''
    if percent != 1:
        bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent * 100) + end_str
    else:
        bar = '\r' + start_str + '\033[92m\u2713\033[0m ' + end_str + '\n'
    print(bar, end='', flush=True)


def traverse_files(path):  # Traverse files
    Flists = []
    try:
        os.listdir(path)
    except PermissionError:
        return Flists
    except FileNotFoundError:
        return Flists
    for file in os.listdir(path):
        if os.access(path + '/' + file, os.R_OK):
            if os.path.isfile(path + '/' + file):
                if os.access(path + '/' + file, os.R_OK) and not 'desktop.ini' in file:
                    Flists.append(path + '/' + file)
            else:
                Flists = Flists + traverse_files(path + '/' + file)
    return Flists


def f2md5(Lpath):  # Calculate md5
    a = []
    for f in Lpath:
        try:
            process_bar((len(a) + 1) / len(Lpath), start_str='Calculate MD5|',
                        end_str='100% ' + str(len(a) + 1) + '/' + str(len(Lpath)), total_length=15)
            fp = open(f, 'rb')
            data = fp.read()
            a.append(hashlib.md5(data).hexdigest())
            if len(a) >= len(Lpath):
                return a
        except PermissionError:
            a.append('error')
            continue
        except FileNotFoundError:
            a.append('error')
            continue


def find_same(list, Flists):  # find same files
    a = {}
    b = {}
    for i in range(len(list)):
        process_bar((i + 1) / len(list), start_str='Data merging|',
                    end_str='100% ' + str(i + 1) + '/' + str(len(list)), total_length=15)
        if not list[i] in a:
            a[list[i]] = []
        a[list[i]].append(Flists[i])
    a['error'] = []
    jisu = 0
    for key, value in a.items():
        process_bar((jisu + 1) / len(a), start_str='Find Duplicates|',
                    end_str='100% ' + str(jisu + 1) + '/' + str(len(a)), total_length=15)
        if len(value) > 1:
            b[key] = value
        jisu += 1
    return b


def print_same(path):  # print file list
    print('Traversing... There are many files and the speed is slow. Please wait patiently!')
    a = traverse_files(path)
    return find_same(f2md5(a), a)


if __name__ == '__main__':
    print_same('.')
