import base64
from pathlib import Path
import streamlit as st

def render_login_wall():
    # 1. Check authentication
    if st.session_state.get("user_id") is not None:
        return True

    # 2. Load Logo
    logo_file = (
        Path(__file__).resolve().parents[2]
        / "static"
        / "logo.jpg"
    )

    if not logo_file.exists():
        fallback_path = Path(
            r"C:\Users\Vivek Hingu\.gemini\antigravity-ide\brain\3d8e920c-5f11-4f5c-a8fb-39a54fff720c\.user_uploaded\media_1793425151543.jpg"
        )

        if fallback_path.exists():
            logo_file = fallback_path

    logo_img_tag = ""

    if logo_file.exists():
        logo_b64 = base64.b64encode(
            logo_file.read_bytes()
        ).decode("utf-8")

        logo_img_tag = f"""
        <img class="brand-logo"
        src="data:image/jpeg;base64,{logo_b64}"
        alt="Workout Logo"/>
        """

    # 3. Custom Styling
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@600;700;800;900&display=swap');

        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #F8FAFC !important;
        }

        .stApp {
            background-color: #0A0F17 !important;
            background-image:
                radial-gradient(
                    circle at 50% 0%,
                    rgba(182,255,74,0.12),
                    transparent 45%
                ),
                radial-gradient(
                    circle at 10% 60%,
                    rgba(16,185,129,0.06),
                    transparent 35%
                ),
                linear-gradient(
                    180deg,
                    rgba(10,15,23,0.90),
                    rgba(10,15,23,0.96)
                ),
                url("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1920&q=80");

            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stSidebar"],
        [data-testid="stSidebarCollapsedControl"] {
            display: none !important;
        }

        .block-container {
            max-width: 580px !important;
            padding: 2rem 1.5rem !important;
        }

        /* Branding */

        .brand-header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            margin: 0 auto 10px;
        }

        .brand-logo {
            width: 76px;
            height: 76px;
            border-radius: 16px;
            object-fit: cover;
            border: 2px solid rgba(182,255,74,0.5);
            box-shadow: 0 0 24px rgba(182,255,74,0.42);
        }

        .brand-title {
            font-family: 'Outfit', sans-serif !important;
            font-size: clamp(24px, 4.2vw, 32px) !important;
            font-weight: 800 !important;
            color: #FFFFFF !important;
            margin: 0 !important;
            letter-spacing: -0.6px;
            line-height: 1.2 !important;
        }

        .brand-accent {
            color: #B6FF4A !important;
        }

        .brand-tagline {
            text-align: center;
            font-size: 16px;
            color: #94A3B8;
            margin: 0 auto 24px;
        }

        /* Login Card */

        [data-testid="stForm"] {
            background: rgba(13,19,29,0.88) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 20px !important;
            padding: 24px 26px !important;
            box-shadow: 0 20px 40px -10px rgba(0,0,0,0.6) !important;
            backdrop-filter: blur(16px) !important;
        }

        .form-heading {
            font-size: 19px;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 5px;
        }

        .form-hint {
            font-size: 13px;
            color: #94A3B8;
            margin-bottom: 18px;
        }

        /* Inputs */

        [data-testid="stWidgetLabel"] p {
            color: #F1F5F9 !important;
            font-weight: 600 !important;
            font-size: 13px !important;
        }

        .stTextInput input {
            background: #0D131C !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255,255,255,0.15) !important;
            border-radius: 10px !important;
            min-height: 46px !important;
            font-size: 14px !important;
            padding: 0 14px !important;
        }

        .stTextInput input:focus {
            border-color: #B6FF4A !important;
            box-shadow: 0 0 0 2px rgba(182,255,74,0.2) !important;
        }

        .stTextInput input::placeholder {
            color: #64748B !important;
        }

        /* Dropdown */

        div[data-baseweb="select"] > div {
            background: #0D131C !important;
            border: 1px solid rgba(255,255,255,0.15) !important;
            border-radius: 10px !important;
            min-height: 46px !important;
        }

        div[data-baseweb="select"] * {
            color: #FFFFFF !important;
        }

        /* Button */

        div[data-testid="stFormSubmitButton"] > button {
            width: 100% !important;
            min-height: 48px !important;
            background: linear-gradient(
                135deg,
                #B6FF4A,
                #10B981
            ) !important;
            border: none !important;
            border-radius: 12px !important;
            font-size: 15px !important;
            font-weight: 700 !important;
            margin-top: 10px !important;
            box-shadow: 0 6px 20px -4px rgba(182,255,74,0.35) !important;
            transition: all 0.2s ease !important;
        }

        div[data-testid="stFormSubmitButton"] p {
            color: #060E04 !important;
            font-weight: 800 !important;
        }

        div[data-testid="stFormSubmitButton"] > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 10px 25px -4px rgba(182,255,74,0.5) !important;
        }

        /* Footer */

        .footer-text {
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #64748B;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # 4. Branding Section
    st.markdown("""
    <h1 class="brand-title">
        Vision Based
        <span class="brand-accent">Workout System</span>
    </h1>
        """, unsafe_allow_html=True)

    # 5. Login Form
    with st.form("login_form", clear_on_submit=False):

        st.markdown(
            """
            <div class="form-heading">
                Welcome Back
            </div>

            <div class="form-hint">
                Enter your username and fitness goal to begin.
            </div>
            """,
            unsafe_allow_html=True
        )

        username = st.text_input(
            "Username",
            placeholder="Enter your username"
        )

        workout_goal = st.selectbox(
            "What's your fitness goal?",
            options=[
                "💪 Muscle Building",
                "🔥 Weight Loss",
                "🏋️ Strength",
                "⚡ General Fitness"
            ],
            index=0,
            key="login_workout_goal"
        )

        submit_button = st.form_submit_button(
            "Start Workout ➔",
            use_container_width=True
        )

    # 6. Form Processing
    if submit_button:

        clean_user = username.strip()

        if not clean_user:
            st.error("Please enter a username to continue.")
            return False

        # Save user information
        st.session_state["username"] = clean_user

        st.session_state["user_id"] = (
            f"user_{clean_user.lower().replace(' ', '_')}"
        )

        # Save fitness goal
        st.session_state["workout_goal"] = workout_goal

        # Initialize workout state
        if "workout_started" not in st.session_state:
            st.session_state["workout_started"] = False

        st.rerun()

    return False
