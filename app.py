import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Mezon Miniature", page_icon="👗")
st.markdown("<h1 style='text-align: center;'>اتاق پرو مجازی مزون مینیاتور</h1>", unsafe_allow_html=True)

if "GOOGLE_API_KEY" not in st.secrets:
    st.error("لطفاً کلید API را در تنظیمات وارد کنید.")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "max_output_tokens": 8192,
    }

    # اصلاح نام مدل برای جلوگیری از ارور NotFound
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest",
        generation_config=generation_config,
    )

    col1, col2 = st.columns(2)
    with col1:
        u_file = st.file_uploader("عکس مشتری", type=['jpg', 'png', 'jpeg'])
    with col2:
        d_file = st.file_uploader("عکس لباس", type=['jpg', 'png', 'jpeg'])

    if st.button("✨ اجرای پرو مجازی"):
        if u_file and d_file:
            with st.spinner("در حال تحلیل استایل مینیاتور..."):
                try:
                    img1 = Image.open(u_file)
                    img2 = Image.open(d_file)
                    # درخواست از هوش مصنوعی
                    response = model.generate_content([
                        "شما مشاور مزون مینیاتور هستید. با دیدن این دو تصویر، پرو لباس عروس را تحلیل کنید و بگویید چقدر با چهره و فرم بدن شخص همخوانی دارد. پاسخ را به فارسی بنویسید.",
                        img1,
                        img2
                    ])
                    st.success("تحلیل هوشمند:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"خطای غیرمنتظره: {e}")
        else:
            st.warning("لطفاً هر دو عکس را آپلود کنید.")
