import pandas
import k_anonymity

if __name__ == '__main__':
    # dataset = pandas.read_csv('成绩关系型数据集.csv').drop(columns='姓名').drop(index=120)#读入数据存入dateset，删除地120行和地1列
    # k = int(input('请输入 k 值：'))
    # dataset_output = k_anonymity.k_anonymized(dataset, k)
    # dataset_output.to_csv('k 匿名成绩关系型数据集.csv', index=None)
    # print('数据生成成功！')

    dataset = pandas.read_csv('adult_data.csv')
    headers = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
    dataset.columns = headers
    k = int(input('请输入 k 值：'))
    dataset_output = k_anonymity.k_anonymized(dataset, k)
    dataset_output.to_csv('k_anonymized_adult_data.csv', index=None)
    print('数据生成成功！')
