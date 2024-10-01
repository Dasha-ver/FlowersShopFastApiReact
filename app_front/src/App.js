import './App.css';
import GeneralPage from "./components/GeneralPage";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
        <Routes>
                <Route path="/GeneralPage" element={<GeneralPage/>}/>
        </Routes>

    </div>
  );
}

export default App;
