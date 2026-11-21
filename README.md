EcoPack AI: Sustainable Packaging Recommendation System

EcoPack AI is an AI-powered decision-support system designed to help industries transition from traditional packaging to eco-friendly alternatives. By leveraging Machine Learning and Business Intelligence, the system predicts packaging material costs and CO₂ footprints while ranking materials based on a Sustainability Score.

The project combines data engineering, machine learning, web application development, business intelligence, and cloud deployment to support more sustainable packaging decisions.

Project Overview

The transition to sustainable packaging is often hindered by the complex trade-offs between mechanical strength, cost, and environmental impact. EcoPack AI addresses this challenge by providing data-driven recommendations that help industries evaluate packaging alternatives based on cost and environmental performance.

Core Features

- **AI-Driven Recommendations:** Uses Random Forest and XGBoost models to predict packaging material costs and CO₂ emissions.
- **Industry-Specific Filtering:** Provides tailored packaging considerations for:
  - Healthcare – sterility and strength.
  - Electronics – ESD protection and fragility.
  - Food – biodegradability.
- **Business Intelligence Dashboard:** Visualizes CO₂ reduction trends and cost-benefit analysis.
- **Automated Reporting:** Generates sustainability performance reports in PDF and Excel formats.
- **Sustainability Scoring:** Ranks packaging materials based on their sustainability performance.

Technical Stack

| Category | Technologies |
|---|---|
| Backend | Python, Flask (REST API) |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Database | PostgreSQL |
| Machine Learning | Scikit-Learn, Random Forest, XGBoost, Joblib |
| Data Science | Pandas, NumPy, Matplotlib |
| Cloud Platform | AWS |
| Infrastructure as Code | Terraform |
| Cloud Infrastructure | AWS EC2, VPC, Security Groups, IAM |
| Server Environment | Ubuntu Linux |
| Application Server | Gunicorn |
| Reverse Proxy | Nginx |
| Version Control | Git, GitHub |

Project Architecture

The project is structured around four major development milestones:

1. **Data Engineering**
   - PostgreSQL schema design.
   - Bulk data ingestion using StringIO buffers.
   - Preparation and organization of packaging material and product datasets.

2. **Machine Learning Pipeline**
   - Data preprocessing and feature engineering.
   - Development of cost and CO₂ prediction models.
   - Random Forest and XGBoost model training and evaluation.

3. **API Development**
   - Flask backend development.
   - REST API integration for serving model predictions.
   - Frontend integration for user interaction.

4. **Business Intelligence**
   - Sustainability data visualization.
   - Cost-benefit analysis.
   - Automated PDF and Excel reporting.

Cloud Infrastructure & DevOps Deployment

EcoPack AI was deployed on an AWS EC2 instance using Terraform for Infrastructure as Code (IaC). The deployment involved provisioning cloud infrastructure, configuring networking and security, and setting up the application on an Ubuntu Linux server.

AWS Infrastructure with Terraform

Terraform configuration files are maintained in the `Terraform/` directory.

```text
Terraform/
├── main.tf
├── provider.tf
├── variables.tf
├── outputs.tf
└── .terraform.lock.hcl
```

Terraform configuration files:

- **main.tf:** Defines the AWS infrastructure resources used for deployment.
- **provider.tf:** Configures the AWS provider for Terraform.
- **variables.tf:** Defines input variables used in the infrastructure configuration.
- **outputs.tf:** Defines outputs from the Terraform configuration.
- **.terraform.lock.hcl:** Locks provider dependency versions to maintain consistent Terraform configurations.

Deployment & Server Configuration

- **AWS EC2:** Provisioned an Ubuntu-based virtual server to host the Flask application.
- **Terraform:** Used Infrastructure as Code to provision AWS infrastructure.
- **AWS VPC:** Configured cloud networking for the deployment.
- **AWS Security Groups:** Configured network access rules for the application.
- **AWS IAM:** Worked with IAM permissions and resolved access-related issues.
- **Ubuntu Linux:** Managed server configuration and application deployment.
- **Gunicorn:** Configured as the WSGI application server for the Flask application.
- **Nginx:** Configured as a reverse proxy to handle incoming application requests.
- **Git & GitHub:** Used for source code management and version control.

Deployment Architecture

<img width="500" height="300" alt="image" align-items: center src="https://github.com/user-attachments/assets/86c743b9-e8d4-4157-b746-b6a6f09b0ebe" />


Installation & Setup

1. Prerequisites

Make sure the following tools are installed:

- Python 3.9 or later
- PostgreSQL 15 or later
- Git

2. Clone the Repository

```bash
git clone -b Ecopack_AI https://github.com/prachiavhad/Packaging-Recommendation-System.git

cd Packaging-Recommendation-System
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Database Configuration

Configure your PostgreSQL database credentials in `db_setup.py`.

Run the database setup and data ingestion scripts:

```bash
python db_setup.py

python db_ingestion.py
```

### 5. Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

Model Performance

- **Cost Predictor:** Random Forest Regressor, optimized to capture non-linear packaging material price fluctuations.
- **CO₂ Predictor:** XGBoost Regressor, used for environmental footprint forecasting.
- **Evaluation:** Model performance is assessed using R² scores across training and testing datasets.

The prediction models support data-driven packaging comparisons for procurement and sustainability decision-making.

Future Scope

- Improve model performance with additional packaging material datasets.
- Expand sustainability evaluation criteria.
- Enhance cloud infrastructure and deployment automation.
- Extend the recommendation system to support additional industries.

Author

**Prachi Avhad**

[GitHub Repository](https://github.com/prachiavhad/Packaging-Recommendation-System)
