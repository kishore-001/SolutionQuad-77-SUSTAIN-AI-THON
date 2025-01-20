import  { useState, useEffect } from 'react';

export default function Dashboard() {
  const [sensorData, setSensorData] = useState({
    temperature: 0,
    humidity: 0,
    moisture: 0,
  });
  const [cropType, setCropType] = useState('Loading...');

  // Function to fetch data from API
  const fetchSensorData = async () => {
    try {
      const response = await fetch('http://localhost:8000/get_data');
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const data = await response.json();
      setSensorData({
        temperature: data.temperature,
        humidity: data.humidity,
        PH: data.pH,
      });
      console.log(data);

      // Determine crop condition
      const crop = getCropCondition(data.humidity, data.temperature, data.pH);
      setCropType(crop);
    } catch (error) {
      console.error('Error fetching sensor data:', error);
    }
  };

  // Function to determine crop based on sensor data
  const getCropCondition = (humidity, temperature, pH) => {
    const crops = [
        { name: 'Wheat', pH: [6.0, 7.0], humidity: [30, 60], temperature: [26, 32] },
        { name: 'Rice', pH: [5.5, 6.5], humidity: [65, 75], temperature: [26, 35] },
        { name: 'Corn', pH: [5.8, 7.0], humidity: [40, 70], temperature: [27, 33] },
        { name: 'Barley', pH: [6.0, 7.5], humidity: [30, 60], temperature: [27, 32] },
        { name: 'Soybean', pH: [6.0, 7.0], humidity: [50, 70], temperature: [26, 33] },
        { name: 'Potato', pH: [5.5, 6.5], humidity: [60, 80], temperature: [18, 28] },
        { name: 'Sugarcane', pH: [6.0, 7.5], humidity: [60, 80], temperature: [30, 35] },
        { name: 'Tomato', pH: [5.5, 7.0], humidity: [50, 70], temperature: [20, 30] },
        { name: 'Cotton', pH: [6.0, 7.5], humidity: [50, 65], temperature: [25, 35] },
        { name: 'Tea', pH: [4.5, 5.5], humidity: [70, 90], temperature: [20, 30] },
    ];

    const suitableCrops = crops.filter(crop => 
        pH >= crop.pH[0] && pH <= crop.pH[1] &&
        humidity >= crop.humidity[0] && humidity <= crop.humidity[1] &&
        temperature >= crop.temperature[0] && temperature <= crop.temperature[1]
    );

    console.log("hello");
    console.log(suitableCrops);

    return suitableCrops.length > 0 ? suitableCrops.map(crop => crop.name).join(', ') : 'No suitable crop found';
  };

  // Fetch data initially and every 30 seconds
  useEffect(() => {
    fetchSensorData();
    const interval = setInterval(fetchSensorData, 30000);
    return () => clearInterval(interval); // Cleanup interval on component unmount
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <div>
        <p>
          <strong>Temperature:</strong> <span id="temperature">{sensorData.temperature} °C</span>
        </p>
        <p>
          <strong>Humidity:</strong> <span id="humidity">{sensorData.humidity} %</span>
        </p>
        <p>
          <strong>PH:</strong> <span id="moisture">{sensorData.PH}</span>
        </p>
        <p>
          <strong>Recommended Crop:</strong> <span id="cropType">{cropType}</span>
        </p>
      </div>
    </div>
  );
}
