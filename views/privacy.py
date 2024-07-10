import streamlit as st
import time

POLICY_1 = """
We collect both personal and non-personal information to provide and improve our services. Personal information includes details you provide directly, such as your name, email address, and contact details, when you register or interact with our site. Non-personal information includes data automatically collected, we may also collect information about your device.
"""
POLICY_2 = """
We use the information we collect to provide, maintain, and improve our services. This includes creating and managing your account, processing transactions, sending you updates and promotional materials, and responding to your inquiries. We also use the information to analyze usage trends, personalize your experience on our site, and ensure the security of our services.
"""
POLICY_3 = """
Privacy and security are critical components of maintaining trust and integrity in any digital platform. Privacy involves safeguarding personal information and ensuring that users have control over how their data is collected, used, and shared. It requires transparency about data practices and respect for user consent.
"""
POLICY_4 = """
We may share your information with third parties to comply with legal obligations, protect and defend our rights and property, prevent fraud, and enhance our services. This includes sharing information with service providers who assist us with operations such as payment processing, data analysis, email delivery, and hosting. Rest assured, we take measures to ensure that your data is shared securely and only as necessary.
"""

def stream_1_data():
    for word in POLICY_1.split(" "):
        yield word + " "
        time.sleep(0.03)
def stream_2_data():
    for word in POLICY_2.split(" "):
        yield word + " "
        time.sleep(0.03)
def stream_3_data():
    for word in POLICY_3.split(" "):
        yield word + " "
        time.sleep(0.03)
def stream_4_data():
    for word in POLICY_4.split(" "):
        yield word + " "
        time.sleep(0.03)


st.title("Privacy Policy")
st.write(
    "Welcome to Pragati. This Privacy Policy explains how we collect, use, and protect your information when you visit our website. Please read this policy carefully. If you do not agree with it, please do not use our site. We may update this policy from time to time. Changes will be indicated by the July 20, 2024 above. Continued use of our site constitutes acceptance of the changes."
)
st.write("\n")
st.write("\n")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
with col1:
    if st.button("Data Collection"):
        st.write_stream(stream_1_data)

with col2 :
    if st.button("Data Track & Usage"):
        st.write_stream(stream_2_data)

with col3 :
    if st.button("Privacy Security"):
        st.write_stream(stream_3_data)
with col4 :
    if st.button("Information Sharing"):
        st.write_stream(stream_4_data)
