import main
import io
import sys
import re
import math


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '35 5 10 20 40 15\n'
    sys.stdin = io.StringIO(datastr)

    main.main()
    number = [35, 5, 10, 20, 40, 15]
    main.split(number)
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert number[0] <= 15
    assert number[1] <= 15
    assert number[2] == 15
    assert number[3] >= 15
    assert number[4] >= 15
    assert number[5] >= 15
