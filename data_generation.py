import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

def generate_quiz_data(n_samples=1000):
    # Features
    # 1. Study Hours (0 to 20 hours)
    study_hours = np.random.uniform(0, 20, n_samples)
    
    # 2. Previous Scores (0 to 100)
    prev_scores = np.random.uniform(40, 100, n_samples)
    
    # 3. Quiz Difficulty (1: Easy, 2: Medium, 3: Hard)
    quiz_difficulty = np.random.randint(1, 4, n_samples)
    
    # 4. Time Spent on Quiz (10 to 60 minutes)
    time_spent = np.random.uniform(10, 60, n_samples)
    
    # Target: Quiz Score (0 to 100)
    # Score depends heavily on study hours and previous scores, and negatively on difficulty
    # Some noise is added to make it realistic
    noise = np.random.normal(0, 5, n_samples)
    
    base_score = (study_hours * 1.5) + (prev_scores * 0.6) - (quiz_difficulty * 5) + (time_spent * 0.1) + 10
    
    # Clip scores between 0 and 100
    quiz_score = np.clip(base_score + noise, 0, 100)
    
    data = pd.DataFrame({
        'Study_Hours': study_hours,
        'Prev_Scores': prev_scores,
        'Quiz_Difficulty': quiz_difficulty,
        'Time_Spent': time_spent,
        'Quiz_Score': quiz_score
    })
    
    return data

if __name__ == "__main__":
    df = generate_quiz_data()
    df.to_csv('quiz_data.csv', index=False)
    print("Dataset 'quiz_data.csv' generated successfully with 1000 samples.")
    print(df.head())
