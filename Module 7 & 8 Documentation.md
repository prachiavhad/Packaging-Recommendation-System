**Milestone 4**

**Module 7: Business Intelligence Dashboard**
Objective: Transforming raw data and model predictions into actionable sustainability insights and professional reports.
1\. Libraries \& Tools Installed
* matplotlib: Used for generating dark-themed, publication-quality static visualizations.
* reportlab: A PDF toolkit for creating dynamic sustainability certificates.
* openpyxl / pandas: For structured Excel data exporting.
* sqlite3 (Local) / psycopg2 (Cloud): For querying selection logs and material metadata.

2\. Implementation Logic
* Analytics Engine (bi\_dashboard.py): \* Queries the selection\_logs to calculate Material Popularity.
* Visualizations: \* Radar Chart: Visualizes the "Recyclability Index" across different material categories.
* Reporting System: Automated a pipeline where clicking "Export" triggers the backend to compile the latest database snapshots into a formatted PDF Sustainability Report.

**Module 8: Deployment \& Documentation**
Objective: Moving the application from a local development environment to a live, cloud-accessible production server.
1\. Cloud Infrastructure
* Platform: Render (Platform-as-a-Service).
* Database: PostgreSQL Cloud Instance (Managed Service).
* Web Server: gunicorn (Green Unicorn) was used as a production-grade WSGI HTTP Server to handle multiple concurrent requests.

2\. Deployment Workflow
* Database Migration: \* The schema from db\_setup.py was applied to the Render PostgreSQL instance.
* CI/CD Pipeline: \* Connected the GitHub repository to Render for Auto-Deployment.
* Mobile Optimization:
Implemented Flask-CORS to handle Cross-Origin Resource Sharing for mobile browser compatibility.
Applied CSS Media Queries to ensure the UI remains functional on smaller viewports (solving overlapping button issues).

3\. Final Documentation Artifacts
* README.md: Created a technical guide including installation steps, API endpoint descriptions, and a tech stack summary.
* Technical Report: Documented the architectural flow from the PostgreSQL data layer to the XGBoost/Random Forest ML models to the Flask/Bootstrap UI.
* Video Demo: Recorded a walkthrough of the "Eco Winner" comparison tool, BI dashboard interactivity, and successful PDF report generation.
