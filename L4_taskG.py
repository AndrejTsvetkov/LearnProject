import re
from decimal import *


def is_correct_format(string):
    pattern = "[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
    if string.startswith("rgba"):
        list = re.findall(r'\(.*\)', string)
        m_str = list[0].strip('()')
        m_list = m_str.split(',')
        if len(m_list) == 4:
            if all(bool(re.search(pattern, element)) and 0.0 <= Decimal(element) <= 255.0 for element in m_list[:-1]):
                if bool(re.search(pattern, m_list[-1])) and 0.0 <= Decimal(m_list[-1]) <= 1.0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif string.startswith("rgb"):
        list = re.findall(r'\(.*\)', string)
        m_str = list[0].strip('()')
        m_list = m_str.split(',')
        if len(m_list) == 3:
            if all(element.endswith('%') for element in m_list):
                if all(bool(re.search(pattern, element.rstrip('%'))) and 0.0 <= Decimal(element.rstrip('%')) <= 100.0 for element in m_list):
                    return True
                else:
                    return False
            else:
                if all(bool(re.search(pattern, element)) and 0.0 <= Decimal(element) <= 255.0 for element in m_list):
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False



test1 = "rgb(0%,50%,100%)"
test2 = "rgba(0,0,0,0)"
test3 = "rgb(255,255,255)"
test4 = "rgb(0,,0)"
test5 = "rgb(-1,0,0)"
test6 = "rgba(0,0,0,1.5)"
test7 = "rgba(0,0,0,0.5)"

print(is_correct_format(test1))
print(is_correct_format(test2))
print(is_correct_format(test3))
print(is_correct_format(test4))
print(is_correct_format(test5))
print(is_correct_format(test6))
print(is_correct_format(test7))
