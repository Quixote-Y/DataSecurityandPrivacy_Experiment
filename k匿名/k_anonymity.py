import numpy
import pandas


def generalized(df):
    df_copy = df.drop(index=df.index)  # 复制相同dataframe并清空
    for label, content in df.items():
        arr = content.to_numpy()
        if content.dtype == 'object':
            if content.equals(df.iloc[:, -1]):  # 遇到最后一列，为敏感信息列，直接输出
                df_copy[label] = pandas.DataFrame(arr, columns=[label])
                return df_copy

            first_element = arr[0]
            if all(element == first_element for element in arr):
                arr = numpy.full_like(arr, first_element)
            else:
                arr = numpy.full_like(arr, '*')

        elif content.dtype == 'int64':
            if content.equals(df.iloc[:, -1]):  # 遇到最后一列，为敏感信息列，直接输出
                df_copy[label] = pandas.DataFrame(arr, columns=[label])
                return df_copy

            max_element = arr.max()
            min_element = arr.min()
            if max_element == min_element:
                arr = numpy.full_like(arr, max_element, dtype=object)
            else:
                arr = numpy.full_like(arr, f'{min_element}~{max_element}', dtype=object)

        df_copy[label] = pandas.DataFrame(arr, columns=[label])  # 将处理后的dataframe放入copy中


def k_anonymized(df, k):
    df_copy = df.drop(index=df.index)
    group = df.shape[0] / k  # 有几组
    while group > 0:
        df_opr = df.head(k)
        df_copy = pandas.concat([df_copy, generalized(df_opr)], ignore_index=True)
        df = df.tail(df.shape[0] - k)
        group -= 1
    return df_copy


