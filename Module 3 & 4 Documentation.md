**Milestone 2**

**Module 3: Machine Learning Dataset Preparation**
Objective: To curate a high-signal feature set and establish a rigorous validation framework for predictive modeling.

3.1 Data Partitioning \& Feature Selection
The dataset engineered in Milestone 1 was subjected to a systematic split to ensure model generalizability.
* Train-Test Split: A 80/20 stratified split was implemented using train\_test\_split to allocate data for model training and unbiased evaluation.
* Feature Engineering for ML: Categorical variables, specifically material\_type, were transformed into numerical vectors using One-Hot Encoding.
* Feature Matrix (X): Included raw mechanical properties such as strength, weight capacity, and biodegradability.
* Target Variables (y): Dual regression targets were established:
     unit\_cost for financial forecasting.
     co2\_emission\_score for environmental impact forecasting.

3.2 Scaling and Pipeline Construction
To maintain mathematical consistency across varied units (e.g., Newtons vs. Percentage), numerical features were processed through a scaling pipeline. This prevents features with larger numerical ranges from disproportionately influencing the gradient descent or node splitting processes.

**Module 4: AI Recommendation Model (ML-Based)**
Objective: To deploy supervised learning algorithms capable of forecasting material performance and automating the ranking logic.

4.1 Model Architectures (ai\_recommendation\_model.py)
Two distinct ensemble learning algorithms were selected based on their robustness to tabular data:
1. Random Forest Regressor (Cost Prediction):
* Utilized for its ability to handle non-linear relationships     and reduce variance through bagging (Bootstrap Aggregating).
* Configured with 100 estimators to ensure stable convergence of cost estimates.
2. XGBoost Regressor (CO\_2 Footprint Prediction):
* Deployed an Extreme Gradient Boosting framework to optimize the environmental impact prediction.
* Leveraged boosting to minimize residual errors, specifically focusing on the complex trade-offs between material weight and emission factors.

4.2 Model Evaluation Metrics
The performance of the predictive engines was validated using a multi-metric approach to ensure precision and reliability:
* Root Mean Squared Error (RMSE): Used to penalize large outliers in cost and emission forecasting.
* Mean Absolute Error (MAE): Provided an intuitive measure of the average error magnitude.
* R^2 Score (Coefficient of Determination): Employed to measure the proportion of variance explained by the models, ensuring the predictions correlate highly with actual material behaviors.

4.3 Material Ranking System
Post-inference, a ranking algorithm was implemented to synthesize model outputs into a decision-making tool.
* ML-Driven Inference: The system feeds real-time product requirements into the loaded .joblib models.
* Weighted Suitability Calculation: Predicted values are passed into a scoring function that ranks materials from #1 (Optimal) to #N (Least Sustainable), enabling the backend to serve the most efficient packaging options to the user interface.
