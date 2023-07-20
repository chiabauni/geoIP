import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()
CURRENCY_RATE_KEY = os.getenv("CURRENCY_RATE_API_KEY")
IP_KEY = os.getenv("IP_API_KEY")
IP_API_URL = os.getenv("IP_API_URL")
CURRENCY_RATE_API_URL = os.getenv("CURRENCY_RATE_API_URL")
CURRENCY_COUNTRY_API_URL = os.getenv("CURRENCY_COUNTRY_API_URL")

def update_states(dict_countries, countries_statistics, response_ip, distance_bs_as_country):
    countries_statistics.add_total_invocations()
    if (response_ip.json()['country_name'] not in dict_countries):
        dict_countries[response_ip.json()['country_name']] = [distance_bs_as_country, 1]
        if (countries_statistics.get_min_distance() > distance_bs_as_country):
            countries_statistics.set_min_distance(distance_bs_as_country)
        if (countries_statistics.get_max_distance() < distance_bs_as_country):
            countries_statistics.set_max_distance(distance_bs_as_country)
    else:
        dict_countries[response_ip.json()['country_name']][1] += 1
    countries_statistics.set_mean_distance(distance_bs_as_country)

def api_calls(ip):
    response_ip = requests.get(IP_API_URL + ip + '?access_key=' + IP_KEY + '&language=es')
    response_currency = requests.get(CURRENCY_COUNTRY_API_URL + response_ip.json()['country_code'], verify=False)
    currency_code = list(response_currency.json()[0]["currencies"].keys())[0]
    response_currency_rate = requests.get(CURRENCY_RATE_API_URL + '?access_key=' + CURRENCY_RATE_KEY + '&base=EUR&symbols=' + currency_code)
    currency_rate = list(response_currency_rate.json()["rates"].values())[0]
    return response_ip, currency_code, currency_rate

def is_valid_ip(ip):
    #IPv4
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    #IPv6
    regex1 = "((([0-9a-fA-F]){1,4})\\:){7}"\
             "([0-9a-fA-F]){1,4}"
    p = re.compile(regex)
    p1 = re.compile(regex1)
    if (re.search(p, ip)):
        return True
    elif (re.search(p1, ip)):
        return True
    return False

