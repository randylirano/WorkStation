import { useState } from 'react';

import Button from '@mui/material/Button';
import DarkModeIcon from '@mui/icons-material/DarkMode';
import LightModeIcon from '@mui/icons-material/LightMode';
import Stack from '@mui/material/Stack';
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';


function SettingMenu() {
    const [theme, setTheme] = useState('light');
    const [showToggle, setShowToggle] = useState(false);

    const handleTheme = (event, newTheme) => {
        setTheme(newTheme);
    };

    const toggleThemeGroup = (event) => {
        setShowToggle(!showToggle);
    };

    return (
        <Stack>
            <Button
                variant='text'
            >
                Logout
            </Button>
            <Button
                variant='text'
                onClick={toggleThemeGroup}
            >
                Theme
            </Button>
            { showToggle && (
                <ToggleButtonGroup
                    value={theme}
                    exclusive
                    onChange={handleTheme}
                    aria-label='theme alignment'
                >
                    <ToggleButton value='light' aria-label='light theme'>
                        <LightModeIcon />
                    </ToggleButton>
                    <ToggleButton value='dark' aria-label='dark theme'>
                        <DarkModeIcon />
                    </ToggleButton>
                </ToggleButtonGroup>
            )}
        </Stack>
  );
}

export default SettingMenu;
