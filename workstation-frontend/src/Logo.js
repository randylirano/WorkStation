import Box from '@mui/material/Box';
import Button from '@mui/material/Button';

import { Link } from 'react-router-dom';

import logo from './img/logo.svg';


function Logo({
    clickable
}) {
    return (
        <Button
            component={Link}
            to={'/'}
            disabled={!clickable}
        >
            <Box
                component='img'
                sx={{
                  height: 50,
                  width: 50,
                }}
                alt='Logo'
                src={logo}
              />
        </Button>
  );
}

export default Logo;
