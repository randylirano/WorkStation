import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';


function CenterComponent({ children }) {
    return (
        <Box
            display='flex'
            justifyContent='center'
            alignItems='center'
            style={{
                minHeight: '100vh',
            }}
        >
            <Grid
              container
              spacing={3}
              align='center'
              justify='center'
              direction='column'
             >
                { children }
          </Grid>
      </Box>
  );
}

export default CenterComponent;
