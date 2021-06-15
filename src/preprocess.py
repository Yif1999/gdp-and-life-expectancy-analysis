from numpy.lib.function_base import kaiser
import pandas as pd

#定义函数用于将数据中包含的k、M等字符计算为数值
def str2num(x):
  x=str(x)
  if 'k' in x:
    return eval(x.replace('k','*1000'))
  elif 'M' in x:
    return eval(x.replace('M','*1000000'))
  elif 'B' in x:
    return eval(x.replace('B','*1000000000'))
  else:
    return eval(x)

#多数据表数据融合方法
def fusion(path,i,le,p):
  indata=pd.read_excel(path+i) #读入收入数据Excel文件
  lidata=indata.melt(
    id_vars="country",  #设置行索引
    var_name="year",  #设置列索引
    value_name="income" #设置值
  ) #转为长数据
  lidata=lidata[lidata["year"]>=2005];lidata=lidata[lidata["year"]<=2019] #筛选指定年份间的数据
  lidata["income"]=lidata["income"].transform(str2num)  #数据中的k、M转为对应数值

  ledata=pd.read_excel(path+le) #读入期望寿命数据Excel文件
  lledata=ledata.melt(
    id_vars="country",  #设置行索引
    var_name="year",  #设置列索引
    value_name="life_exp" #设置值
  ) #转为长数据
  lledata=lledata[lledata["year"]>=2005];lledata=lledata[lledata["year"]<=2019]  #筛选指定年份间的数据

  pdata=pd.read_excel(path+p) #读入人口数据Excel文件
  lpdata=pdata.melt(
    id_vars="country",  #设置行索引
    var_name="year",  #设置列索引
    value_name="pop" #设置值
  ) #转为长数据
  lpdata=lpdata[lpdata["year"]>=2005];lpdata=lpdata[lpdata["year"]<=2019]  #筛选指定年份间的数据
  lpdata["pop"]=lpdata["pop"].transform(str2num)  #数据中的k、M转为对应数值

  income_life=pd.merge(lidata,lledata,left_on=["year","country"],right_on=["year","country"],how="inner") #将收入与期望寿命对应数据融合
  income_life_pop=pd.merge(income_life,lpdata,left_on=["year","country"],right_on=["year","country"],how="inner")  #继续将人口数据合入

  return(income_life_pop)