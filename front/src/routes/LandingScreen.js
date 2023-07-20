import {Button, Grid, Stack, Typography, List, ListItem} from "@mui/material";
import { getCountryByIp } from "../services/getCountryByIp";
import { getStatistics } from "../services/getStatistics";
import {useState} from "react";
import InputNumber from "../components/InputNumber";

export default function LandingScreen() {
    const [ip, setIp] = useState({value: null, error: ""});
    const [info, setInfo] = useState({});
    const [statistics, setStatistics] = useState({});
    const [isLoading, setIsLoading] = useState(false);
    const [isLoadingStatistics, setIsLoadingStatistics] = useState(false);

    function validateIP(ip) {
        //IPv4
        let ipv4 = /(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/;
        //IPv6
        let ipv6 = /((([0-9a-fA-F]){1,4})\:){7}([0-9a-fA-F]){1,4}/;
        if (ip.match(ipv4))
            return true;
        else if (ip.match(ipv6))
            return true;
        return false;
    }

    const onSuccess = async () => {
        if (validateIP(ip.value) === false) {
            setIp({...ip, error: "Debe ingresar una IPv4 o IPv6 valida"})
            return;
        }
        else {
            setIp({...ip, error: ""})
            await getCountryByIp(ip.value).then((response) => {
                if (response.status === 200) {
                    setInfo(response.data);
                    console.log(response.data);
                    setIsLoading(true);
                }
            });
        }
    }

    const onStatistics = async () => {
        await getStatistics().then((response) => {
            if (response.status === 200) {
                setStatistics(response.data);
                console.log(response.data);
                setIsLoadingStatistics(true);
            }
        });
    }

    return (
                <Stack>
                    <Grid
                        container
                        direction="row"
                        justifyContent="space-between"
                        alignItems="center"
                    >
                        <Typography variant="h2">Geolocalización de IPs</Typography>
                        {!isLoadingStatistics && (
                            <Button
                                variant="contained"
                                sx={{color: "#FFFFFF", borderRadius: 20, fontWeight: 'bold'}}
                                onClick={onStatistics}
                            >
                                Obtener estadisticas
                            </Button>
                        )}
                        {isLoadingStatistics && (
                            <Button
                                variant="contained"
                                sx={{color: "#FFFFFF", borderRadius: 20, fontWeight: 'bold'}}
                                onClick={() => {
                                    setStatistics({});
                                    setIsLoadingStatistics(false);
                                }}
                            >
                                Volver
                            </Button>
                        )}
                    </Grid>
                    {statistics && isLoadingStatistics && (
                        <Stack sx={{marginBottom:10}}>
                            <Typography variant="h4" style={{marginTop: 5}}>Estadisticas</Typography>
                            <Typography variant="subtitle1"><b>Distancia más cercana a Buenos Aires:</b> {Math.round(statistics.min_distance)} kms</Typography>
                            <Typography variant="subtitle1"><b>Distancia más lejana a Buenos Aires:</b> {Math.round(statistics.max_distance)} kms</Typography>
                            <Typography variant="subtitle1"><b>Promedio de distancias:</b> {Math.round(statistics.mean_distance)} kms</Typography>
                        </Stack>
                    )}
                    {!isLoadingStatistics && (
                        <>
                            <Typography variant="subtitle1">Ingrese a continuacion una IP</Typography>
                            <Stack direction="horizontal" mt={5}>
                                <InputNumber variable={ip} setVariable={setIp} />
                            </Stack>
                            <Stack direction="horizontal" mt={2}>
                            <Button
                                variant="contained"
                                sx={{color: "#FFFFFF", borderRadius: 20, fontWeight: 'bold', marginBottom: 5, width: "60%"}}
                                onClick={onSuccess}
                            >
                                Enviar
                            </Button>
                            </Stack>
                            {info && isLoading && (
                                <Stack sx={{marginBottom:10}}>
                                    <Typography variant="h4">Informacion de la IP</Typography>
                                    <Typography variant="subtitle1"><b>IP:</b> {info.ip}</Typography>
                                    <Typography variant="subtitle1"><b>Pais:</b> {info.country}</Typography>
                                    <Typography variant="subtitle1"><b>ISO Code:</b> {info.country_code}</Typography>
                                    <Typography variant="subtitle1"><b>Idiomas:</b></Typography>
                                    {info.languages.map((language) => (
                                        <List sx={{ listStyleType: 'disc', pl: 4 }}>
                                            <ListItem sx={{ display: 'list-item' }}>
                                                <Typography variant="subtitle1">{language.name} ({language.code})</Typography>
                                            </ListItem>
                                        </List>
                                    ))}
                                    <Typography variant="subtitle1"><b>Moneda:</b> {info.currency_code} (1 {info.currency_code} = {info.currency_rate} EUR)</Typography>
                                    {/*<Typography variant="subtitle1"><b>Hora:</b></Typography>*/}
                                    <Typography variant="subtitle1"><b>Distancia estimada:</b> {Math.round(info.distance)} kms   ({Math.round(info.bs_as_coord[0])}, {Math.round(info.bs_as_coord[1])}) a ({Math.round(info.country_coord[0])}, {Math.round(info.country_coord[1])})</Typography>
                                </Stack>
                            )}
                        </>
                    )}
                </Stack>
    )
}