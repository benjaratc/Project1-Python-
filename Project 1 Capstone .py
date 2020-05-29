#!/usr/bin/env python
# coding: utf-8

# Part 1 

# 1. จงเขียนโปรแกรมรับค่า Input จากผู้ใช้ ถ้าผู้ใช้ใส่ 0.0 จึงจะสิ้นสุดโปรแกรม คำนวณหาค่าเฉลี่ยของเลขทั้งหมดที่ผู้ใช้ใส่ และปริ้นค่าเฉลี่ยคูณด้วยจำนวนครั้งที่ใส่ทั้งหมด 

# In[7]:


Count = 0
Sum = 0 

num = float(input('ใส่ตัวเลขใดๆ (ถ้าใส่ 0.0 สิ้นสุดโปรแกรม ) :'))  

while num != 0.0:
    Sum = Sum + num
    Count +=1
    num = float(input('ใส่ตัวเลขใดๆ (ถ้าใส่ 0.0 สิ้นสุดโปรแกรม ) :')) 

avg = Sum/Count 
print(avg*Count)
print('Finished')


# 2. จงเขียนโปรแกรมให้ผู้ใช้ใส่เลข ขอบเขตล่าง และ ขอบเขตบน และคำนวณหาเลขจำนวนเฉพาะ (Prime Number) ที่อยู่ระหว่างขอบเขตล่างและขอบเขตบน

# In[735]:


low_bound = int(input('Enter a low bound number  :'))                                                    #if_else 
up_bound = int(input('Enter a high bound number  :'))  

for num in range(low_bound,up_bound +1): 
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break 
        else:
            print('%d is a prime number' %(num))

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers            


# Part 2 : Video Game Sales 

# In[46]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# 1. Import ไฟล์ vgsales เช็คข้อมูลเบื้องต้น

# In[183]:


df = pd.read_csv('../Desktop/DataCamp/vgsales.csv')
df.head()


# In[185]:


df.info()


# In[181]:


df.describe()


# 2. สุ่มอ่านข้อมูล 10 แถว หัว 5 แถว และท้าย 10 แถว

# In[57]:


df.sample(10)


# In[55]:


df.head(5)


# In[56]:


df.tail(10)


# 3. หา Top 10 Platform ยอดฮิต พร้อมระบุจำนวน

# In[187]:


countPlatform = df['Platform'].value_counts()       #df['Platform'].value_counts().head(10)
countPlatform.head(10)


# 4. หา Bottom 10 Platform ยอดฮิต พร้อมระบุจำนวน

# In[75]:


countPlatform = df['Platform'].value_counts()
countPlatform.tail(10)


# 5. หา Top 10 Platform ชนิดของเกมส์ยอดฮิต พร้อมระบุจำนวน 

# In[77]:


groupPlatform = df['Genre'].value_counts()
countGenre.head(10)


# 6. หา Bottom 10 Platform ชนิดของเกมส์ยอดฮิต พร้อมระบุจำนวน

# In[78]:


countGenre = df['Genre'].value_counts()
countGenre.tail(10)


# 7. หารายละเอียดเกมส์ GTA V ภาคต่างๆ ทั้งหมด 

# In[190]:


df[df['Name'] == 'Grand Theft Auto V']


# 8. หาจำนวนเกมส์ที่มีชื่อซ้ำกันทั้งหมด

# In[208]:


df[df['Name'].duplicated(keep = False)].sort_values('Name')   #keep = False คือซ้ำกันหมดจะออกมาอยู่ด้วย


# 9. หาจำนวนเกมส์ที่มีชื่อและ Platform ซ้ำกันทั้งหมด

# In[210]:


df[df[['Name','Platform']].duplicated(keep = False)].sort_values('Name')


# 10. จากข้อ 9 พิจารณาแถวที่ข้อมูลซ้ำแและลบแถวนั้น

# In[225]:


df_new = df.drop(df.index[[16127,14999,4145]])   #or inplace = True
df_new.head()


# 11. หารายได้ทั้งหมดเกมส์ FIFA 15

# In[313]:


