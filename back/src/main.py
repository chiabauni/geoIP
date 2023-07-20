from http.client import HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from geopy import distance
from fastapi import HTTPException
from src.statistic import Statistic
from src.utils.utils import api_calls, update_states, is_valid_ip
from src.utils.constants import BS_AS_LAT, BS_AS_LONG

def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    countries_statistics =  Statistic(100000000000000000, 0, 0, 0)
    dict_countries = {}

    @app.get('/api/country/{ip}', tags=["IP Info"])
    def get_country_info_by_ip(ip: str):
        if (not is_valid_ip(ip)):
            raise HTTPException(status_code=404, detail="IP not valid")
        response_ip, currency_code, currency_rate = api_calls(ip)
        bs_as_coord = (BS_AS_LAT, BS_AS_LONG)
        country_coord = (response_ip.json()['latitude'], response_ip.json()['longitude'])
        distance_bs_as_country = distance.distance(bs_as_coord, country_coord).km
        if (response_ip.status_code == 200):
            update_states(dict_countries, countries_statistics, response_ip, distance_bs_as_country)
            new_response_ip = {
                'ip': response_ip.json()['ip'],
                'country': response_ip.json()['country_name'],
                'country_code': response_ip.json()['country_code'],
                'languages': response_ip.json()['location']['languages'],
                'currency_code': currency_code,
                'currency_rate': currency_rate,
                'distance': str(distance_bs_as_country),
                'bs_as_coord': bs_as_coord,
                'country_coord': country_coord
            }
            return new_response_ip
        else:
            raise HTTPException(status_code=404, detail="Country not found")
        
    @app.get('/api/statistics', tags=["Statistics"])
    def get_statistics():
        return {
            'min_distance': countries_statistics.get_min_distance(),
            'max_distance': countries_statistics.get_max_distance(),
            'mean_distance': countries_statistics.get_mean_distance()
        }
    
    return app

app = create_app()

