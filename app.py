import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

st.set_page_config(page_title="Mezon Miniature", page_icon="👗")

if "GOOGLE_API_KEY" not in st.secrets:
    st.error("لطفاً کلید API را در تنظیمات وارد کنید.")
else:
    # اجبار به استفاده از نسخه پایدار
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    # تست کردن مدل‌های در دسترس (این بخش برای عیب‌یابی عالی است)
    try:
        # استفاده از مدل پایه که برای همه در دسترس است
        model = genai.GenerativeModel('gemini-1.5-flash') 
        
        st.markdown("<h1 style='text-align: center;'>اتاق پرو مجازی مزون مینیاتور</h1>", unsafe_allow_html=True)
        
        u_file = st.file_uploader("عکس مشتری", type=['jpg', 'png', 'jpeg'])
        d_file = st.file_uploader("عکس لباس", type=['jpg', 'png', 'jpeg'])

        if st.button("✨ اجرای پرو مجازی"):
            if u_file and d_file:
                with st.spinner("در حال تحلیل..."):
                    img1 = Image.open(u_file)
                    img2 = Image.open(d_file)
                    # ارسال بدون تنظیمات پیچیده برای تست اولیه
                    response = model.generate_content([
                        "به عنوان مشاور مزون مینیاتور، این لباس را روی بدن این شخص تحلیل کن.",
                        img1, img2
                    ])
                    st.success("تحلیل مینیاتور:")
                    st.write(response.text)
            else:
                st.warning("عکس‌ها را آپلود کنید.")
    except Exception as e:
        st.error(f"مدل در دسترس نیست. کد خطا: {e}")
        st.info("پیشنهاد: یک API Key جدید در Google AI Studio بسازید و مطمئن شوید که ریجن روی United States یا یک کشور اروپایی باشد.")
