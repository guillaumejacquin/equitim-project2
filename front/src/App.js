import './App.scss';
import 'boxicons/css/boxicons.min.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AppLayout from './components/layout/AppLayout';
import Blank from './pages/Blank';
import {MultiStepForm} from './pages/Form'
function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<AppLayout />}>
                    <Route index element={<MultiStepForm />} />
                    <Route path='/mytemplates' element={<Blank />} />
                    <Route path='/newtemplate' element={<Blank />} />
                    <Route path='/mysousjacents' element={<Blank />} />
                    <Route path='/newsousjacent' element={<Blank />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App;