import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#judul
st.title("praktikum 7 visualisasi data")
st.subheader("horizontal barchart dan staked horizontal barchart")

#identitas kelompok
st.markdown("""
            izzuddin ahmad alqosam
            syhidah amalia
            aldi
            """)
# DATASET PENJUALAN SMARTPHONE
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300, 280]
sales_2024 = [380, 450, 320, 300]

# MENGATUR POSISI BATANG
y = np.arange(len(brands))
bar_width = 0.4

# FILTER KATEGORI
kategori = st.selectbox(
    "Pilih Kategori Visualisasi",
    ["Basic Chart", "Kustomisasi Grafik", "Multiple Chart"]
)

# BASIC CHART
if kategori == "Basic Chart":
    st.subheader("Horizontal Bar Chart Sederhana")

    fig1, ax1 = plt.subplots()
    ax1.barh(y, sales_2023, color='skyblue')
    ax1.set_yticks(y)
    ax1.set_yticklabels(brands)
    ax1.set_xlabel("Total Sales (in Units)")
    ax1.set_title("Smartphone Sales by Brand")
    st.pyplot(fig1)

    st.subheader("Stacked Horizontal Bar Chart Sederhana")

    fig2, ax2 = plt.subplots()
    ax2.barh(y, sales_2023, label='2023')
    ax2.barh(y, sales_2024, left=sales_2023, label='2024')
    ax2.set_yticks(y)
    ax2.set_yticklabels(brands)
    ax2.set_xlabel("Total Sales (in Units)")
    ax2.set_title("Smartphone Sales by Brand (Stacked)")
    ax2.legend()
    st.pyplot(fig2)
    
    # KUSTOMISASI GRAFIK
elif kategori == "Kustomisasi Grafik":
    st.subheader("Customized Horizontal Bar Chart")

    fig3, ax3 = plt.subplots()
    ax3.barh(y, sales_2023, color='lightblue', edgecolor='black')
    ax3.set_yticks(y)
    ax3.set_yticklabels(brands)
    ax3.set_xlabel("Total Sales (in Units)")
    ax3.set_title("Customized Smartphone Sales by Brand")
    ax3.grid(axis='x', linestyle='--', alpha=0.6)

    # label nilai (sesuai konsep kustomisasi)
    for i, v in enumerate(sales_2023):
        ax3.text(v + 5, i, str(v), va='center')

    st.pyplot(fig3)

    st.subheader("Customized Stacked Horizontal Bar Chart")

    fig4, ax4 = plt.subplots()
    ax4.barh(y, sales_2023, label='2023', color='skyblue', edgecolor='black')
    ax4.barh(y, sales_2024, left=sales_2023, label='2024', color='salmon', edgecolor='black')
    ax4.set_yticks(y)
    ax4.set_yticklabels(brands)
    ax4.set_xlabel("Total Sales (in Units)")
    ax4.set_title("Customized Stacked Sales by Brand")
    ax4.legend()
    ax4.grid(axis='x', linestyle='--', alpha=0.6)

    st.pyplot(fig4)