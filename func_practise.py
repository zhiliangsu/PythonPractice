# 课堂习题：
# 1、输入5个字母，声明一个可变参数的函数，拼成一个单词
def word(*args, **kwargs):
    res = ''
    for arg in args:
        res += arg
    for kwarg in kwargs.values():
        res += kwarg
    return res

print(word('H', 'e', 'l', 'l', last='o'))


# 2、使用必填参数、默认参数、可变元组参数、可变字典参数，计算一下单词的长度之和
def word_length_count(first, second=None, *args, **kwargs):
    word_length = len(first) + len(second)
    for arg in args:
        word_length += len(arg)
    for kwarg in kwargs.values():
        word_length += len(kwarg)
    return word_length

print(word_length_count('first', 'second', 'third', fourth='fourth'))   


# 3、使用map方法把把[1,2,3]变为[2,3,4]
print(list(map(lambda x : x+1, [1, 2, 3])))


# 课后习题
# 1、成绩等级判断
# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# 60-89分之间用B来表示，60分以下的用C来表示
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 60 and score < 90:
        return 'B'
    else:
        return 'C'

print(grade(59))


# 2、将一句话的单词进行反转显示
def word_reverse_display(sentence):
    result_lists = []
    word_lists = sentence.split()
    for word in word_lists:
        # result_lists.append(''.join(reversed(word)))
        result_lists.insert(0, word[::-1])
        # result_lists.insert(0, ''.join(reversed(word)))

    # result_list = result_lists.reverse()
    return ' '.join(result_lists)

print(word_reverse_display('hello world man'))


# 3、统计一句话有多少个单词
def word_count(sentence):
    word_lists = sentence.split()
    return len(word_lists)

print(word_count('hello, everyone, my name is python.'))


# 4、输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
import re
def char_count(sentense):
    alpha_count = 0
    num_count = 0
    blank_count = 0
    others_count = 0
    for char in sentense:
        if re.match(r'[A-Za-z]', char):
            alpha_count += 1
        elif re.match(r'[0-9]', char):
            num_count += 1
        elif char == ' ':
            blank_count += 1
        else:
            others_count += 1
    return alpha_count, num_count, blank_count, others_count

print(char_count('HI-hello, my name is python. 112233'))


# 5、输出9*9口诀表
def multiple_table(n):
    for i in range(1, n+1):
        for j in range(1, i+1):    
            print('%d * %d = %d\t'%(j, i, i*j), end='')
        print()

multiple_table(9)


# 6、检查IPv4的有效性，有效则返回True，否则返回False
def check_ipv4(ip):
    results = ip.split('.')
    flag = True
    for result in results:
        if int(result) not in range(1, 256):
            flag = False
            break
    return flag

print('legal address:', check_ipv4('10.8.26.201'))
print('illegal address:', check_ipv4('10.8.26.261'))


# 7、检查IP连通性，有效则返回True，否则返回False
import os
def check_connection(ip):
    check_ipv4(ip)
    result = os.popen("ping " + ip + " -n 1").read()
    if "TTL" in result:
        return True
    else:
        return False

print('check connection:', check_connection('10.8.4.254'))
print('check connection:', check_connection('10.8.28.254'))


# 8、找出一段句子中最长的单词及其索引位置，以list返回
def find_word(sentence):
    result_lists = ['']
    length = 0
    word_lists = sentence.split()
    for word in word_lists:
        if len(word) > length:
            length = len(word)
            result_lists.pop()
            result_lists.append(word)
    result_lists.append(word_lists.index(result_lists[0]))
    return result_lists

print(find_word('HI-hello, my name is python. 112233445566'))


# 9、使用匿名函数求100以内偶数的和
print(sum(list(filter(lambda x : x % 2 == 0, list(range(100))))))


# 10、输出banana对应的颜色，且输出其上层key（fruit）对应的value
d = {
    "info":{
        "name":"zhangsan",
        "age":22,
        "fruit":{
            "peach":"red",
            "banana":"yellow"           
            }
        } 
    }
def color_output(dict):
    for info_dict in dict.values():
        for key in info_dict:
            if key == 'fruit':
                print("fruit's value:", info_dict[key])
                for k in info_dict[key]:
                    if k == 'banana':
                        print("banana's color:", info_dict[key][k])

color_output(d)