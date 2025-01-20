import "./App.css";
import { Routes, Route } from "react-router-dom";
import Dailyplan from "./Components/Dailyplan";
import Dashboard from "./Components/Dashboard";
import Suggestion from "./Components/Suggestion";



export default function App() {
	return (
		<Routes>
			<Route path="/" element={<Dashboard />} />
			<Route path="/dailyplan" element={<Dailyplan />} />
			<Route path="/dashboard" element={<Suggestion />} />
		</Routes>
	);
}