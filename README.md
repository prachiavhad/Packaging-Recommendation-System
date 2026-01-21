EcoPack AI: Sustainable Packaging Recommendation System  

EcoPack AI is an AI-powered decision-support system designed to help industries transition from traditional packaging to eco-friendly alternatives. By leveraging Machine Learning and Business Intelligence, the system predicts material costs and CO\_2 footprints while ranking materials based on a proprietary Sustainability Score.

Project Overview
The transition to sustainable packaging is often hindered by the complex trade-offs between mechanical strength, cost, and environmental impact. This project automates that analysis using a full-stack data science approach.

Core Features:
* AI-Driven Recommendations: Uses Random Forest and XGBoost to predict unit costs and CO\_2 emissions.
* Industry-Specific Filtering: Tailored constraints for Healthcare (sterility/strength), Electronics (ESD/fragility), and Food (biodegradability).
* BI Dashboard: Visual analytics for CO\_2 reduction trends and cost-benefit analysis.
* Automated Reporting: Export sustainability performance data as PDF or Excel reports.

Technical Stack
* Backend: Python, Flask (REST API)
* Frontend: HTML5, CSS3, Bootstrap 5 (Responsive UI)
* Database: PostgreSQL (Relational Data & Logs)
* Machine Learning: Scikit-Learn (Random Forest), XGBoost, Joblib
* Data Science: Pandas, NumPy, Matplotlib (BI Dashboard)
* Deployment: Gunicorn, Render Cloud

Project Architecture
The project is structured into four distinct milestones representing the end-to-end development lifecycle:
* Data Engineering: PostgreSQL schema design and bulk data ingestion using StringIO buffers.
* ML Pipeline: Feature engineering of CO\_2 and Cost-Efficiency indices.
* API Development: Flask backend for serving real-time model inferences.
* Business Intelligence: Data visualization and automated PDF reporting logic.

Installation & Setup
1. Prerequisites
* Python 3.9+
* PostgreSQL 15+2. 

2\. Clone the Repository

git clone https://github.com/prachiavhad/Packaging-Recommendation System.git
cd Packaging-Recommendation-System

3\. Install Dependencies
pip install -r requirements.txt

4\. Database Configuration
Update the credentials in db\_setup.py and run:
python db\_setup.py
python db\_ingestion.py

5\. Run the Application
python app.py
Access the UI at http://127.0.0.1:5000

Model Performance
* Cost Predictor: Random Forest Regressor optimized for non-linear price fluctuations.
* CO2 Predictor: XGBoost Regressor for precise environmental footprint forecasting.
* Metric Success: Achieved high R^2 scores across training and testing datasets, ensuring reliable recommendations for procurement decision-making.



