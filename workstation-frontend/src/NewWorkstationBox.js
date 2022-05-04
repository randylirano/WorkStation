import AddIcon from '@mui/icons-material/Add';
import Card from '@mui/material/Card';
import CardActionArea from '@mui/material/CardActionArea';
import { grey } from '@mui/material/colors';

import { Link } from 'react-router-dom';


function NewWorkstationBox() {
    return (
        <Card
            sx={{
                width: 100,
                height: 100,
                borderStyle: 'dashed',
                borderColor: grey[700],
                backgroundColor: grey[200],
                '&:hover': {
                  backgroundColor: grey[400],
                  opacity: [0.9, 0.8, 0.7],
                },
            }}
        >
            <CardActionArea
                sx={{
                    height: '100%'
                }}
            >
                <Link to='/workstation/new'>
                    <AddIcon
                        fontSize='large'
                        sx={{ color: grey[700] }}
                    />
                </Link>
            </CardActionArea>
        </Card>
  );
}

export default NewWorkstationBox;
