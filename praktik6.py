import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#header
st.title("praktikum 06 visualisasi data")
st.write("kelompok 26")
st.markdown("""
        - Syahidah Yuli Amaliah
        - izzuddin ahmad alqosam
        - Adi Triadi   
            """)

#dataset
stores = ['store A', ' store B', 'Store c']
male = [150,200,180]
female = [120,230,170]

#dataset transaksi penjualan
stores = ['store A', ' store B', 'Store c']
produk_a = [209,250,300]
produk_b= [150,300,200]

#data quater
q1_male = [150,180,160]
q1_female = [140,200,180]
q2_male = [170,190,175]
q2_female = [130,210,160]

#1grafik staked vertical bar chart
st.subheader("grafik staked vertical bar chart")

fig, ax =plt.subplots()
x = np.arange(len(stores))
ax.bar(x,male, label= 'male', color='blue')
ax.bar(x,female,bottom = 'female', label='female', color='pink')

ax.set_title('population on gender and store')
ax.set_xlabel('stores')
ax.set_ylabel('population')
ax.set_xticklabels(x)
ax.legend()

st.pyplot(fig)


#2 grafik staked vertical bar chart dengan matplotlib
st.subheader("grafik staked vertical bar chart dengan matplotlib")

fig, ax =plt.subplots()
x = np.arange(len(stores))
ax.bar(x,produk_a, label = 'produk A', color='blue')
ax.bar(x,produk_b,bottom = 'male' ,label='produk B', color='green')

ax.set_title('sales transaction by store')
ax.set_xlabel('stores')
ax.set_ylabel('sales')
ax.set_xticklabels(x)
ax.legend()

st.pyplot(fig)


#3 kustomisasi stacked vertichal bar chart
st.subheader("kustomisasi stacked vertichal bar chart")

for i in range(len(x)):
    plt.text(x[i], (produk_a[i]/2),str(produk_a[i])/2, ha='center', color='white')
    plt.text(x[i], produk_b[i] + produk_b[i]/2, str(produk_b[i]), ha='center', color='black')
st.pyplot(fig)


#4 grafik multiple stcaked vertichal barchat
st.subheader("multiple stcaked vertical bar chart")

fiq,ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

ax.bar(x-width/2,q1_male,label = 'q1_male', color = ' lightblue', width=width)
ax.bar(x-width/2,q2_male,bottom =q2_male,label = 'q2_male', color = 'red', width=width)

ax.set_title('pouplation by gender and store(multiple quaters)')
ax.set_xlabel('stores')
ax.set_ylabel('population')
ax.set_xticklabels(x)
ax.legend()

st.pyplot(fig)

