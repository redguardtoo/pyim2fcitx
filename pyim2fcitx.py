#!/usr/bin/env python
import sys
import re
import getopt


def usage():
    print("Usage:")
    print("  python pyim2fcitx.py [-f 5] my-dict.pyim\n")
    print("  -f: fcitx version whose default value is 4 \n")
    print("  Visit https://github.com/tumashu/pyim to get pyim dictionaries")


if __name__ == "__main__":
    all_args = sys.argv[1:]
    opts, arg = getopt.getopt(all_args, 'f:')
    fcitx_version = 4

    if len(arg) < 1:
        usage()
        exit(1)

    for opt, arg_val in opts:
        if opt == "-f" and int(arg_val) > fcitx_version:
            fcitx_version = int(arg_val)
    rd = open(arg[0], "r")
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
                    if fcitx_version == 5:
                        print("%s %s 0" % (word, pinyin))
                    else:
                        print("%s %s" % (pinyin, word))
            else:
                if fcitx_version == 5:
                    pinyin_and_word = line.replace("-", "'").split()
                    # first is pinyin, second is word
                    print("%s %s 0" % (pinyin_and_word[1], pinyin_and_word[0]))
                else:
                    print(line.replace("-", "'"))
