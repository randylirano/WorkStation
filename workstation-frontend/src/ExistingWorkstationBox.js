import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import Card from '@mui/material/Card';
import CardActionArea from '@mui/material/CardActionArea';
import { grey } from '@mui/material/colors';

import { Link } from 'react-router-dom';


function ExistingWorkstationBox() {
    return (
        <Card
            sx={{
                width: 100,
                height: 100,
                borderStyle: 'solid',
                borderColor: grey[500],
                backgroundColor: 'primary.main',
                '&:hover': {
                  backgroundColor: 'secondary.main',
                  opacity: [0.9, 0.8, 0.7],
                },
            }}
        >
            <CardActionArea
                sx={{
                    height: '100%'
                }}
            >
                <Link to='/workstation/uuid'>
                    <ArrowForwardIosIcon
                        fontSize='large'
                        sx={{ color: 'white' }}
                    />
                </Link>
            </CardActionArea>
        </Card>
  );
}

export default ExistingWorkstationBox;