df2 = df_new.groupby('Name').sum().reset_index()
df2


# In[231]:


df2[df2['Name'] == 'FIFA 15']


# 12. หารายได้ทั้งหมดของเกมส์ GTA V ในญี่ปุ่น

# In[232]:


df2[df2['Name'] == 'Grand Theft Auto V']


# 13. สร้าง DF ที่ให้ index เป็นรายชื่อของเกมส์ที่มีซ้ำ และ Column เป็นจำนวนที่มีซ้ำ ไม่นับที่เป็น Unique

# In[385]:


count = df_new['Name'].value_counts()
count = pd.DataFrame(count)
count = count[count['Name']>1]
count.rename(columns = {'Name':'Count'})


# 14. สร้าง DF ที่มี index เป็นชื่อบริษัท และเรียงลำดับตามรายได้รวมจากมากไปน้อย

# In[393]:


publisher = df_new.groupby('Publisher').sum().sort_values('Global_Sales')[::-1]
publisher = publisher['Global_Sales']
publisher = pd.DataFrame(publisher).reset_index()
publisher


# 15. จงสร้าง DF ที่บรรจุเกมส์ Series Call of duty ทั้งหมด

# In[416]:


callOfDuty = df_new[df_new['Name'].apply(lambda check: check[0:12] == 'Call of Duty')]
callOfDuty


# 16. จงหาว่า Call of Duty ภาคใดใน PC มีรายสูงสุดในยุโรป 5 อันดับแรก

# In[420]:


PC = callOfDuty[callOfDuty['Platform']=='PC'].sort_values('EU_Sales')[::-1].head(5)
PC


# 17. จงหาว่า Platform ใด มียอดขายรวมสูงสุดในยุโรป

# In[242]:


df_new.groupby('Platform').sum().sort_values('EU_Sales')[::-1].head(1)


# 18. จงหาว่าเกมส์ประเภทใดมียอดขายเฉลี่ยสูงสุดในภูมิภาคอื่นๆรอบโลก

# In[243]:


df_new.groupby('Genre').sum().sort_values('Global_Sales')[::-1].head(1)


# 19. สร้าง Bar Plot โดยให้แกน X เป็น Platform และ Y เป็นยอดขายทั่วโลก

# In[334]:


fig = plt.figure(figsize = (18,10))
sns.barplot(data = df_new, x ='Platform', y = 'Global_Sales')


# 20. สร้าง Pie Chart หาส่วนแบ่งทางการตลาดของ 5 บริษัทแรกที่มีรายได้มากที่สุด

# In[421]:


Top5MarketShare = df.groupby('Publisher').sum().sort_values('Global_Sales')[::-1].head(5)
Top5MarketShare


# In[422]:


fig = px.pie(Top5MarketShare, values = 'Global_Sales', names = Top5MarketShare.index)
fig.show()


# 21. สร้าง Count Plot นับข้อมูลประเภทของเกมส์

# In[423]:


fig = plt.figure(figsize = (22,8))
sns.countplot(x='Genre', data = df_new)
fig.show()


# 22. สร้าง Bar plot Top 5 รายได้ทั่วโลกของ Call of Duty ภาคต่างๆใน Xbox

# In[449]:


top5callOfDuty = callOfDuty[callOfDuty['Platform'] == 'X360'].sort_values('Global_Sales')[::-1].head(5)
top5callOfDuty


# In[446]:


fig = plt.figure(figsize = (20,8))
sns.barplot(data = top5callOfDuty, x = 'Name', y = 'Global_Sales')
fig.show()


# 23. สร้าง Line Graph แสดงรายได้จาก North America จากปีแรกถึงปีสุดท้าย

# In[286]:


year = df.groupby('Year').sum()
year.head()


# In[451]:


fig = px.line(year, y = 'NA_Sales', x = year.index, title = 'NA Sales', labels = {'x':'Year'})
fig.show()


# 24. สร้าง Stripplot โดยให้แกน X เป็น Genre และ แกน Y เป็นรายได้ทั่วโลก

# In[458]:


