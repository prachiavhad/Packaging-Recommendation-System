**Milestone 3**

**Module 5: Flask Backend API**
Objective: To architect a RESTful communication layer that bridges the AI models, the PostgreSQL database, and the end-user interface.

5.1 REST API Architecture (app.py)
The backend was developed using the Flask micro-framework to expose several key endpoints for data processing and model inference.
* Product Input Handling: A /predict (POST) endpoint was implemented to receive JSON payloads containing product parameters such as industry type and fragility level.
* AI Material Recommendation: The API integrates with the pre-trained .joblib models to generate real-time suitability predictions based on the input parameters.
* Environmental Score Computation: Integrated logic within the API routes calculates the CO₂ Impact Index and Sustainability Score dynamically for each material candidate.

5.2 Database Connectivity & Security
* PostgreSQL Integration: Established a persistent connection using psycopg2 to query material metadata and log user selections.
* Secure Data Exchange: Implemented Cross-Origin Resource Sharing (CORS) to secure requests between the frontend and backend. All responses are structured in a standardized JSON format for seamless frontend parsing.

**Module 6: Frontend UI Development**
Objective: To design an intuitive, responsive dashboard that allows users to interact with AI predictions and compare material sustainability.

6.1 User Interface Design
The frontend was built using a modern web stack to ensure accessibility across devices.
* Core Technologies: Utilized HTML5 for structure, CSS3 for custom styling, and Bootstrap 5 for a mobile-first responsive grid system.
* Dynamic Input Forms: Created interactive forms that allow users to select industry categories (e.g., Electronics, Food) and define product weight and fragility requirements.

6.2 Data Visualization & Metrics
* AI Recommendation Display: The UI dynamically renders "Eco-Winner" cards, highlighting the top-ranked sustainable material for the specific product input.
* Ranking \& Comparison Table:
1. Ranking Table: Displays the top 10 material alternatives in a structured table format.
2. Comparison Metrics: Shows color-coded indicators for Predicted Cost (INR) and CO₂ Reduction %, enabling users to perform trade-off analysis between budget and environmental impact.
