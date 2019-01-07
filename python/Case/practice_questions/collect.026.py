# coding: UTF-8

print(r'''
【程序26】题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续 判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
''')

# Stupid approach:
def old_JudgingTheWeek(week_str):
    week_str = str(week_str).lower()
    if week_str[0] == 'M'.lower():
        return '星期一'
    if week_str[0] == 'T'.lower():
        if week_str[1] == 'u'.lower():
            return '星期二'
        elif week_str[1] == 'h'.lower():
            return '星期四'
    if week_str[0] == 'W'.lower():
        return '星期三'
    if week_str[0] == 'F'.lower():
        return '星期五'
    if week_str[0] == 'S'.lower():
        if week_str[1] == 'a'.lower():
            return '星期六'
        elif week_str[1] == 'u'.lower():
            return '星期天'
    return '错误参数: ' + week_str

def new_JudgingTheWeek(week_str):
    week_str = str(week_str).lower()
    rule_list = [
        ['星期一', 'M', ],
        ['星期二', 'T', 'u'],
        ['星期三', 'W' ],
        ['星期四', 'T', 'h'],
        ['星期五', 'F', ],
        ['星期六', 'S', 'a'],
        ['星期天', 'S', 'u'],
    ]
    for item in rule_list:
        if week_str[0] == item[1].lower():
            if len(week_str) <= 1:
                continue
            if len(item) <= 2 or week_str[1] == item[2].lower():
                return item[0]
    return '错误参数: ' + week_str

week_str_list = [
    't',
    'th',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
    'EFlieja',
]
for week_str in week_str_list:
    result_str = new_JudgingTheWeek(week_str)
    print(week_str, '结果: ', result_str)
