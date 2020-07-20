import requests
import json
import sys


def get_text(url):
    response = requests.get(url)

    with open('ribatext.txt', 'w') as fh:
        fh.write(response.text)


def char_counter():
    text = sys.argv[1]
    lines = 0
    spaces = 0
    letters = 0
    # avg_len = []

    for line in open(text):
        lines += 1
        letters += len(line)
        # avg_len.append(line)

        for letter in line:
            if letter == ' ':
                spaces += 1
            else:
                pass
    print("lines count: ", lines)
    print("spaces count: ", spaces)
    print("letters or symbols: ", letters)
    print("Average lines len is: ", round(letters / lines, 0))

    return lines, spaces, round(letters / lines, 0)


def json_writer():
    data = char_counter()
    record = json.dumps(data)
    with open('text_saver.json', 'w') as fh:
        fh.write(record)
    return 0


get_text(sys.argv[2])
# char_counter()
json_writer()
#

# 'https://code.google.com/archive/p/pypsum/'

# python  Lesson_8.py ribatext.txt https://code.google.com/archive/p/pypsum/