fig = plt.figure(figsize = (20,8))
sns.stripplot(x = 'Genre', y = 'Global_Sales',data = df_new)
fig.show()


# 25. สร้าง Distribution Plot ของปี

# In[459]:


fig = plt.figure(figsize = (20,8))
sns.distplot(df['Year'])


# 26. สร้าง Bar Plot แสดงรายได้รวมในญี่ปุ่นรายปี

# In[340]:


Japan_Sales = df_new.groupby('Year').sum()
Japan_Sales.head()


# In[344]:


fig = plt.figure(figsize = (20,8))
sns.barplot(data = Japan_Sales, x = Japan_Sales.index, y = 'JP_Sales')
fig.autofmt_xdate()
fig.show()


# Part 2: Airbnb

# 1. Import ไฟล์ AB_NYC_2019 และ เช็คข้อมูลเบื้องต้น

# In[353]:


bnb = pd.read_csv('../Desktop/DataCamp/AB_NYC_2019.csv')
bnb.head()


# In[463]:


bnb.info()


# 2. สุ่มอ่านข้อมูล 10 แถว หัว 5 แถว และท้าย 10 แถว

# In[354]:


bnb.sample(10)


# In[355]:


bnb.head(5)


# In[356]:


bnb.tail(10)


# 3. หา Top 10 Neighbourhood ยอดฮิต พร้อมระบุจำนวน

# In[466]:


countNeighbourhood = bnb['neighbourhood'].value_counts()
countNeighbourhood = pd.DataFrame(countNeighbourhood)
countNeighbourhood = countNeighbourhood.rename(columns = {'neighbourhood':'count'})
countNeighbourhood.head()


# 4. หา Bottom 10 Neighbourhood ยอดฮิต พร้อมระบุจำนวน

# In[491]:


countNeighbourhood = bnb.groupby('neighbourhood').size().reset_index(name = 'count').sort_values('count')[::-1]
countNeighbourhood.tail(10)


# 5. หา Top 10 Neighbourhood Group ยอดฮิต พร้อมระบุจำนวน

# In[359]:


countNeighbourhoodGroup = bnb['neighbourhood_group'].value_counts()
countNeighbourhoodGroup.head(10)


# 6. หา Bottom 10 Neighbourhood Group ยอดฮิต พร้อมระบุจำนวน

# In[360]:


countNeighbourhoodGroup = bnb['neighbourhood_group'].value_counts()
countNeighbourhoodGroup.tail(10)


# 7. หาค่าเฉลี่ยราคาของพื้นที่ และเขต

# In[361]:


groupby_neighbourhood_group = bnb.groupby('neighbourhood_group').mean()
groupby_neighbourhood_group['price']      #bnb.groupby('neighbourhood_group').mean()['price'] 


# In[497]:


groupby_neighbourhood = bnb.groupby('neighbourhood').mean().reset_index()[['neighbourhood','price']].sort_values('price')[::-1]
groupby_neighbourhood


# 8. จงหาว่าห้องประเภทใดมีราคาเฉลี่ยมากที่สุด

# In[363]:


groupby_roomtype = bnb.groupby('room_type').mean()
groupby_roomtype['price']


# 9. จงหาว่าพื้นที่ใดมีข้อมูลพื้นที่อยู่แค่หน่วยเดียว

# In[364]:


countNeighbourhood[countNeighbourhood ==1]


# 10. จงหาว่าที่พักแบบใดมีการให้บริการมากที่สุด และมากเท่าใด

# In[505]:


room_type = bnb['room_type'].value_counts()
room_type = pd.DataFrame(room_type)
room_type = room_type.rename(columns = {'room_type':'count'})
room_type


# 11. จงหาว่าพื้นที่ใดมีจำนวนรีวิวมากที่สุด และ เขตใดมีจำนวนรีวิวมากที่สุด

# In[513]:


bnb.groupby('neighbourhood').sum().sort_values('number_of_reviews')[::-1].head(1)


# In[515]:


bnb.groupby('neighbourhood_group').sum().sort_values('number_of_reviews')[::-1].head(1)


# 12. จงหา Top 3 จำนวน Minimum Nights ที่มีเขตไม่ซ้ำกัน

