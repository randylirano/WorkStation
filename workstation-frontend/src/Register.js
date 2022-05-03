import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';

import { grey } from '@mui/material/colors';

import CenterComponent from './CenterComponent';
import Logo from './Logo';


function Register() {
    return (
        <CenterComponent>
            <Box
                component='div'
                textAlign='left'
                direction='column'
                alignSelf='center'
            >
                <Typography
                    variant='h4'
                    style={{
                        fontWeight: 450,
                        width: 'fit-content'
                    }}
                >
                    Register
                </Typography>
                <Grid
                    item
                    spacing={2}
                    display='flex'
                    justifyContent='center'
                    alignItems='center'
                    direction='column'
                    style={{
                        marginTop: 10,
                        paddingTop: 20,
                        backgroundColor: grey[100],
                        width: '30vw',
                    }}
                >
                    <Logo />
                    <Stack
                        spacing={2}
                        direction='column'
                        alignItems='left'
                        style={{
                            margin: 20,
                            width: '90%',
                        }}
                    >
                        <TextField
                          label='Username'
                          style={{
                              backgroundColor: 'white',
                          }}
                        />
                        <TextField
                          label='Email'
                          type='email'
                          style={{
                              backgroundColor: 'white',
                          }}
                        />
                        <TextField
                          label='Password'
                          type='password'
                          style={{
                              backgroundColor: 'white',
                          }}
                        />
                        <TextField
                          label='Confirm Password'
                          type='password'
                          style={{
                              backgroundColor: 'white',
                          }}
                        />
                        <Button variant='contained' >
                            Register
                        </Button>
                    </Stack>
                </Grid>
            </Box>
        </CenterComponent>
  );
}

export default Register;
