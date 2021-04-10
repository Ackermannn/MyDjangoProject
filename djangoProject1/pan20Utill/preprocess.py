"""
预处理数据

来源 xlsx文件
输出xlsx文件

需要 csv指标排序

使用 前观察xlsx是否有  proc_time  collect_name 等 列名
"""
import os

import pandas as pd
from .utills import wash_data
current_dir = os.path.dirname(__file__)
os.path.join(current_dir, 'data/index_name_sorted.csv')
sortTable = pd.read_csv(os.path.join(current_dir, 'data/index_name_sorted.csv'))


def preprocessCSV(inputFile, outputFile):
    df = pd.read_csv(inputFile)
    ret = preprocess(df)
    ret.to_csv(outputFile)


def preprocessExcel(inputFile, outputFile):
    df = pd.read_excel(inputFile, engine='openpyxl')
    ret = preprocess(df)
    ret.to_excel(outputFile)


def preprocess(df):
    """
    step 1. 去重
    step 2. 旋转
    step 3. 格式化
    step 4. 指标排序、日期排序
    step 5. 检查空值
    step 6. 异常分析与缺失处理

    # :param inputFile:
    # :param outputFile:
    :return:
    """
    # df = pd.read_excel(inputFile, engine='openpyxl')
    df = df.drop_duplicates(subset=['proc_time', 'collect_name'])  # 去除重复
    pivoted = pd.pivot(df, values='collect_value', columns='collect_name', index='proc_time')  # 旋转
    pivoted.index = pd.to_datetime(pivoted.index)
    pivoted.sort_index(inplace=True)
    pivoted = pivoted[sortTable['name']]  # 抽出来255指标

    if not (pivoted.count() == pivoted.shape[0]).all():
        raise Exception("有空值！！")

    pivoted = wash_data(pivoted)  # 箱型图去除异常
    # pivoted.to_excel(outputFile)

    return pivoted


if __name__ == '__main__':
    inputFiles = [
        "data/0200_d-01-03.csv",
        "data/0200_h-01-03.csv",
        "data/0200_t-01-03.csv",
                  ]
    outputFiles = [
        "data/pivoted0200_d-01-03.csv",
        "data/pivoted0200_h-01-03.csv",
        "data/pivoted0200_t-01-03.csv",
                  ]
    for i in range(3):
        preprocessCSV(inputFiles[i], outputFiles[i])
    # test
    # df = pd.read_excel('data/xw_bf2_0200_d.xlsx', engine='openpyxl')
    # df = df.drop_duplicates(subset=['proc_time', 'collect_name'])  # 去除重复
    # pivoted = df.pivot(values='collect_value', columns='collect_name', index='proc_time')  # 旋转
