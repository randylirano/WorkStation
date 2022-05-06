import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';

import { Link } from 'react-router-dom';

import CenterComponent from './CenterComponent';
import Logo from './Logo';
import NewWorkstationBox from './NewWorkstationBox';
import ExistingWorkstationBox from './ExistingWorkstationBox';


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
                direction='column'
                sx={{
                    alignSelf: 'center'
                }}
            >
                <Stack
                    direction='row'
                    spacing={2}
                >
                    <ExistingWorkstationBox/>
                    <NewWorkstationBox/>
                </Stack>
            </Grid>
        </CenterComponent>
  );
}

export default Home;
