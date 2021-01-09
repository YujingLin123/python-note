import pandas as pd
import numpy as np

f1 = pd.read_table("annotation.txt",sep="\t",header='infer')
df1 = pd.DataFrame(f1)

"""
#df1
         #pacId     locusName transcriptName  ... Best-hit-arabi-name arabi-symbol                                      arabi-defline
0      40123409  MD00G1000100   MD00G1000100  ...         AT5G55550.3          NaN    RNA-binding (RRM/RBD/RNP motifs) family protein
1      40123412  MD00G1000200   MD00G1000200  ...         AT5G45590.1          NaN                              Ribosomal protein L35
2      40123481  MD00G1000300   MD00G1000300  ...                 NaN          NaN                                                NaN
3      40123149  MD00G1000400   MD00G1000400  ...         AT1G47480.1          NaN          alpha/beta-Hydrolases superfamily protein
4      40123771  MD00G1000500   MD00G1000500  ...         AT5G45580.1          NaN               Homeodomain-like superfamily protein
...         ...           ...            ...  ...                 ...          ...                                                ...
45111  40125340  MD17G1287000   MD17G1287000  ...         AT1G73370.1  ATSUS6,SUS6                                 sucrose synthase 6
45112  40124216  MD17G1287300   MD17G1287300  ...         AT5G17240.1        SDG40                                SET domain group 40
45113  40124454  MD17G1287500   MD17G1287500  ...         AT1G65840.1  ATPAO4,PAO4                                polyamine oxidase 4
45114  40124551  MD17G1287600   MD17G1287600  ...         AT1G66120.1          NaN  AMP-dependent synthetase and ligase family pro...
45115  40125439  MD17G1287700   MD17G1287700  ...         AT5G52820.1          NaN  WD-40 repeat family protein / notchless protei...

"""
df1_GO = df1[['locusName','GO']].drop_duplicates()

"""
#df1_GO
          locusName                                           GO
0      MD00G1000100                                   GO:0003676
1      MD00G1000200  GO:0006412,GO:0005840,GO:0005622,GO:0003735
2      MD00G1000300                                          NaN
3      MD00G1000400                        GO:0016787,GO:0008152
4      MD00G1000500                                          NaN
...             ...                                          ...
45111  MD17G1287000                        GO:0016157,GO:0005985
45112  MD17G1287300                                   GO:0005515
45113  MD17G1287500                                          NaN
45114  MD17G1287600                        GO:0008152,GO:0003824
45115  MD17G1287700                                   GO:0005515
"""
split_columns = ['GO']
df1_convert = df1_GO.drop(columns=split_columns, axis=1)

"""
#df1_convert
          locusName
0      MD00G1000100
1      MD00G1000200
2      MD00G1000300
3      MD00G1000400
4      MD00G1000500
...             ...
45111  MD17G1287000
45112  MD17G1287300
45113  MD17G1287500
45114  MD17G1287600
45115  MD17G1287700

"""
for column in split_columns:
	df1_convert = df1_convert.join(df1_GO[column].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename(column))
	df1_convert = df1_convert.reset_index(drop=True)
	print(df1_convert)
  
 """
           locusName          GO
0      MD00G1000100  GO:0003676
1      MD00G1000200  GO:0006412
2      MD00G1000200  GO:0005840
3      MD00G1000200  GO:0005622
4      MD00G1000200  GO:0003735
...             ...         ...
75263  MD17G1287300  GO:0005515
75264  MD17G1287500         NaN
75265  MD17G1287600  GO:0008152
75266  MD17G1287600  GO:0003824
75267  MD17G1287700  GO:0005515
 """
