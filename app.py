import streamlit as st
from detect_objects import detect_count_objects

st.title("Web App for Camouflaged Military Objects detection")
# add_bg_from_local('pic2.png')
upload = st.file_uploader("Upload image", type=['png', 'jpg'])

# create two buttons on the same line
c1, c2 = st.columns(2)

inp_img = c1.button("View input image")
out_img = c2.button("Detect concealed object")

if upload is not None and inp_img:
    st.subheader("You uploaded following image")
    st.image(upload)
elif upload is not None and out_img:
    num_objects, result = detect_count_objects(upload)
    if num_objects >= 1:
        st.subheader(f"The total number of detected objects are {num_objects}!")
        st.image(image=result)
    else:
        st.subheader("It seems the input image doesn't have objects!!")
else:
    st.subheader("You have not uploaded any image yet!!")
