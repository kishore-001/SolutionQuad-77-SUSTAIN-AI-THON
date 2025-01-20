import "./App.css";
import { Routes, Route } from "react-router-dom";
import Dailyplan from "./Components/Dailyplan";
import Home from "./Components/Home";
import Suggestion from "./Components/Suggestion";



export default function App() {
	return (
		<Routes>
			<Route path="/home" element={<Home />} />
			<Route path="/dailyplan" element={<Dailyplan />} />
			<Route path="/suggestion" element={<Suggestion />} />
		</Routes>
	);
}