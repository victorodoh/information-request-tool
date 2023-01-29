from cache_dict import cached_data
import requests

def render_police_force_list():
    police_list_key = "police_list_key"

    # if police force list is available in cache return else fetch from the api
    if police_list_key in cached_data:
        return cached_data[police_list_key]
    else:
        resp = requests.get("https://data.police.uk/api/forces")
        if resp.status_code == 200:
            data = resp.json()
            list_of_police_force = {item["name"] : item["id"] for item in data}
            cached_data[police_list_key] = list_of_police_force
        else:
            list_of_police_force = {}
        return list_of_police_force
    
def return_stop_and_search_cases(police_force_selected, year_month):
    police_stop_and_search_list = render_police_force_list()
    
    # cache the stop and search result after each call to the api
    stop_and_search_key = police_force_selected + "-" + year_month
    if stop_and_search_key in cached_data:
        return cached_data[stop_and_search_key]
    else:
        response = requests.get(
            "https://data.police.uk/api/stops-force?force="
            + police_stop_and_search_list[police_force_selected]
            + "&date="
            + year_month
        )
        if response.status_code == 200:
            result = response.json()
            cached_data[stop_and_search_key] = {"length": len(result), "data": result}
            return {"length": len(result), "data": result}
        else:
            return {}