import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def train_quiz_model():
    # Load data
    df = pd.read_csv('quiz_data.csv')
    
    # Define features and target
    X = df[['Study_Hours', 'Prev_Scores', 'Quiz_Difficulty', 'Time_Spent']]
    y = df['Quiz_Score']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Training Complete.")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R2 Score: {r2:.4f}")
    
    # Save model
    joblib.dump(model, 'quiz_model.pkl')
    print("Model saved as 'quiz_model.pkl'.")

if __name__ == "__main__":
    train_quiz_model()
