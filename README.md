# 🏋️‍♂️ Vision-Based Workout System (AI Gym Trainer)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.54.0-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose%20Estimation-00C7B7.svg?logo=google&logoColor=white)](https://developers.google.com/mediapipe)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent, real-time computer vision fitness trainer that monitors exercise form, tracks repetitions, calculates joint biomechanics, and delivers audio & visual feedback directly through an interactive WebRTC Streamlit interface.

---

## 🌟 Key Features

- **🎯 Real-Time Pose & Biomechanics Tracking:** Uses Google MediaPipe Pose and OpenCV for landmark detection and joint angle computations.
- **🔄 Automated Repetition & Set Counter:** Accurately counts reps per set and overall progress based on kinematic state machines.
- **📐 Form & Posture Feedback:** Detects bad form, hip sagging, excessive swinging, shallow depth, and back arching in real time.
- **📹 Low-Latency WebRTC Video Streaming:** Smooth live video feed handling via `streamlit-webrtc`.
- **🗣️ Smart Audio & AI Coaching:** Integrated text-to-speech feedback (gTTS) and LLM-powered exercise insights (Groq).
- **🎨 Custom Modern Dark UI:** Styled with sleek glassmorphism, responsive controls, and custom typography.
- **🔐 User Profiles & Goal Setting:** Tailor workout sessions according to fitness goals (Muscle Building, Weight Loss, Strength, General Fitness).

---

## 🏋️ Supported Exercises & Tracked Metrics

| Exercise | Tracked Biometrics | Form Quality Checks |
| :--- | :--- | :--- |
| **Squats** | Knee Angle, Back Angle | Depth Status (Parallel / Full / Shallow) |
| **Push-ups** | Elbow Angle, Body Alignment | Hip Sagging / Elevation Status |
| **Bicep Curls** | Elbow Angle | Shoulder Stability & Body Swing Detection |
| **Shoulder Press** | Elbow Angle, Arm Extension | Back Arching & Lockout Validation |
| **Lunges** | Front Knee Angle, Torso Angle | Balance & Knee Over Extension |

---

## 🏗️ Project Architecture

```plaintext
Ai-GYM_Trainer/
├── core/                       # Core kinematics and calculation engines
├── detectors/                  # Exercise-specific landmark detectors
├── ml_models/                  # Trained models and pose classification weights
├── services/                   # Modular service architecture
│   ├── auth/                   # Authentication & login wall UI
│   ├── coaching/               # LLM feedback & audio cue services
│   ├── config/                 # Workout & exercise configuration schemas
│   ├── persistence/            # Session persistence & history logging
│   ├── state/                  # Streamlit session state management
│   ├── tracking/               # Repetition counter & set trackers
│   ├── ui/                     # Custom CSS & font injectors
│   └── vision/                 # WebRTC frame processors & MediaPipe pipelines
├── static/                     # Custom fonts (AdobeClean.otf) & stylesheet (style.css)
├── .env.example                # Template for environment credentials
├── .gitignore                  # Git ignore rules for virtualenvs and secrets
├── main.py                     # Streamlit application entry point
└── requirements.txt            # Project dependencies
```

### 🔄 System Workflow & Data Pipeline

The diagram below illustrates the end-to-end data lifecycle: from real-time webcam video streaming via Streamlit WebRTC, through the MediaPipe detector and kinematic calculations, to metric evaluations, SQLite database logging, and dynamic UI updates.

![System Workflow Diagram](static/workflow.jpg)

```mermaid
flowchart TD
    %% Video Streaming & Processing Pipeline
    FrameUpdate["Frame update"] --> VideoInput["Video input<br/>Streamlit WebRTC"]
    VideoInput --> VideoProcessor["Video Processor Class"]
    VideoProcessor --> Detector["Detector Class /<br/>Mediapipe Model"]
    Detector --> FrameOutput["Frame output"]

    %% Closed loop & Metric processing
    FrameOutput --> FrameUpdate
    FrameOutput --> Metrics["Metrics update /<br/>Goal progress /<br/>DB Operations"]

    %% Database & UI Reflection
    Metrics --> SQLite["SQLite Setup"]
    Metrics --> ReflectsUI["Reflects to ui"]

    ReflectsUI --> LoginForm["Login Form UI"]
    ReflectsUI --> SidebarUI["Sidebar UI"]
    ReflectsUI --> StylesFonts["Add styles and fonts"]
```

#### Workflow Breakdown:
1. **Video Ingestion Loop (`Streamlit WebRTC`)**:
   - The user's live webcam stream is captured via `streamlit-webrtc` as incoming video frames (`Video input`).
   - Each frame is routed to the custom `Video Processor Class`.
2. **Pose Detection & Kinematics (`MediaPipe & OpenCV`)**:
   - The `Detector Class` passes the frame through the Google MediaPipe Pose model to extract 33 3D body landmarks.
   - Computes biomechanical joint angles (e.g., knee, elbow, torso, back arch) and evaluates exercise posture.
3. **Frame Output & Feedback Loop**:
   - Visual skeletons, angles, and feedback overlays are rendered directly onto the video frame (`Frame output`).
   - The annotated frame is pushed back to `Frame update` for continuous, smooth WebRTC rendering.
4. **Metrics Update & Database Persistence (`SQLite`)**:
   - Analyzes movement states (inflection points) to increment repetition and set counts.
   - Evaluates progress against user-configured goals.
   - Synchronizes workout logs, session statistics, and user achievements with local SQLite storage (`SQLite Setup`).
5. **UI Reflection (`Streamlit Frontend`)**:
   - **Login Form UI**: Captures username and fitness goals, persisting session state across reruns.
   - **Sidebar UI**: Provides interactive controls for workout planning, exercise selection, and real-time metric scorecards.
   - **Styles and Fonts**: Injects custom styling (`static/style.css`) and local typography (`AdobeClean.otf`) for a modern dark-mode interface.

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+**
- A working **Webcam**
- (Optional) [uv](https://github.com/astral-sh/uv) for fast package management

### 2. Clone the Repository
```bash
git clone https://github.com/thatvivekhingu/Vision-Based-Workout-System.git
cd Vision-Based-Workout-System
```

### 3. Create & Activate Virtual Environment

**Using `uv` (Recommended):**
```bash
# Create venv
uv venv

# Activate venv
# On Windows (PowerShell):
.venv\Scripts\activate
# On Linux / macOS:
source .venv/bin/activate
```

**Using standard `python -m venv`:**
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows PowerShell
```

### 4. Install Dependencies
```bash
# Using uv
uv pip install -r requirements.txt

# Or using standard pip
pip install -r requirements.txt
```

### 5. Setup Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 6. Run the Application
```bash
streamlit run main.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## 💻 Tech Stack

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/), [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc)
- **Computer Vision & ML:** [MediaPipe](https://developers.google.com/mediapipe), [OpenCV](https://opencv.org/)
- **Audio Feedback:** [gTTS](https://pypi.org/project/gTTS/)
- **LLM Coaching:** [Groq](https://groq.com/)
- **Styling:** Custom CSS, CSS Grid/Flexbox, Adobe Clean font

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
