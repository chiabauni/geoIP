import instance from './config/axios'

export const getStatistics = async (ip) => {
    return await instance.get(`/statistics`)
}