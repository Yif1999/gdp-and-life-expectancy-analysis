import os
from plotly.offline import  plot
import pandas as pd
import plotly.express as px
import preprocess

path = os.path.dirname(os.path.abspath(__file__)) #获取src路径
data_path=path+"/../data/" #设定数据源路径
os.chdir(path+"/../out/")  #设定输出路径

data=px.data.gapminder()[["country","continent"]] #获取洲数据源
data=data.drop_duplicates(subset=["country","continent"],keep="first")  #删除重复行
fusion_data=preprocess.fusion(data_path,
                              "income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx",
                              "life_expectancy_years.xlsx",
                              "population_total.xlsx") #传入文件路径并返回多数据表融合后的结果
result=pd.merge(fusion_data,data,left_on="country",right_on="country",how="left")  #数据融合

result.to_excel("人均GDP和人均寿命2005-2019.xlsx")  #输出结果的Excel文件
dataset=result.dropna()  #删除NA值
fig = px.scatter(dataset, x="income", y="life_exp", animation_frame="year",
                 animation_group="country",size="income", color="continent",
                 hover_name="country",log_x=True, size_max=45,
                 range_x=[500,200000], range_y=[25,90],
                 labels=dict(income="人均收入(PPP购买力标准)",life_exp="人均寿命"))  #设置图片参数
plot(fig) #绘图输出html动画网页