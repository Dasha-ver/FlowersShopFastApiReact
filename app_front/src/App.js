import './App.scss';
import GeneralPage from "./components/GeneralPage";
import ItemsTable from './components/ItemsTable'
import SelectedItemPage from './components/SelectedItemPage'
import SelectedCategoryPage from "./components/SelectedCategoryPage";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import React, {useState, useEffect} from 'react';

function App() {

    return (
        <div className="App">
            <Routes>
                    <Route path="/GeneralPage" element={<GeneralPage/>}/>
                    <Route path="/SelectedCategoryPage" element={<SelectedCategoryPage/>}/>
                    <Route path="/ItemsTable" element={<ItemsTable/>}/>
                    <Route path="/SelectedItemPage" element={<SelectedItemPage/>}/>
            </Routes>

        </div>
  );
}

export default App;
