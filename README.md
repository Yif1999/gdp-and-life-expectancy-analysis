

# gdp-and-life-expectancy-analysis

### 数据来源

`https://www.gapminder.org/data/`网站所提供的Income、Life expectancy、Population数据。

### 分析目标

本项目用于统计2005-2019年全球各地区人均gdp和人均期望寿命信息，并提供Excel形式的统计结果与HTML网页形式的可视化动画。

### 目录结构

- `data`存放原始数据集，形式为三个Excel文件。
- `out`为结果输出路径。
- `src`存放源代码。

### 程序简述

在`src`目录下的`preprocess.py`负责数据预处理，`fusion`函数实现对三张Excel数据表对应数据的提取与融合，`str2num`函数可将数据集中包含的文本字符转换为数值；`main.py`为主程序运行入口，对预处理后的数据进行后处理并输出Excel和HTML结果文件。

注：在源代码中更有对每一行代码的详细注释。
