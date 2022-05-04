import { useState } from "react";

import AddPhotoAlternateIcon from '@mui/icons-material/AddPhotoAlternate';
import Button from '@mui/material/Button';
import LibraryAddCheckIcon from '@mui/icons-material/LibraryAddCheck';
import NoteIcon from '@mui/icons-material/Note';
import SpeedDial from '@mui/material/SpeedDial';
import SpeedDialIcon from '@mui/material/SpeedDialIcon';
import SpeedDialAction from '@mui/material/SpeedDialAction';
import Stack from '@mui/material/Stack';
import WallpaperIcon from '@mui/icons-material/Wallpaper';

import { v4 as uuidv4 } from 'uuid';

import { Rnd } from "react-rnd";


function Workstation() {
    const [componentList, setComponentList] = useState([]);

    const addComponent = (event) => {
        let key = uuidv4();
        setComponentList(componentList.concat(
            <Rnd
                key={key}
                style={{
                    backgroundColor: '#FFF59B',
                }}
                default={{
                    x: 100,
                    y: 100,
                    width: 320,
                    height: 200
                }}
            />
        ));
        console.log(componentList);
    };

    return (
        <div>
            <Stack
                spacing={1}
                position='fixed'
                margin={2}
                top={75}
            >
                <Button variant='contained' >
                    Save
                </Button>
                <Button variant='outlined'>
                    Delete
                </Button>
                <SpeedDial
                    ariaLabel='speeddial'
                    icon={<SpeedDialIcon />}
                    direction='down'
                >
                    <SpeedDialAction
                        key='post-it'
                        icon={<NoteIcon/>}
                        tooltipTitle='Post-It'
                        onClick={addComponent}
                    />
                    <SpeedDialAction
                        key='checklist'
                        icon={<LibraryAddCheckIcon/>}
                        tooltipTitle='Checklist'
                        onClick={addComponent}
                    />
                    <SpeedDialAction
                        key='image'
                        icon={<AddPhotoAlternateIcon/>}
                        tooltipTitle='Image'
                        onClick={addComponent}
                    />
                    <SpeedDialAction
                        key='background'
                        icon={<WallpaperIcon/>}
                        tooltipTitle='Background'
                        onClick={addComponent}
                    />
                </SpeedDial>
            </Stack>
            { componentList }
        </div>
  );
}

export default Workstation;
