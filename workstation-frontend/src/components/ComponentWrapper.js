import { useState } from "react";

import IconButton from '@mui/material/IconButton';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardHeader from '@mui/material/CardHeader';
import Divider from '@mui/material/Divider';
import MinimizeIcon from '@mui/icons-material/Minimize';
import Typography from '@mui/material/Typography';

import CloseIcon from '@mui/icons-material/Close';

import { Rnd } from "react-rnd";


function ComponentWrapper({ onClose, children }) {
    const [ hidden, setHidden ] = useState(false);

    const toggleHidden = () => {
        setHidden(!hidden);
    };

    return (
        <Rnd
            default={{
                x: 200,
                y: 100,
            }}
            minWidth={200}
            minHeight={60}
        >
            <Card
                style={{
                    backgroundColor: '#FFF59B',
                    border: 'rounded',
                    width: '100%',
                    height: '100%',
                }}
            >
                <CardHeader
                    action={
                        <div>
                            <IconButton onClick={toggleHidden} >
                                <MinimizeIcon />
                            </IconButton>
                            <IconButton onClick={onClose} >
                                <CloseIcon />
                            </IconButton>
                        </div>
                    }
                    disableTypography={true}
                    title={
                        <Typography variant='h6' contentEditable={true}>
                            Title goes here
                        </Typography>
                    }
                />
                <Divider />
                { !hidden && (
                    <CardContent>
                        { children }
                    </CardContent>
                )}
            </Card>
        </Rnd>
  );
}

export default ComponentWrapper;
