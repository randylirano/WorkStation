import { createTheme, ThemeProvider } from '@mui/material/styles';
import Box from '@mui/material/Box';

import {
  BrowserRouter,
  Route,
  Routes
} from "react-router-dom";

import Home from './Home';
import Login from './Login'
import Logo from './Logo';
import Register from './Register';
import SettingMenu from './SettingMenu';
import Workstation from './Workstation';


const theme = createTheme({
    palette: {
        primary: {
            main: '#1E7363',
        },
        secondary: {
            main: '#a73032',
        },
    },
});


function App() {
    return (
        <ThemeProvider theme={theme}>
            <BrowserRouter>
                <Box
                    component='div'
                    position='fixed'
                    margin={2}
                >
                    <Logo clickable />
                </Box>
                <Box
                    component='div'
                    position='fixed'
                    right={0}
                    margin={2}
                >
                    <SettingMenu />
                </Box>
                <Routes>
                    <Route exact path="/" element={<Home/>} />
                    <Route exact path="/register" element={<Register/>} />
                    <Route exact path="/login" element={<Login/>} />
                    <Route exact path="/workstation/*" element={<Workstation/>} />
                </Routes>
            </BrowserRouter>
        </ThemeProvider>
  );
}

export default App;
