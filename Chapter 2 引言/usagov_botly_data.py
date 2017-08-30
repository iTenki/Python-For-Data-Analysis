import json
# 导入数据
path = '/Users/iTenki/Documents/GitHub/Python-For-Data-Analysis/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, encoding = 'utf8')]

# 对时区进行计数
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

# 对时区进行计数

'''
# 用函数，遍历数据，将其计数值保存在字典中
from get_counts_function import get_counts
from get_counts2_function import get_counts2
from top_counts_function import top_counts

counts_dict = get_counts(time_zoens)
print(top_counts(counts_dict))
'''

'''
# 用Python标准库 collections.Counter计数
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))
'''

# 用pandas对时区进行计数
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

frame = DataFrame(records)
# tz_counts = frame['tz'].value_counts()

'''
# 处理缺失值
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknow'
tz_counts = clean_tz.value_counts()
tz_counts[:10].plot(kind = 'barh', rot = 0)
'''

# 处理设备信息
result = Series([x.split()[0] for x in frame.a.dropna()])
result.value_counts()