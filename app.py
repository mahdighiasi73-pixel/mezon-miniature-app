import streamlit as st
import google.generativeai as genai
from PIL import Image

# تنظیمات صفحه
st.set_page_config(page_title="مزون مینیاتور", page_icon="👗")
st.title("👗 اتاق پرو هوشمند مزون مینیاتور (نازی‌آباد)")

# اتصال به هوش مصنوعی (API Key را در تنظیمات استریم‌لیت ست می‌کنیم)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.write("به دنیای مد مینیاتور خوش آمدید. عکس خود را آپلود کنید.")

user_img = st.file_uploader("عکس خودتان را انتخاب کنید", type=['jpg', 'png', 'jpeg'])
dress_img = st.file_uploader("عکس لباس مزون را انتخاب کنید", type=['jpg', 'png', 'jpeg'])

if st.button("پرو مجازی"):
    if user_img and dress_img:
        st.info("در حال پردازش توسط هوش مصنوعی مینیاتور...")
        # در اینجا منطق ارسال به Gemini قرار می‌گیرد
    else:
        st.warning("لطفاً هر دو عکس را آپلود کنید.")
