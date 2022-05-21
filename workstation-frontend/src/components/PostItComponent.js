import Typography from '@mui/material/Typography';

import ComponentWrapper from './ComponentWrapper'


function PostItComponent({ onClose }) {
    return (
        <ComponentWrapper onClose={onClose}>
            <Typography
                variant='body'
                contentEditable={true}
            >
                Hello World
            </Typography>
        </ComponentWrapper>
  );
}

export default PostItComponent;
