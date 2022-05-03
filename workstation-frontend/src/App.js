import { createTheme, ThemeProvider } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';

import {
  BrowserRouter,
  Route,
  Routes
} from "react-router-dom";

import Home from './Home';
import Login from './Login'
import Logo from './Logo';
import Register from './Register';


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
            <Box
                component='div'
                position='fixed'
                margin={2}
            >
                <Logo />
            </Box>
            <BrowserRouter>
                <Routes>
                    <Route exact path="/" element={<Home/>} />
                    <Route exact path="/register" element={<Register/>} />
                    <Route exact path="/login" element={<Login/>} />
                </Routes>
            </BrowserRouter>
        </ThemeProvider>
  );
}

export default App;