# In[520]:


bnb.sort_values('minimum_nights')[::-1].drop_duplicates('neighbourhood_group').head(3)


# 13. จงหาชื่อ Host ที่ลิสที่อยู่มากที่สุด 10 อันดับแรก (Hint: ใช้ชื่อไม่ได้)

# In[543]:


host = bnb.sort_values('calculated_host_listings_count')[::-1]       .drop_duplicates('calculated_host_listings_count')       .head(10)
host[['host_id','host_name','calculated_host_listings_count']] 


# 14. จงหาชื่อ Host ที่มีชื่อซ้ำกันมากที่สุด 10 ชื่อ (โดยที่ไม่ใช้คนเดียวกัน)

# In[563]:


host = bnb.sort_values('host_id')[::-1]       .drop_duplicates('host_id')
host_duplicate = host['host_name'].value_counts()
host_duplicate[host_duplicate>1].head(10)


# 15. จงหาชื่อ Host ที่มีรีวิวมากที่สุด 10 อันดับแรก

# In[567]:


bnb.groupby(['host_id','host_name'],as_index = False).sum().sort_values('number_of_reviews')[::-1].head(10)


# 16. จงหาชื่อ Host ที่มีการลิสที่อยู่ที่มีราคาเฉลี่ยสูงที่สุด 10 อันดับแรก

# In[574]:


bnb.groupby(['host_id','host_name'],as_index = False).mean().sort_values('price')[::-1].head(10)


# 17. จงเพิ่ม 2 คอลัมน์ชื่อ Year และ Month จาก last review ต่อท้าย โดยใช้ข้อมูลจากคอลัมน์ last_review (Hint: ใช้ lambda)

# In[576]:


bnb.head()


# In[588]:


bnb2 = bnb.dropna()
bnb2[['Year','Month','Date']] = bnb2.last_review.str.split("-",expand=True)
bnb2.head()


# 18. สร้าง column ใหม่ โดยให้บรรจุ Time of the week (วันจันทร์ อังคาร....) โดยใช้ข้อมูลจาก last_review (Hint: ใช้ timestamp เข้ามาช่วย) 

# In[699]:


day_of_week = {0:'Mon',1:'Tue', 2:'Wed', 3:'Thur', 4:'Fri', 5:'Sat',6:'Sun'}
bnb2['last_review'] = pd.to_datetime(bnb2['last_review'])
bnb2['day_of_week'] = bnb2['last_review'].apply(lambda time: time.dayofweek)
bnb2['day_of_week'] = bnb2['day_of_week'].map(day_of_week)
bnb2_day = bnb2.drop('day of week',axis = 1)
bnb2_day.head()


# 19. สร้าง Count Plot นับข้อมูลประเภทของที่อยู่อาศัย

# In[598]:


fig = plt.figure(figsize = (12,8))
sns.countplot(data = bnb, x = 'room_type')
fig.show()


# 20. สร้าง Pie Chart หาพื้นที่ ที่มีที่อยู่อาศัยเยอะที่สุด 5 อันดับแรก

# In[377]:


Top5Areas = bnb.groupby('neighbourhood').count().sort_values('id')[::-1].head(5)
Top5Areas


# In[378]:


fig = px.pie(Top5Areas, values = 'id', names = Top5Areas.index)
fig.show()


# 21. สร้าง Box Plot โดยให้แกน X เป็น เขต และ Y เป็นจำนวนรีวิว

# In[685]:


fig = plt.figure(figsize = (25,10))
fig = sns.boxplot(data = bnb, x = 'neighbourhood_group',y = 'number_of_reviews')
fig.set(ylim = (0,80))


# 22. สร้าง HeatMap จาก Correlation ของ DataFrame และพิจารณาดูความสัมพันธ์ พร้อมกับนำความสัมพันธ์ที่เป็น Strongest Positive มาทำ Scatter Plot

# In[604]:


bnb_corr = bnb.corr()
bnb_corr


# In[611]:


fig = plt.figure(figsize = (15,15))
sns.heatmap(bnb_corr, annot = True)


