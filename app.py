import streamlit as st
import cv2
import numpy as np
import os
import tempfile
import streamlit.components.v1 as components
from ultralytics import YOLO
# Load model details from pickle file
def model(model_path):
    try:
        model=YOLO(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Main Streamlit app
def main(model_path ):
    st.title('Healmet Detection')
    
    # Load the model
    loaded_model = model(model_path)
    
    if loaded_model is None:
        st.error("Could not load the model. Please check your model files.")
        return

    # Image uploader
    uploaded_image = st.file_uploader(
        "Choose an image file", 
        type=['jpg', 'png', 'jpeg'],
        accept_multiple_files=False
    )

    if uploaded_image is not None:
        # Read the uploaded image
        file_bytes = uploaded_image.read()
        
        # Convert to OpenCV image
        nparr = np.frombuffer(file_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        # Predict using the loaded model
        try:
            result = loaded_model.predict(image)
        except Exception as e:
            st.error(f"Error during prediction: {e}")
            return
        # Display the image
        st.image(result[0].plot(), caption='Detected!')

def nev():
    st.set_page_config(layout="wide")
    components.html("""
<!-- Font Awesome for social icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<body>
                
   <style>
        

    .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 150px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 80%;
            top: 0%;
            z-index: 1000;
        }

        .logo {
            display: flex;
            align-items: center;
             margin-right: 60px;
                    
        }

        .logo img {
            
            height: 40px;
            width: auto;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 30px;
        }

        .nav-links a {
            text-decoration: none;
            color: #666;
            font-size: 16px;
            transition: color 0.3s ease;
        }

        .nav-links a:hover {
            color: #2d59a7;
        }

        .social-links {
            display: flex;
            gap: 15px;
            margin-right: 20px;
        }

        .social-links a {
            color: #666;
            text-decoration: none;
        }

        .social-links i {
            font-size: 18px;
        }

        .schedule-call {
            width:150px;
            background-color: #2d59a7;
            color: white !important;
            padding: 10px 20px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .schedule-call:hover {
            background-color: #1e3c7a;
        }

        /* Mobile menu styles */
        .hamburger {
            display: none;
            cursor: pointer;
            background: none;
            border: none;
            padding: 10px;
        }

        .hamburger span {
            display: block;
            width: 25px;
            height: 3px;
            background-color: #666;
            margin: 5px 0;
            transition: all 0.3s ease;
        }

        @media (max-width: 768px) {
            .hamburger {
                display: block;
            }

            .nav-links {
                display: none;
                position: absolute;
                top: 70px;
                left: 0;
                right: 0;
                background-color: white;
                flex-direction: column;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }

            .nav-links.active {
                display: flex;
            }

            .navbar {
                padding: 15px 20px;
            }
        }
    </style>
    <nav class="navbar">
        <div class="logo">
            <img src="https://static.wixstatic.com/media/a08789_941b7895bcde42eeb0adea78b4c96181~mv2.jpg/v1/fill/w_199,h_104,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/dallas_edited_edited.jpg" alt="Neuramonks Logo">
        </div>
        
        <button class="hamburger" id="hamburger">
            <span></span>
            <span></span>
            <span></span>
        </button>

        <div class="nav-links" id="nav-links">
             <a href="https://www.deepneuralai.com/" target="_blank">Home</a>
            <a href="https://www.deepneuralai.com/careers" target="_blank">Careers</a>
            <a href="https://www.deepneuralai.com/about" target="_blank">About Us</a>
            <a href="https://www.deepneuralai.com/services-8" target="_blank">Services</a>
                
       <div class="social-links">
                <a href="https://www.facebook.com/wix" target="_blank"><i class="fab fa-facebook-f"></i></a>
                <a href="https://www.linkedin.com/company/91364292/admin/feed/posts/" target="_blank"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/company/91364292/admin/feed/posts/"><i class="fab fa-linkedin-in" target="_blank"></i></a>
        </div>
            <a href="#contact" class="schedule-call">Schedule a Call</a>
        </div>
    </nav>
</body>
""")
    
def footer():
    components.html("""
    <body>
    <div></div>
    </body>
"""
    )
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    components.html("""
<body>
<!-- Font Awesome for social icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

 <style>
        
        .footer {
                
            width:100%;
            background-color: #373B44;
            color: white;
            padding: 40px 0;
            text-align: center;
           
        }

        .footer-nav {
            margin-bottom: 20px;
        }

        .footer-nav a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-size: 16px;
            transition: color 0.3s ease;
        }

        .footer-nav a:hover {
            color: #ccc;
        }

        .social-links {
            margin: 20px 0;
        }

        .social-links a {
            color: white;
            text-decoration: none;
            margin: 0 10px;
            font-size: 18px;
            transition: transform 0.3s ease;
            display: inline-block;
        }

        .social-links a:hover {
            transform: translateY(-3px);
        }

        .copyright {
            font-size: 14px;
            color: #ccc;
            margin-bottom: 5px;
        }

        .website-link {
            color: white;
            text-decoration: none;
            font-size: 14px;
            transition: color 0.3s ease;
        }

        .website-link:hover {
            color: #ccc;
        }
                       
       
    </style>
        <footer class="footer">
        <nav class="footer-nav">
            <a href="https://www.deepneuralai.com/" target="_blank">Home</a>
            <a href="https://www.deepneuralai.com/careers" target="_blank">Careers</a>
            <a href="https://www.deepneuralai.com/about" target="_blank">About Us</a>
            <a href="https://www.deepneuralai.com/services-8" target="_blank">Services</a>
        </nav>
         
        <div class="social-links">
            <a href="https://www.facebook.com/wix" target="_blank" class="social-link facebook">
                <i class="fab fa-facebook-f"></i>
            </a>
            <a href="https://www.linkedin.com/company/91364292/admin/feed/posts/" target="_blank" class="social-link instagram">
                <i class="fab fa-instagram"></i>
            </a>
            <a href="https://www.linkedin.com/company/91364292/admin/feed/posts/" target="_blank" class="social-link linkedin">
                <i class="fab fa-linkedin-in"></i>
            </a>
        </div>
        <p>Email: info@deepneuralai.com<p>
        <p class="copyright">Copyright © 2024 All Right Reserved.</p>
        <a href="https://neuramonks.com" class="website-link">Neuramonks.com</a>
    </footer>
</body>
""")



# Run the app
if __name__ == "__main__":
    nev()
    main('model\healmet_detaction.pt')
    footer()