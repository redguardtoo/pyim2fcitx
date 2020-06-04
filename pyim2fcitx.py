#!/usr/bin/env python

import sys
import re


def usage():
    print("Usage:")
    print("  python pyim2fcitx.py my-dict.pyim\n")
    print("  Visit https://github.com/tumashu/pyim to get pyim dictionaries")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(1)

    rd = open(sys.argv[1], "r")
    while True:
        line = rd.readline()

        if not line:
            break
        # strip new line
        line = line.strip()

        # fcitx tools can't handle unusual pinyin
        if re.search("^[a-z-]+ ", line):
            # multiple words in one line
            m = re.search("^([a-z-.]+) ([^ ]+ [^ ]+.*)$", line)
            if m:
                pinyin = m.group(1).replace("-", "'")
                words = m.group(2).split()
                for word in words:
                    print("%s %s" % (pinyin, word))
            else:
                print(line.replace("-", "'"))
