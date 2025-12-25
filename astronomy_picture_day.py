import requests
import webbrowser
import os


from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("NASA_API_KEY", "DEMO_KEY")
 

def image_acquisition(selected_date: str):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key,
             "date": selected_date.strip()}
    
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        link = data.get("hfurl") or data.get("url")

        if link:
            webbrowser.open_new_tab(link)
        else:
            print("No URL in response:", data)

    except requests.HTTPError:
        print("Error body:", resp.text[:500])
    except requests.RequestException as e:
        print("The server did not respond (no internet, DNS, timeout", e)
    except ValueError:
        print("Not JSON / broken JSON")



