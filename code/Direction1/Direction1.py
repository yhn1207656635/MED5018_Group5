import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi

# 读取CSV文件
csv_file_path = 'yes_data.csv'
df = pd.read_csv(csv_file_path)

# df = df.sort_values(by='Age_Category')
#
# # 提取年龄、身高和体重列
# ages = df['Age_Category']
# heights = df['Height_(cm)']
# weights = df['Weight_(kg)']
#
# # 绘制身高散点图
# plt.subplot(1, 2, 1)
# plt.scatter(ages, heights, label='Height', color='blue', alpha=0.7)
# plt.title('Height vs Age')
# plt.xlabel('Age')
# plt.xticks(rotation=60)
# plt.ylabel('Height')
# plt.legend()
#
# # 绘制体重散点图
# plt.subplot(1, 2, 2)
# plt.scatter(ages, weights, label='Weight', color='orange', alpha=0.7)
# plt.title('Weight vs Age')
# plt.xlabel('Age')
# plt.xticks(rotation=60)
# plt.ylabel('Weight')
# plt.legend()
#
# # 调整布局
# plt.tight_layout()
#
# # 显示图形
# plt.show()


# # 选择需要比较的列
# disease_columns = [ 'Skin_Cancer', 'Other_Cancer', 'Depression', 'Arthritis']
#
# # 将'yes'/'no'转换为数值数据
# disease_columns = df[disease_columns].replace('Yes', 1).replace('No', 0)
#
# # 计算每种疾病的患病率
# averages = disease_columns.mean()
#
# # 创建雷达图
# labels=np.array(averages.index)
# stats=averages.values
#
# angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
#
# stats=np.concatenate((stats,[stats[0]]))
# angles+=angles[:1]
#
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
# ax.fill(angles, stats, color='red', alpha=0.25)
# ax.plot(angles, stats, color='red', linewidth=2)  # Plot the line around the outside
#
# # 设置雷达图的标签
# ax.set_yticklabels([])
# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(labels)
#
# # 展示图例和标题
# plt.title('Comparison of Diseases')
# plt.show()


# # 提取酒精消费和总体健康列
# alcohol_consumption = df['Alcohol_Consumption']
# overall_health = df['General_Health']
#
# # 绘制散点图
# plt.figure(figsize=(10, 6))
# plt.scatter(alcohol_consumption, overall_health, color='blue', alpha=0.5)
# plt.title('Scatter plot of alcohol consumption and overall health')
# plt.xlabel('Alcohol_Consumption')
# plt.ylabel('General_Health')
# plt.grid(True)
# plt.show()

# # 计算吸烟者和非吸烟者的数量
# smoking_counts = df['Smoking_History'].value_counts()
#
# # 创建柱状图
# plt.figure(figsize=(8, 6))
# sns.set(style="whitegrid")
# sns.barplot(x=smoking_counts.index, y=smoking_counts.values, palette="viridis")
#
# # 添加标题和标签
# plt.title('Ratio of smokers and non-smokers among patients')
# plt.xlabel('Smoking status')
# plt.ylabel('Count')
#
# # 显示图形
# plt.show()

# # 根据性别分割数据
# male_data = df[df['Sex'] == 'Male']
# female_data = df[df['Sex'] == 'Female']
#
# # 创建箱线图
# plt.figure(figsize=(10, 6))
# plt.boxplot([male_data['BMI'], female_data['BMI']], labels=['Male', 'Female'])
# plt.title('BMI Distribution by Gender for Cardiovascular Disease Patients')
# plt.xlabel('Gender')
# plt.ylabel('BMI')
# plt.grid(True)
# plt.show()

# # 根据年龄范畴对数据进行分组，并计算每个范畴的数量
# age_distribution = df['Age_Category'].value_counts().sort_index()
#
# # 创建柱状图
# plt.bar(age_distribution.index, age_distribution.values, color='deepskyblue')
#
# # 添加标题和标签
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.xticks(age_distribution.index, age_distribution.index, rotation=17)
# plt.ylabel('Count')
#
# # 显示柱状图
# plt.show()

# 统计男女比例
gender_counts = df['Sex'].value_counts()

# 创建饼图
labels = gender_counts.index
sizes = gender_counts.values

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightpink'])
ax.axis('equal')  # 使饼图更圆形

# 添加标题
plt.title('Gender Distribution')

# 显示饼图
plt.show()


fig, ax = plt.subplots(2,2,figsize=(15, 10))
sns.violinplot(x = 'Heart_Disease', y = 'Alcohol_Consumption', data = df, ax = ax[0,0]).set_title('Alcohol Consumption and Heart Disease')
sns.violinplot(x = 'Heart_Disease', y = 'Fruit_Consumption', data = df, ax = ax[0,1]).set_title('Fruit Consumption and Heart Disease')
sns.violinplot(x = 'Heart_Disease', y = 'Green_Vegetables_Consumption', data = df, ax = ax[1,0]).set_title('Green_Vegetables Consumption and Heart Disease')
sns.violinplot(x = 'Heart_Disease', y = 'FriedPotato_Consumption', data = df, ax = ax[1,1]).set_title('FriedPotato Consumption and Heart Disease')
