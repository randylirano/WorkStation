import logo from './img/logo.svg';

import Box from '@mui/material/Box';


function Logo() {
    return (
        <Box
            component='img'
            sx={{
              height: 50,
              width: 50,
            }}
            alt='Logo'
            src={logo}
          />
  );
}

export default Logo;
