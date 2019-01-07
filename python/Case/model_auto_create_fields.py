# coding: UTF-8
import re

''' ************************ 数据来源: ************************ '''
source_string = r'''
    id int primary key not null identity (1,1), -- exp:(记录ID) c#type:(int)

    UserSign nvarchar(max), -- exp:(用户标识) c#type:(string)
    UserIP nvarchar(max), -- exp:(用户IP) c#type:(string)
    PageAddress nvarchar(max), -- exp:(PageAddress) c#type:(string)
    DurationMS nvarchar(max), -- exp:(持续时长(毫秒)) c#type:(string)
    IsObsolete int, -- exp:(是否过时作废) c#type:(int)

    TimeAdd datetime, -- exp:(记录添加时间) c#type:(datetime)
    Remark nvarchar(max), -- exp:(记录备注) c#type:(string)
'''



''' ************************ 规则制定: ************************ '''
item_match_re_str = r'^\s*.*\s?as\s?(\w+)\,?\s?\-\-\s?exp\:\((.+)\)\s?c\#type\:\((.+)\)$'
item_match_re_str = r'^\s*(\w+)\s.+\,?\s?\-\-\s?exp\:\((.+)\)\s?c\#type\:\((.+)\)$'

def_data_type_rule = {
    'int': '0',
    'string': 'string.Empty',
    'DateTime': 'ERROR_DATETIME_VALUE',
    'double': '0.0'
}

sort_type_value_rule = {
    'int': 'number',
    'string': 'string',
    'DateTime': 'number',
    'double': 'number'
}

formatList = []
formatList.append(r'''
/// <summary>
/// {explain}
/// </summary>
public {datatype} {name} {{ get {{ return _{name}; }} set {{ _{name} = value; }} }}
private {datatype} _{name} = {deftypevalue};
''')
# formatList.append(r'''public readonly string ColName_{name} = ReflexHelper.Name(() => defModel.{name}); /* {explain} */''')
formatList.append(r'''public readonly string ColName_{name} = defDAL.ColName_{name}; /* {explain} */''')
# formatList.append(r'''<th width="auto" data-sort-type="{sorttypevalue}">{explain}</th>''')
# formatList.append(r'''<td><%#Eval("{name}")%></td>''')
# formatList.append(r'''{name} = DTRequest.GetString(@"{name}"),''')
# formatList.append(r'''@"{name}",''')













print('''\n\n************************ 计算的结果: ************************''')
re_model = re.compile(item_match_re_str, re.I | re.M | re.U)
result = re_model.findall(source_string)

def match_item(key, slist, defvalue):
    for x in slist:
        if x == key:
            return slist[x]
    return defvalue
def get_data_prototype(re_item_result):
    return {
        'datatype': item[2],
        'name': item[0],
        'explain': item[1],
        'deftypevalue': match_item(item[2], def_data_type_rule, '"ERROR"'),
        'sorttypevalue': match_item(item[2], sort_type_value_rule, 'string'),
    }

KVD_List = []
for item in result:
    KVD_List.append(get_data_prototype(item))
for stritem in formatList:
    for KVD in KVD_List:
        print(stritem.format(**KVD))
    print('\n[+] END', stritem, end='\n\n\n')


