import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Root from './routes/Root';
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import theme from "./theme";
import {ThemeProvider} from "@mui/material/styles";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Root />,
    }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <ThemeProvider theme={theme}>
        <RouterProvider router={router} />
      </ThemeProvider>
  </React.StrictMode>
);
