# ~/anaconda2/bin/python
# coding:utf-8

import sys
from gensim import corpora, models
import data_preprocessing_util

reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == '__main__':
    # 列表，其中每个元素也是一个列表，即每行文字分词后形成的词语列表
    word_list = data_preprocessing_util.return_useful_words_list()

    # 生成文档的词典，每个词与一个整型索引值对应
    word_dict = corpora.Dictionary(word_list)

    # 词频统计，转化成空间向量格式
    corpus_list = [word_dict.doc2bow(text) for text in word_list]
    lda = models.ldamodel.LdaModel(corpus=corpus_list, id2word=word_dict, num_topics=8, alpha='auto')

    for pattern in lda.show_topics():
        print 'topic', pattern[0], str(pattern[1])