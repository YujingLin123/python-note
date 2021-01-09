#####拆开脚本如下：
f1 = pd.read_table("TF_background.bed",sep="\t",header=None)
f2 = pd.read_table("TF.bed",sep="\t",header=None)
df1 = pd.DataFrame(f1)
df2 = pd.DataFrame(f2)
df1.columns = ['chr','start','end']
df2.columns = ['chr','start','end']

d = pd.merge(df1,df2,on="chr")
d
"""
  chr  start_x  end_x  start_y  end_y
0   chr01        0    200        0    100
1   chr01        0    200      150    300
2   chr01        0    200      305    450
3   chr01      200    400        0    100
4   chr01      200    400      150    300
5   chr01      200    400      305    450
6   chr01      400    600        0    100
7   chr01      400    600      150    300
8   chr01      400    600      305    450
9   chr02        0    200        0    100
10  chr02        0    200      150    245
11  chr02        0    200      398    457
12  chr02      200    400        0    100
13  chr02      200    400      150    245
14  chr02      200    400      398    457
15  chr02      400    600        0    100
16  chr02      400    600      150    245
17  chr02      400    600      398    457
18  chr03        0    200        0    120
19  chr03        0    200      234    452
20  chr03        0    200      500    600
21  chr03      200    400        0    120
22  chr03      200    400      234    452
23  chr03      200    400      500    600
24  chr03      400    600        0    120
25  chr03      400    600      234    452
26  chr03      400    600      500    600
"""
##different condition
d0 = d[(d['start_y'] >= d['start_x']) & (d['start_y'] <= d['end_x']) & (d['end_y'] > d['end_x'])].drop_duplicates()
d0_overlap = (d0['end_x'] - d0['start_y'])/(d0['end_x']-d0['start_x'])
d0["Overlap"] = d0_overlap
"""
      chr  start_x  end_x  start_y  end_y  Overlap
1   chr01        0    200      150    300    0.250
5   chr01      200    400      305    450    0.475
10  chr02        0    200      150    245    0.250
14  chr02      200    400      398    457    0.010
22  chr03      200    400      234    452    0.830
"""
d1 = d[(d['start_y'] >= d['start_x']) & (d['start_y'] <= d['end_x']) & (d['end_y'] >= d['start_x']) & (d['end_y'] <= d['end_x'])].drop_duplicates()
d1_overlap = (d1['end_y']-d1['start_y'])/(d1['end_x']-d1['start_x'])
d1["Overlap"] = d1_overlap
"""
      chr  start_x  end_x  start_y  end_y  Overlap
0   chr01        0    200        0    100      0.5
9   chr02        0    200        0    100      0.5
18  chr03        0    200        0    120      0.6
26  chr03      400    600      500    600      0.5
"""
d2 = d[(d['end_y'] >= d['start_x']) & (d['start_y'] < d['start_x'])].drop_duplicates()
d2_overlap = (d2['end_y']-d2['start_x'])/(d2['end_x']-d2['start_x'])
d2["Overlap"] = d2_overlap
"""
      chr  start_x  end_x  start_y  end_y  Overlap
4   chr01      200    400      150    300    0.500
8   chr01      400    600      305    450    0.250
13  chr02      200    400      150    245    0.225
17  chr02      400    600      398    457    0.285
25  chr03      400    600      234    452    0.260
"""
##merge matrix
df = d1.append(d2)
df = d0.append(df)
"""
      chr  start_x  end_x  start_y  end_y  Overlap
1   chr01        0    200      150    300    0.250
5   chr01      200    400      305    450    0.475
10  chr02        0    200      150    245    0.250
14  chr02      200    400      398    457    0.010
22  chr03      200    400      234    452    0.830
0   chr01        0    200        0    100    0.500
9   chr02        0    200        0    100    0.500
18  chr03        0    200        0    120    0.600
26  chr03      400    600      500    600    0.500
4   chr01      200    400      150    300    0.500
8   chr01      400    600      305    450    0.250
13  chr02      200    400      150    245    0.225
17  chr02      400    600      398    457    0.285
25  chr03      400    600      234    452    0.260
"""
##group by similar background bin
df0 = df.groupby(by=['chr','start_x','end_x'])['Overlap'].sum().reset_index()

"""
     chr  start_x  end_x  Overlap
0  chr01        0    200    0.750
1  chr01      200    400    0.975
2  chr01      400    600    0.250
3  chr02        0    200    0.750
4  chr02      200    400    0.235
5  chr02      400    600    0.285
6  chr03        0    200    0.600
7  chr03      200    400    0.830
8  chr03      400    600    0.760
"""
