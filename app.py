import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Mezon Miniature", page_icon="👗")
st.markdown("<h1 style='text-align: center; color: #d4af37;'>اتاق پرو مجازی مزون مینیاتور</h1>", unsafe_allow_html=True)

if "GOOGLE_API_KEY" not in st.secrets:
    st.error("لطفاً کلید API را در تنظیمات وارد کنید.")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    try:
        # استفاده از جدیدترین مدل موجود در لیست شما
        model = genai.GenerativeModel('gemini-2.0-flash')

        u_file = st.file_uploader("عکس مشتری", type=['jpg', 'png', 'jpeg'])
        d_file = st.file_uploader("عکس لباس مزون", type=['jpg', 'png', 'jpeg'])

        if st.button("✨ اجرای پرو مجازی"):
            if u_file and d_file:
                with st.spinner("هوش مصنوعی مینیاتور در حال تحلیل استایل..."):
                    img1 = Image.open(u_file)
                    img2 = Image.open(d_file)
                    
                    # ارسال عکس‌ها به هوش مصنوعی نسل جدید
                    response = model.generate_content([
                        "شما مشاور حرفه‌ای مد در مزون مینیاتور هستید. با تحلیل این دو تصویر، توضیح دهید که لباس تصویر دوم چطور با فرم بدن و چهره شخص در تصویر اول هماهنگ می‌شود. پاسخ را با لحنی محترمانه و به زبان فارسی بنویسید.",
                        img1, 
                        img2
                    ])
                    
                    st.success("نتیجه تحلیل هوشمند:")
                    st.write(response.text)
            else:
                st.warning("لطفاً هر دو عکس را آپلود کنید.")

    except Exception as e:
        st.error(f"خطای سیستمی: {e}")
