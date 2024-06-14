import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import base64


def stream():
    st.title('streamlit')
    st.header('hello user')
    st.subheader("hello")
    st.write(2)
    st.markdown('_italic_')
    df=st.write(pd.DataFrame({'a':[1,2,3],'b':[4,5,7]}))
    st.code('www.github.com')
    st.sidebar.title('sidebar')
    st.sidebar.write('hello')
    a = st.button('click me')
    if a:
        st.write('clicked')
    d=st.checkbox('done')
    if d:
        st.write('hello')


#st.sidebar.selectbox('select',{1:'one',2:'two'})

#upload_file=st.file_uploader("select file",type={'jpeg'})
'''a=st.selectbox('select',{1:'one',2:'two'})
if a:
    if upload_file is not None:
        image = Image.open(upload_file)
        st.image(image , caption='uploaded image',use_column_width=True)
        st.write("image uploaded successfully!")
    else:
        st.write("please upload an image file.")'''

    

def visualize():
    a= st.button('click me')
    if a:
        st.write('hello')
    upload_file= st.file_uploader("choose a file",type='jpeg')
    if upload_file is not None:
        image = Image.open(upload_file)
        st.image(image , caption='uploaded image',use_column_width=True)
        st.write("image uploaded successfully!")
    else:
        st.write("please upload an image file.")
    data={
        'a':[5,7,8,5,8,8,9,2],
        'b':[10,20,25,15,23,34,20,10]
    }
    df=pd.DataFrame(data)
    st.write('sample dataframe:')
    st.dataframe(df)

    #histogram
    plt.figure(figsize=(10,5))
    plt.scatter(df['a'],df['b'], alpha=0.90)
    plt.title('histogram of a')
    plt.xlabel('value')
    plt.ylabel('frequency')
    st.pyplot(plt)



st.sidebar.title('sidebar')
choice =st.sidebar.selectbox('select',{1:'one',2:'two'})
if choice==1:
    stream()
else:
    visualize()
    


#background image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background("C:\\Users\\kohinoor1\\Pictures\8sqkca4mtvl21.jpg")
   








