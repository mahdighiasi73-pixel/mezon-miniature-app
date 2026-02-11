import streamlit as st
import google.generativeai as genai
from PIL import Image

# تنظیمات ظاهری
st.set_page_config(page_title="Mezon Miniature", page_icon="👗")
st.markdown("<h1 style='text-align: center;'>اتاق پرو مجازی مزون مینیاتور</h1>", unsafe_allow_html=True)

# بررسی کلید API
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("لطفاً کلید API را در تنظیمات وارد کنید.")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    # تنظیمات مدل
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "max_output_tokens": 8192,
    }

    # خط زیر همان جایی است که ارور می‌داد - حالا اصلاح شده:
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="شما مشاور مد مزون مینیاتور هستید. با لحنی محترمانه پرو لباس را تحلیل کنید."
    )

    col1, col2 = st.columns(2)
    with col1:
        u_file = st.file_uploader("عکس خودتان", type=['jpg', 'png', 'jpeg'])
    with col2:
        d_file = st.file_uploader("عکس لباس", type=['jpg', 'png', 'jpeg'])

    if st.button("✨ اجرای پرو مجازی"):
        if u_file and d_file:
            with st.spinner("در حال تحلیل..."):
                img1 = Image.open(u_file)
                img2 = Image.open(d_file)
                response = model.generate_content([
                    "لطفاً بگویید این لباس عروس با توجه به فرم چهره و استایل این شخص، چطور به نظر می‌رسد؟",
                    img1,
                    img2
                ])
                st.success("تحلیل هوشمند مینیاتور:")
                st.write(response.text)
        else:
            st.warning("لطفاً هر دو عکس را آپلود کنید.")
