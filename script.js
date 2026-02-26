document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const studyHours = parseFloat(document.getElementById('studyHours').value);
    const prevScores = parseFloat(document.getElementById('prevScores').value);
    const difficulty = parseInt(document.getElementById('difficulty').value);
    const timeSpent = parseFloat(document.getElementById('timeSpent').value);

    // Simulate the ML model logic (matching the generation formula for consistency)
    // base_score = (study_hours * 1.5) + (prev_scores * 0.6) - (quiz_difficulty * 5) + (time_spent * 0.1) + 10
    
    let prediction = (studyHours * 1.6) + (prevScores * 0.58) - (difficulty * 4.5) + (timeSpent * 0.12) + 8.5;
    
    // Add some "AI jitter" for realism
    prediction += (Math.random() - 0.5) * 2;
    
    // Clamp between 0 and 100
    prediction = Math.min(Math.max(prediction, 0), 100);

    // Update UI
    const resultCard = document.getElementById('resultCard');
    const predictionValue = document.getElementById('predictionValue');
    const confidenceText = document.getElementById('confidenceText');
    const predictBtn = document.getElementById('predictBtn');

    predictBtn.innerText = 'Analyzing...';
    predictBtn.disabled = true;

    setTimeout(() => {
        resultCard.style.display = 'block';
        predictionValue.innerText = prediction.toFixed(1);
        
        // Confidence simulation
        if (studyHours > 5 && prevScores > 50) {
            confidenceText.innerText = 'Confidence: High';
            confidenceText.style.color = '#10b981';
        } else {
            confidenceText.innerText = 'Confidence: Medium';
            confidenceText.style.color = '#f59e0b';
        }

        predictBtn.innerText = 'Analyze Performance';
        predictBtn.disabled = false;
        
        // Scroll to result
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 1200);
});
