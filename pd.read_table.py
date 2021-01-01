pandas.read_table(filepath_or_buffer,sep='\t',delimiter=None,
                  header='infer',names=None,index_col=None,usecols=None,squeeze=False,
                  prefix=None,mangle_dupe_cols=True,dtype=None,engine=None,converters=None,
                  true_values=None,false_values=None,skipinitialspace=False,skiprows=None,
                  nrows=None,na_values=None,keep_default_na=True,na_filter=True,verbose=False,
                  skip_blank_lines=True,parse_dates=False,infer_datetime_format=False,
                  keep_date_col=False,date_parser=None,dayfirst=False,iterator=False,
                  chunksize=None,compression='infer',thousands=None,decimal=b'.',lineterminator=None,
                  quotechar='"',quoting=0,escapechar=None,comment=None,encoding=None,dialect=None,
                  tupleize_cols=None,error_bad_lines=True,warn_bad_lines=True,skipfooter=0,
                  doublequote=True,delim_whitespace=False,low_memory=True,memory_map=False,
                  float_precision=None)
                  
#filepath_or_buffer   第一个参数,把文件地址传入即可;
#engine='python'      默认是c引擎解析,如果使用python引擎,可以解析更丰富的内容;
#header='infer'       默认会自动推断数据文件头,如果设置为None则无文件头,为1则第一行是文件头;
#sep='\t'             默认是由tab分割的数据,如果是其他可以另改,比如','
