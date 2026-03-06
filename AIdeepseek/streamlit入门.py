import streamlit as st

st.title("入门演示")
st.header("一级标题")
st.subheader("二级标题")

st.write("张润张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏")
st.write("张润张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏")
st.write("张润张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏张润可爱捏")

st.image("./resources/zr1.jpg",width=500)

password = st.text_input("请输入密码",type="password")
st.write(f"输入的密码是:{password}")