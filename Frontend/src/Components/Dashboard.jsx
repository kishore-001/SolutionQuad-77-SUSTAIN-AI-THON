import  { useState } from 'react';

function CropPredictionForm() {
    const [temperature, setTemperature] = useState('');
    const [humidity, setHumidity] = useState('');
    const [ph, setPh] = useState('');
    const [prediction, setPrediction] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                temperature: parseFloat(temperature),
                humidity: parseFloat(humidity),
                ph: parseFloat(ph),
            }),
        });
        const data = await response.json();
        setPrediction(data.crop);  // Display the predicted crop
    };

    return (
        <div>
            <h1>Crop Prediction</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Temperature:</label>
                    <input
                        type="number"
                        value={temperature}
                        onChange={(e) => setTemperature(e.target.value)}
                    />
                </div>
                <div>
                    <label>Humidity:</label>
                    <input
                        type="number"
                        value={humidity}
                        onChange={(e) => setHumidity(e.target.value)}
                    />
                </div>
                <div>
                    <label>pH:</label>
                    <input
                        type="number"
                        value={ph}
                        onChange={(e) => setPh(e.target.value)}
                    />
                </div>
                <button type="submit">Predict Crop</button>
            </form>

            {prediction && <h2>Predicted Crop: {prediction}</h2>}
        </div>
    );
}

export default CropPredictionForm;
