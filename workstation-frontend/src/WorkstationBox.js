import AddIcon from '@mui/icons-material/Add';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Grid from '@mui/material/Grid';

import { grey } from '@mui/material/colors';


function WorkstationBox() {
    return (
        <Card
            sx={{
                width: 100,
                height: 100,
                borderStyle: 'dashed',
                borderColor: grey[700],
                backgroundColor: grey[200]
            }}
        >
            <Box
                display='flex'
                justifyContent='center'
                alignItems='center'
                style={{
                    minHeight: '100%',
                }}
            >
                <Grid
                    container
                    spacing={0}
                    align='center'
                    alignItems='center'
                    justify='center'
                    direction='column'
                >
                    <AddIcon
                        fontSize='large'
                        sx={{ color: grey[700] }}
                    />
                </Grid>
            </Box>
        </Card>
  );
}

export default WorkstationBox;
