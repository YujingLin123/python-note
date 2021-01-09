split（）正序分割列；rsplit（）逆序分割列
Series.str.split(pat=None, n=-1, expand=False)
参数:
pat : 字符串,默认使用空白分割.
n : 整型,默认为-1,既使用所有的分割点分割
expand : 布尔值,默认为False.如果为真返回数据框(DataFrame)或复杂索引(MultiIndex);如果为假,返回序列(Series)或者索引(Index).
return_type : 弃用,使用spand参数代替
返回值:
split : 参考expand参数