# In[614]:


fig = plt.figure(figsize = (12,10))
sns.scatterplot(data = bnb, x = 'reviews_per_month',y = 'number_of_reviews')
fig.show()


# 23. สร้าง Bar plot หาจำนวน Last review ของแต่ละเดือนของปี 2018 (change from count plot to bar plot)

# In[701]:


bnb3 = bnb2_day.groupby(['Year','Month'], as_index = False).sum()
bnb4 = bnb3[bnb3['Year'] == '2018']
bnb4


# In[686]:


fig = plt.figure(figsize = (12,10))
sns.barplot(data = bnb4, x = 'Month', y = 'number_of_reviews')
fig.show()


# 24. สร้าง Pie Chart หาอัตราส่วน Last Review ในแต่ละวัน

# In[700]:


fig = px.pie(bnb2_day , values = 'number_of_reviews', names = 'day_of_week')
fig.show()


# 25. สร้าง Line Graph หาราคาเฉลี่ยในแต่ละเดือนของ Last Review ในปี 2019

# In[702]:


bnb5 = bnb2_day.groupby(['Year','Month'], as_index = False).mean()
bnb6 = bnb5[bnb5['Year'] == '2019']
bnb6          #vdo is wrong no 2019 


# In[707]:


px.line(bnb6 , x = 'Month',y = 'price')


# 26. สร้าง Column ใหม่ โดยคำนวณ ณ เวลาปัจจุบันถึงวันที่ Last Review ห่างกันกี่วัน (Hint: ใช้ datetime ปัจจุบัน - datetime last review)

# In[713]:


import datetime
today = datetime.datetime.today()
today 


# In[717]:


bnb2_day['diff']= bnb2_day['last_review'].apply(lambda past: (today - past).days)
bnb2_day.head()


# 27. สร้าง Pie Chart ของระยะห่างของเวลา ระหว่างปัจจุบันถึง Last review เฉลี่ย ของแต่ละเขต (หน่วยเป็นวัน)

# In[720]:


bnb7 = bnb2_day.groupby('neighbourhood_group', as_index = False).mean()
bnb7


# In[721]:


fig = px.pie(bnb7 , values = 'diff', names = 'neighbourhood_group')
fig.show()


# 28. สร้าง Bar Plot ของระยะห่างของเวลา ระหว่างปัจจุบันถึง Last review เฉลี่ย ของแต่ละพื้นที่ 10 พื้นที่แรกที่มีระยะเวลามากที่สุด (หน่วยเป็นวัน)

# In[724]:


bnb8 = bnb2_day.groupby('neighbourhood', as_index = False).mean().sort_values('diff')[::-1].head(10)
bnb8.head()


# In[727]:


fig = plt.figure(figsize = (23,10))
sns.barplot(data = bnb8, x = 'neighbourhood', y = 'diff')
fig.show()


# 29. สร้าง Bar Plot ของค่าเฉลี่ยระยะเวลาห่างระหว่างปัจจุบันถึง Last review เฉลี่ย ของแต่ละพื้นที่ 10 พื้นที่แรกที่มีระยะเวลาน้อยที่สุด 

# In[728]:


bnb9 = bnb2_day.groupby('neighbourhood', as_index = False).mean().sort_values('diff')[::-1].tail(10)
bnb9.head()


# In[729]:


fig = plt.figure(figsize = (23,10))
sns.barplot(data = bnb9, x = 'neighbourhood', y = 'diff')
fig.show()


# 30. สร้าง Scatter Plot หาความสัมพันธ์ระหว่าง ระยะเวลาห่างระหว่างปัจจุบันถึง Last review กับ Minimum Nights (Hint: Correlation)

# In[730]:


fig = plt.figure(figsize = (15,15))
sns.heatmap(bnb_corr, annot = True)


# In[732]:


fig = plt.figure(figsize = (20,10))
sns.scatterplot(data = bnb2_day, x = 'diff',y = 'minimum_nights')
fig.show()


# In[733]:


px.scatter(bnb2_day, x = 'diff',y = 'minimum_nights')

