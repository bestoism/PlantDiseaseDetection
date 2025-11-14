# 🌿 Intelligent Plant Disease Detector with Active Learning

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red.svg)

This project transcends a simple plant disease detector. It's an **intelligent diagnostic assistant** designed to help farmers and plant enthusiasts identify diseases from leaf images using Deep Learning. More importantly, this system is engineered to **learn from its users** through an *active learning* feedback loop, enabling it to become progressively smarter over time.

## ✨ Live Demo

Try the application live here:

**[➡️ Click here to try the Live Demo!]([YOUR_STREAMLIT_APP_URL])**

*(Note: The application may take a moment to wake up on the first visit.)*

## 📸 Application Showcase

![Application Screenshot]([YOUR_SCREENSHOT_URL])
*(Replace this URL with a screenshot of your app. An easy way: take a screenshot, upload it to a new "Issue" in this GitHub repo, and then copy the image link.)*

## 🚀 Key Features

- **High-Accuracy Disease Classification**: Utilizes a MobileNetV2 architecture with Transfer Learning to classify 15 different plant conditions (diseased and healthy).
- **Interactive Web Interface**: Built with Streamlit for a seamless and intuitive user experience for uploading images and viewing results.
- **Informative Diagnostic Assistant**: Doesn't just provide a prediction label but also offers detailed **descriptions, symptoms, and treatment suggestions** for the detected disease.
- **Model Uncertainty Detection**: The application intelligently uses a **confidence threshold**. If the model is not confident in its prediction, it refrains from providing a potentially misleading answer.
- **💡 Innovation: Active Learning Feedback Loop**: When the model is uncertain, it **requests feedback from the user**. Users can provide the correct label (including free-text input). This valuable data is collected to retrain and improve the model in the future, creating a virtuous cycle of improvement.

## 🛠️ Technology Stack

- **Backend & Model**: Python, TensorFlow, Keras
- **Frontend & UI**: Streamlit
- **Image Processing**: OpenCV, Pillow
- **Numerical Computing**: NumPy
- **Dataset**: A filtered version of the PlantVillage Dataset

## 📂 Project Structure

```
.
├── models/
│   └── plant_disease_model.h5    # Trained model (ignored by .gitignore)
├── notebooks/
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_Model_Training.ipynb
│   └── 03_Model_Inference.ipynb
├── feedback/
│   └── needs_review/             # User feedback images & labels (ignored by .gitignore)
├── app.py                        # Main Streamlit application code
├── disease_info.py               # "Database" for disease information
├── requirements.txt              # Dependencies for deployment
└── README.md
```

## ⚙️ Installation & Local Setup

To run this project on your local machine, follow these steps:

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/[YOUR_USERNAME]/[YOUR_REPO_NAME].git
    cd [YOUR_REPO_NAME]
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the venv
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    The application will automatically open in your web browser.

## 🔄 The Active Learning Cycle Concept

This system is designed to evolve:

1.  **Prediction & Uncertainty**: The model makes a prediction. If the confidence is below 70%, it requests help.
2.  **User Feedback**: The user provides the correct label via an interactive form.
3.  **Data Collection**: The "difficult" image and its user-provided label are saved to the `feedback/needs_review/` directory.
4.  **Manual Verification & Relabeling**: Periodically, an administrator reviews the collected data to validate the user labels.
5.  **Retraining**: The model is retrained on an enriched dataset that now includes these challenging real-world examples.
6.  **Redeployment**: The new, smarter model is deployed, and the cycle continues.

## 🔮 Future Roadmap

- [ ] **Automated Retraining Pipeline (MLOps)**: Implement a simple MLOps pipeline to automatically trigger retraining when a certain amount of new feedback data is collected.
- [ ] **Explainable AI (XAI)**: Integrate Grad-CAM to visualize which parts of an image the model is focusing on to make its decisions.
- [ ] **Batch Image Uploads**: Allow users to upload multiple images at once for analysis.
- [ ] **Mobile Version (TFLite)**: Convert the model to the TensorFlow Lite (`.tflite`) format for potential deployment on mobile applications.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## 🙏 Acknowledgements

- This project utilizes the dataset from [PlantVillage](https://plantvillage.psu.edu/), a fantastic resource for the research community.
