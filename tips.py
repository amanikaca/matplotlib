import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Tips Dataset Visualizer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Load uploaded or default file
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("tips.csv")  # Ensure this file is in your GitHub repo

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Tips Dataset Visualizations')

# 1. Histogram
axs[0, 0].hist(df['total_bill'], bins=20, color='skyblue', edgecolor='black')
axs[0, 0].set_title('Histogram of Total Bill')
axs[0, 0].set_xlabel('Total Bill')
axs[0, 0].set_ylabel('Frequency')

# 2. Boxplot
axs[0, 1].boxplot(df['tip'], patch_artist=True, boxprops=dict(facecolor='lightgreen'))
axs[0, 1].set_title('Boxplot of Tip Amounts')
axs[0, 1].set_ylabel('Tip')

# 3. Pie Chart
gender_counts = df['sex'].value_counts()
axs[1, 0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightblue'])
axs[1, 0].set_title('Gender Distribution')

# 4. Bar Chart
avg_total_bill_by_day = df.groupby('day')['total_bill'].mean()
axs[1, 1].bar(avg_total_bill_by_day.index, avg_total_bill_by_day.values, color='orange')
axs[1, 1].set_title('Average Total Bill by Day')
axs[1, 1].set_ylabel('Average Total Bill')
axs[1, 1].set_xlabel('Day')

plt.tight_layout()
st.pyplot(fig)
