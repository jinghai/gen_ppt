import os
import pandas as pd

# 输入输出路径
input_path = r'D:\RTBH-10-1-2025\lenovo_france_august_2025.xlsx'
output_dir = r'D:\RTBH-10-1-2025\Engagement_breakdown\output'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'engagement_summary_raw.csv')

# 读取Excel
df = pd.read_excel(input_path)

# 解析时间，提取日期（年月日）
# Zeit格式示例: "2025. 08. 31. 23:26"
df['Date'] = pd.to_datetime(df['Zeit'].str.replace('.', '', regex=False).str.strip(), format='%Y %m %d %H:%M', errors='coerce').dt.date

# 过滤情感标签，统一小写
df['Polarity'] = df['Polarity'].str.lower()

# 只保留三种情感标签
valid_polarities = ['positiv', 'negativ', 'neutral']
df = df[df['Polarity'].isin(valid_polarities)]

# 计算互动总和（点赞+分享+评论）
df['Engagement'] = df['Anzahl von Likes'] + df['Anzahl von Teilen'] + df['Anzahl von Kommentaren']

# 按日期和情感分组，求互动总和
daily_engagement = df.groupby(['Date', 'Polarity'])['Engagement'].sum().reset_index()

# 透视表转换，日期为行，情感为列
pivot_df = daily_engagement.pivot(index='Date', columns='Polarity', values='Engagement').fillna(0)

# 统一列名顺序和大小写
pivot_df = pivot_df.rename(columns={'negativ': 'Negative', 'neutral': 'Neutral', 'positiv': 'Positive'})
pivot_df = pivot_df[['Positive', 'Negative', 'Neutral']]

# 保存结果
pivot_df.to_csv(output_path, index=True, date_format='%Y-%m-%d')

print(f"原始互动总和数据已保存到: {output_path}")