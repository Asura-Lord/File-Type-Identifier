import streamlit as st
import os
import hashlib

# ======= Magic Bytes Database =======
MAGIC_SIGNATURES = {
    b'\xFF\xD8\xFF': 'JPG',
    b'\x89\x50\x4E\x47': 'PNG',
    b'\x25\x50\x44\x46': 'PDF',
    b'MZ': 'EXE',
    b'PK': 'ZIP'
}

# ======= Functions =======
def get_file_type(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(8)
        for sig, ftype in MAGIC_SIGNATURES.items():
            if header.startswith(sig):
                return ftype
    return "Unknown"

def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_extension(file_name):
    return os.path.splitext(file_name)[1][1:].upper()

# ======= Streamlit UI =======
st.set_page_config(page_title="File Type Identifier 🔍", page_icon="🧠", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
        font-family: 'Courier New', monospace;
    }
    .title {
        color: #33FF57;
        text-align: center;
        font-size: 2.2em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .danger {
        background-color: #ff4b4b;
        color: white;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
    }
    .safe {
        background-color: #00c853;
        color: white;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
    }
    .info-box {
        background-color: #1e1e2e;
        padding: 12px;
        border-radius: 8px;
        margin-top: 10px;
        color: #bbb;
    }
</style>
""", unsafe_allow_html=True)

# ======= Title =======
st.markdown("<div class='title'>🧩 File Type Identifier & Malware Hint Scanner</div>", unsafe_allow_html=True)
st.write("Upload any file below to reveal its **true identity** 🕵️‍♂️")

# ======= File Upload =======
uploaded_file = st.file_uploader("Choose a file", type=None)

if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    real_type = get_file_type(uploaded_file.name)
    ext_type = get_extension(uploaded_file.name)
    file_hash = get_file_hash(uploaded_file.name)

    st.markdown(f"<div class='info-box'>📁 **File Name:** {uploaded_file.name}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-box'>🔍 **Detected Type:** {real_type}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-box'>📎 **Extension Type:** {ext_type}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-box'>🧮 **SHA256 Hash:** {file_hash}</div>", unsafe_allow_html=True)

    # ======= Check Mismatch =======
    if real_type != ext_type and real_type != "Unknown":
        st.markdown("<div class='danger'>⚠️ Suspicious File Detected! Type Mismatch ⚠️</div>", unsafe_allow_html=True)
        st.warning("This file might be disguised. Proceed with caution!")
    elif real_type == "Unknown":
        st.info("File type not recognized. Possibly corrupted or uncommon format.")
    else:
        st.markdown("<div class='safe'>✅ Safe File — Type Matches Extension</div>", unsafe_allow_html=True)

# ======= Footer =======
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>⚡ Built by Sujan | Stay Safe, Stay Dangerous ⚔️</p>",
    unsafe_allow_html=True
)
