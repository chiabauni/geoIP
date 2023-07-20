import instance from './config/axios'

export const getCountryByIp = async (ip) => {
    return await instance.get(`/country/${ip}`)
}