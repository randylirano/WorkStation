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

import PostItComponent from './components/PostItComponent';


const COMPONENT = {
    POST_IT: PostItComponent,
    CHECKLIST: PostItComponent,
    IMAGE: PostItComponent,
}


function Workstation() {
    const [componentList, setComponentList] = useState([]);

    const removeComponent = (key) => () => {
        const newList = componentList.filter((item) => item.key !== key);
        setComponentList(newList);
    };

    const addComponent = (Component) => () => {
        let key = uuidv4();
        setComponentList(componentList.concat(
            <Component
                key={key}
                onClose={removeComponent(key)}
            />
        ));

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
                        onClick={addComponent(COMPONENT.POST_IT)}
                    />
                    <SpeedDialAction
                        key='checklist'
                        icon={<LibraryAddCheckIcon/>}
                        tooltipTitle='Checklist'
                        onClick={addComponent(COMPONENT.CHECKLIST)}
                    />
                    <SpeedDialAction
                        key='image'
                        icon={<AddPhotoAlternateIcon/>}
                        tooltipTitle='Image'
                        onClick={addComponent(COMPONENT.IMAGE)}
                    />
                    <SpeedDialAction
                        key='background'
                        icon={<WallpaperIcon/>}
                        tooltipTitle='Background'
                    />
                </SpeedDial>
            </Stack>
            { componentList }
        </div>
  );
}

export default Workstation;
