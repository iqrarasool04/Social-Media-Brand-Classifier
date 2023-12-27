const predictionForm = document.getElementById('prediction-form');
const predictionResults = document.getElementById('prediction-results');

predictionForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const text = document.getElementById('text').value;

    // Send a POST request to the Flask app's /predict endpoint
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    })
    .then(response => response.json())
    .then(data => {
        predictionResults.innerHTML = ''; // Clear previous results

        // Display predictions from both models
        predictionResults.innerHTML += `<h4>SVM Prediction:</h4>`;
        predictionResults.innerHTML += `<p>${data.svm_prediction}</p>`;

        predictionResults.innerHTML += `<h4>Random Forest Prediction:</h4>`;
        predictionResults.innerHTML += `<p>${data.rf_prediction}</p>`;
    })
    .catch(error => {
        console.error(error);
        predictionResults.innerHTML = '<p>Error fetching predictions.</p>';
    });
});
