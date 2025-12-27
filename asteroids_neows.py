import requests
import webbrowser


from config import API_KEY
    

def asteroid_data_acquisition(start_date: str) -> str:
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {"api_key": API_KEY,
             "start_date": start_date.strip()}
    
    try:
        resp = requests.get(url, params=params, timeout=(5, 30))
        resp.raise_for_status()
        data = resp.json()
        
        neos_by_date = data.get("near_earth_objects", {})
        if not neos_by_date:
            print("No near_earth_objects in response")
            return

        for date_key in sorted(neos_by_date.keys()):
            neos = neos_by_date.get(date_key, [])
            if not neos:
                continue

            neo = neos[0]

            link = neo.get("nasa_jpl_url")                     

            if link:
                webbrowser.open_new_tab(link)
            else:
                webbrowser.open_new_tab(resp.url)

            return

        print("No NEOs found in returned window.")

    except requests.HTTPError:
        print("Error body:", resp.text[:500])
    except requests.RequestException as e:
        print("The server did not respond (no internet, DNS, timeout", e)
    except ValueError:
        print("Not JSON / broken JSON")