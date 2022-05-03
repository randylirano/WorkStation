import logo from './img/logo.svg';

import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

import { Link } from 'react-router-dom';

import CenterComponent from './CenterComponent';
import Logo from './Logo';
import WorkstationBox from './WorkstationBox';


function Home() {
    return (
        <CenterComponent>
            <Grid
                item
                spacing={2}
            >
                <Logo/>
                <Typography variant='h1'>Work Station</Typography>
                <Button
                    variant='text'
                    component={Link}
                    to={'/register'}
                >
                    Register
                </Button>
                <Typography variant='body'> / </Typography>
                <Button
                    variant='text'
                    component={Link}
                    to={'/login'}
                >
                    Login
                </Button>
            </Grid>
            <Grid
                item
                spacing={2}
            >
                <WorkstationBox/>
            </Grid>
        </CenterComponent>
  );
}

export default Home;
