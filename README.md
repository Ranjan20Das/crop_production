A machine learning web application that predicts the most suitable crop to grow based on soil and weather conditions.
Built with IBM Cloud Machine Learning, Python, and Streamlit.

🚀 Features

Predicts suitable crop from soil nutrients and environmental data.

Deployed model on IBM Cloud Watson Machine Learning.

Frontend built using Streamlit.

Hosted on Streamlit Cloud for easy access.

🧑‍💻 Tech Stack

Python 3.9+

IBM Watson Machine Learning (Model Deployment)

Streamlit (Web UI)

Requests (API calls to IBM Cloud endpoint)

📦 Installation

Clone this repository:

git clone https://github.com/your-username/crop-prediction.git
cd crop-prediction


Install dependencies:

pip install -r requirements.txt


Example requirements.txt:

streamlit
requests

🔑 Setup IBM Cloud API Key

Log in to IBM Cloud Console
.

Navigate to Manage → Access (IAM) → API Keys.

Create a new API key and copy it.

Add your credentials in app.py:

API_KEY = "your-ibm-cloud-api-key"
DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/crop123/predictions?version=2021-05-01"

▶️ Run Locally
streamlit run app.py


Open in browser at: http://localhost:8501

☁️ Deploy on Streamlit Cloud

Push your repo to GitHub.

Go to Streamlit Cloud
.

Connect your GitHub repo.

Select app.py as the entry point.

Deploy 🚀

🖼️ App Interface

Enter soil & weather details (N, P, K, temperature, humidity, pH, rainfall).

Click Predict Crop.

The app shows the most suitable crop for your conditions.
