
import pandas as pd
import numpy as np
import re

f1 = pd.read_table("gene.gff3",sep="\t",header=None)
df1 = pd.DataFrame(f1)
df1.columns = ['chr','Database','feature','start','end','label1','strand','label2','info']

##根据feature的列提取含有gene的字符串
df1_gene = df1[df1['feature'].str.contains('gene')]

####基因区域
df1_gene = df1_gene[['chr','start','end','strand']]

     chr  start    end strand
0  Chr15   5301   6082      +
4  Chr15   6173  10605      -

####正链基因上游
df1_UpGene = df1_gene[df1_gene['strand']=="+"]

df1_UpGene = df1_UpGene[df1_UpGene['start'] > 2000]
df1_UpGene['start_new'] = df1_UpGene['start'] - 2000 + 1

df1_UpGene = df1_UpGene.drop('end',axis=1)
df1_UpGene = df1_UpGene[['chr','start_new','start']]
df1_UpGene.columns = ['chr','start','end']

     chr  start   end
0  Chr15   3302  5301

####正链基因下游
df1_DownGene = df1_gene[df1_gene['strand']=="+"]

df1_DownGene['end_new'] = df1_DownGene['end'] + 2000

df1_DownGene = df1_DownGene.drop('start',axis=1)
df1_DownGene = df1_DownGene[['chr','end','end_new']]
df1_DownGene.columns = ['chr','start','end']

     chr  start   end
0  Chr15   6082  8082

####负链基因上游
df2_UpGene = df1_gene[df1_gene['strand']=="-"]

df2_UpGene['end_new'] = df2_UpGene['end'] + 2000

df2_UpGene = df2_UpGene.drop('start',axis=1)
df2_UpGene = df2_UpGene[['chr','end','end_new']]
df2_UpGene.columns = ['chr','start','end']

     chr  start    end
4  Chr15  10605  12605

####负链基因下游
df2_DownGene = df1_gene[df1_gene['strand']=="-"]

df2_DownGene = df2_DownGene[df2_DownGene['start'] > 2000]
df2_DownGene['start_new'] = df2_DownGene['start'] - 2000 + 1

df2_DownGene = df2_DownGene.drop('end',axis=1)
df2_DownGene = df2_DownGene[['chr','start_new','start']]
df2_DownGene.columns = ['chr','start','end']

     chr  start   end
4  Chr15   4174  6173


####合并上述的区域
##基因上游
dfup = df1_UpGene.append(df2_UpGene)

     chr  start    end
0  Chr15   3302   5301
4  Chr15  10605  12605

dfdown = df1_DownGene.append(df2_DownGene)

     chr  start   end
0  Chr15   6082  8082
4  Chr15   4174  6173


dfgene = df1_gene = df1_gene[['chr','start','end']]

     chr  start    end
0  Chr15   5301   6082
4  Chr15   6173  10605
