import time
from utils import terminal_clean


TEXT_INFO = """
---------------------------------------------------------------------------------------------------
1. APOD, or Astronomy Picture of the Day, is a popular NASA website that features a different stunning image or photograph of the universe daily, accompanied by a brief, expert explanation written by professional astronomers, serving as a fantastic educational resource for all ages and showcasing the wonders of space.
---------------------------------------------------------------------------------------------------
2. A solar flare (FLR) is a powerful source of energy on the Sun that induces magnetic processes in the solar atmosphere. These events are accompanied by radiation emissions, X-rays, and ultraviolet light. They can affect cosmic changes and even technical systems on Earth, such as satellite communications, communications, and navigation.
---------------------------------------------------------------------------------------------------
3. NeoWs (Near Earth Object Web Service) is a NASA-powered RESTful API providing real-time data and information on Near-Earth Objects (NEOs), like asteroids, allowing users (developers, scientists, apps like Asteroid Tracker) to search for them by date, ID, or browse the entire dataset for planetary defense and scientific research.
---------------------------------------------------------------------------------------------------
"""

def exit_information():
    input("Press any button to continue... ")
    terminal_clean()

def output_information(text:str) -> str:

    terminal_clean()

    for i in text:  
        time.sleep(0.01)
        print(i, end='', flush=True)
    
    exit_information()
    return text







