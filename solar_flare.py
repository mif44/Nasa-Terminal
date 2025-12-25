import requests
import webbrowser
import os


from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("NASA_API_KEY", "DEMO_KEY")


def producing_solar_flare(start_date: str):
    url = "https://api.nasa.gov/DONKI/FLR"
    params ={"api_key": api_key,
             "startDate": start_date.strip()}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        
        if not data:
            print(f"No solar flares found for the date {start_date}")
            return
        
        for event in data:
            flrID = event.get("flrID")
            beginTime = event.get("beginTime")
            peakTime = event.get("peakTime")
            classType = event.get("classType")
            link = event.get("link")
            
        if flrID:
                print(f"Solar Flare ID: {flrID}")
                print(f"Begin Time: {beginTime}")
                print(f"Peak Time: {peakTime}")
                print(f"Class Type: {classType}")
                print(f"Link: {link}")
                print("-" * 50)
        else:
            print(f"No flare ID found for the event.")

    except requests.HTTPError:
        print("Error body:", resp.text[:500])
    except requests.RequestException as e:
        print("The server did not respond (no internet, DNS, timeout", e)
    except ValueError:
        print("Not JSON / broken JSON")