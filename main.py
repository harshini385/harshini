import streamlit as st
from streamlit_option_menu import option_menu

# st.title("Hello World")
# st.header("This is a header")
# st.subheader("this is a subheader")
# st.write("This is a text")
# st.text("This is a text")
# st.code("""
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Add two numbers
# sum = num1 + num2

# """, language="python")

# st.latex(r"E=mc^2")
# st.metric(label="Temperature",value="70 degree F")
# st.progress(0.5,text="50%")
# st.text_input("Enter your name")
# st.number_input("Enter your age")
# st.date_input("Enter your date of birth")
# st.checkbox("I agree")
# st.radio("select your gender",["male","female","other"])
# st.multiselect("Select Your Country",["United states","canada","United Kingdom"])
# st.slider(label="select your age",min_value=0,max_value=100,value=23)

with st.sidebar:

    select = option_menu(
        menu_title="vinsup",
        options=['Home','About','Service'],
        icons=['house','file-person','gear']


    )
if select=="Home":
    st.title("Welcome to Home")
    st.divider()
    col1,col2 = st.columns(2)
    with col1:
        a=  st.text_input("Name")
        if st.button("click"):
         st.write(a)
         st.balloons()
    with col2:
        st.text_input("Email")
        st.image('https://wallpaperaccess.com/full/4723250.jpg')
elif select=="About":
    st.title("Welcome to About")
elif select=="Service":
    st.title("Welcome to Service")
    