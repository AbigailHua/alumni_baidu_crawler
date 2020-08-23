# alumni_baidu_crawler

一个可以在百度搜索中爬取校友信息的简单爬虫

### 实现思路

读取校友名字，百度搜索"校友名字+上海交通大学"

保存第一页的搜索结果（10条左右）

目前反反爬虫策略仅限headers和sleep（本爬虫使用频率较低，对速度要求不高）

### Input

名为name.txt的文档，每一行是一位校友的名字

与.py同级

### Output

一个名为html的文件夹，与.py同级

下面的子文件夹以校友名字命名

子文件夹里保存搜索结果的txt文件，文件名为根据Windows文件命名规则处理后的网页title

#### Output目录结构：
└─html

    ├─alumni1
    
    │      searchResult1.txt
    
    │      searchResult2.txt
    
    │      ...
    
    │      searchResult10.txt
    
    │      
    
    └─alumni2
    
    │      searchResult1.txt
    
    │      searchResult2.txt
    
    │      ...
    
    │      searchResult10.txt
    
    └─...
