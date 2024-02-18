import streamlit as st

st.title("OpenC Streamlit Demp")
st.header("header")

image = st.file_uploader("Upload an image file", type=['jpeg','jpg','png'])
if image is not None:
    st.image(image)
st.text("Some text")

selected_value = st.selectbox("Select Box", ["Asd", "asdf", "asdfasdf"])
st.write(selected_value)
checkbox_value = st.checkbox("Applly Checkbox")
st.write(checkbox_value)