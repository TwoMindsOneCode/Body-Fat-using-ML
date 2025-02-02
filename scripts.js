document.getElementById('prediction-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(result => {
            document.getElementById('bmi-result').textContent = `Your BMI: ${result.bmi}`;
            document.getElementById('bodyfat-result').textContent = `Body Fat Percentage: ${result.body_fat}%`;

            const bmiClassification = classifyBMI(result.bmi);
            document.getElementById('bmi-class-result').textContent = `BMI Classification: ${bmiClassification}`;

            const bodyFatClassification = classifyBodyFat(result.body_fat);
            document.getElementById('bodyfat-class-result').textContent = `Body Fat Classification: ${bodyFatClassification}`;
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
});

function classifyBMI(bmi) {
    if (bmi < 18.5) return 'Underweight';
    if (bmi >= 18.5 && bmi < 24.9) return 'Normal weight';
    if (bmi >= 25 && bmi < 29.9) return 'Overweight';
    return 'Obese';
}

function classifyBodyFat(bodyFat) {
    if (bodyFat < 10) return 'Essential Fat';
    if (bodyFat >= 10 && bodyFat < 20) return 'Athletes';
    if (bodyFat >= 20 && bodyFat < 25) return 'Fitness';
    if (bodyFat >= 25 && bodyFat < 32) return 'Average';
    return 'Obese';
}
