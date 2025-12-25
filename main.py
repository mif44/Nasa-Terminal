import questionary


from utils import launch_terminal, terminal_exit, terminal_clean
from astronomy_picture_day import image_acquisition
from asteroids_neows import asteroid_data_acquisition
from data_acquisition import get_data
from information import output_information, text
from solar_flare import producing_solar_flare


def menu_visualization():
    while True:
        choice = questionary.select("Select an option:", choices=["1. Astronomy Picture of the Day", "2. Solar Flare (FLR)", "3. Asteroids - NeoWs", "4. Information", "5. Exit"]).ask()
        if choice == "1. Astronomy Picture of the Day":
            selected_date = get_data()
            image_acquisition(selected_date)
        elif choice == "2. Solar Flare (FLR)":
            start_data = get_data()
            producing_solar_flare(start_data)
        elif choice == "3. Asteroids - NeoWs":
            start_data = get_data()
            asteroid_data_acquisition(start_data)
        elif choice == "4. Information":
            output_information(text)
        elif choice == "5. Exit":
            terminal_clean()
            terminal_exit()


if __name__ == "__main__":
    launch_terminal()
    menu_visualization()