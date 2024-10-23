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
                    <Route path="/kvetki.bel" element={<GeneralPage/>}/>
                    <Route path="/kvetki.bel/category" element={<SelectedCategoryPage/>}/>
                    <Route path="/ItemsTable" element={<ItemsTable/>}/>
                    <Route path="/kvetki.bel/category/item" element={<SelectedItemPage/>}/>
            </Routes>

        </div>
  );
}

export default App;
