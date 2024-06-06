
import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
from pyzbar.pyzbar import decode

# Part 1: QR Code Generation and Display

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    img_buffer = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(img_buffer, format="PNG")
    return img_buffer.getvalue()

st.title("QR Code Generator and Decoder")

# Text input for QR code data
data = st.text_input("Enter data to encode in QR code:", "This is some text data to be encoded in the QR code.")

if st.button("Generate QR Code"):
    img_data = generate_qr_code(data)
    st.image(img_data, caption="Generated QR Code", use_column_width=True)
    
    # Save QR code image to file
    with open('qr_code.png', 'wb') as f:
        f.write(img_data)

# Part 2: QR Code Decoding and Verification

st.header("Decode QR Code")

uploaded_file = st.file_uploader("Upload QR code image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded QR Code", use_column_width=True)
    
    decoded_objects = decode(img)
    decoded_data = decoded_objects[0].data.decode('utf-8') if decoded_objects else None
    
    if decoded_data:
        st.write("Decoded data from QR code:", decoded_data)
    else:
        st.write("Decoded data unavailable. Potential decoding issue.")
