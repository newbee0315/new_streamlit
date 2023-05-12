import streamlit as st
import matplotlib.pyplot as plt
# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query("SELECT * from kucun where  年份 = '2023年';", ttl=600)

dfs = df.groupby(['客户名称'])['本月实际库存数量'].sum().reset_index()
st.dataframe(dfs)

"一共有" +str(len(df))+ "条明细"

df = df[df['大区']=='华东区']
dfs1 = df.groupby(['办事处'])['本月实际库存数量'].sum().reset_index()
dfs1.columns = ['办事处','数量']
st.dataframe(dfs1)
