import streamlit as st
import datetime 
import pandas as pd

st.title("Text box")
#creating  text box
name= st.text_input("enter your name")
st.write("your name is ", name)

#creating text area
input_text =st.text_area("Enter your review")
#printing entred text
st.write("""You entered: \n""",input_text)

#create number input
st.number_input("Enter your number")

#create number input
num= st.number_input("enter your number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

st.title("time")
#defening time function
st.time_input("Select your time")

st.title("Date")
#defening data function
st.date_input("Select date")

st.title("Date")
#defening date function
st.date_input("select your date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))

st.title("select color")
#defening color picker
color_code= st.color_picker("select your color")
st.header(color_code)

st.title("CSV Data")
data_file=st.file_uploader("Upload csv", type=["csv"])
details= st.button("Cheack details")
if details:
    if data_file is not None:
        file_details={"file_name":data_file.name,"file type":data_file.type,
        "file_size":data_file.size}
        st.write(file_details)
        df= pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("NO csv file is uploaded")
        
my_form=st.form(key='form')
a=my_form.text_input(label='enter any text')
#defening submit button
submit_button= my_form.form_submit_button(label='submit')

st.write(a)