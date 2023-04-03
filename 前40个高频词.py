
# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词


# 读取文件
fn = open('气象灾害具体内容.txt',encoding='utf-8') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, ' ', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data) # 精确模式分词
object_list = []
remove_words = open('stopwords.txt',encoding='utf-8').read()

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top40 = word_counts.most_common(40) # 获取前40最高频的词
print (word_counts_top40) # 输出检查


