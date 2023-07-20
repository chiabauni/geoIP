import React from 'react';
import { FormControl, FormHelperText, InputLabel, OutlinedInput} from "@mui/material";

export default function InputNumber(props) {
    const {variable, setVariable} = props;

    return (
        <>
            <FormControl sx={{ m: 1, width:"60%" }}>
                <InputLabel htmlFor="outlined-adornment-amount" color={variable.error === "" ? "primary" : "error"}>IP</InputLabel>
                <OutlinedInput
                    id="outlined-adornment-amount"
                    label="Ip"
                    type="text"
                    error={variable.error !== ""}
                    value={variable.value}
                    onChange={(event) => {
                        setVariable({...variable, value: event.target.value});
                    }}
                />
                {!!variable.error && (
                    <FormHelperText error id="variable-error">
                        {variable.error}
                    </FormHelperText>
                )}
            </FormControl>
        </>
    )
} 