import './App.scss';
import GeneralPage from "./components/GeneralPage";
import ItemsTable from './components/ItemsTable'
import SelectedItemPage from './components/SelectedItemPage'
import SelectedCategoryPage from "./components/SelectedCategoryPage";
import Login from "./authComponents/Login";
import Signup from "./authComponents/Signup";
import User from "./authComponents/User";
import Private from "./authComponents/Private";
import SelectedMenuHeaderPage from './components/SelectedMenuHeaderPage'
import {BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";

function App() {

    return (
        <div className="App">
            <Routes>
                    <Route path="/user" element={<User/>} />
                    <Route path="/private" element={<Private/>} />
                    <Route path="/login" element={<Login/>} />
                    <Route path="/signup" element={<Signup/>} />
                    <Route path="/kvetki.bel" element={<GeneralPage/>}/>
                    <Route path="/kvetki.bel/category" element={<SelectedCategoryPage/>}/>
                    <Route path="/ItemsTable" element={<ItemsTable/>}/>
                    <Route path="/kvetki.bel/category/item" element={<SelectedItemPage/>}/>
                    <Route path="/kvetki.bel/description" element={<SelectedMenuHeaderPage/>} />
            </Routes>

        </div>
  );
}

export default App;
