import logging

"""
导入logger logger.info .warning .error 即可
"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s File "%(pathname)s", line %(lineno)d: %(message)s')
logger = logging.getLogger(name='main')


def wash_data(df):
    """箱型图法"""
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    mi = q1 - 1.5 * iqr
    ma = q3 + 1.5 * iqr
    # error = df[(df < mi) | (df > ma)]
    data_c = df[(df >= mi) & (df <= ma)]
    return data_c.interpolate().bfill()  # 线性插值
