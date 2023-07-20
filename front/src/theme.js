import { createTheme } from '@mui/material/styles';

const theme = createTheme({
    typography: {
        fontFamily: ['"Montserrat"', 'Open Sans'].join(','),
        fontSize: 16,
        h1: {
            fontWeight: 'bolder'
        },
        h2: {
            fontWeight: 'bolder'
        },
        h3: {
            fontWeight: 'bolder'
        },
        h4: {
            fontWeight: 'bolder'
        },
        h5: {
            fontWeight: 'bolder'
        },
        h6: {
            fontWeight: 'bolder'
        },
    },
    palette: {
        primary: {
            main: "#F0C323",
        },
        white: {
            main: "#FFFFFF"
        }
    }
})

export default theme;