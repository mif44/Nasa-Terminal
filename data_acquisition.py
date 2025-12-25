import questionary


from datetime import datetime


def get_data() -> tuple[str]:
    while True:

        choice = questionary.text("Enter the start date format YYYY-MM-DD:").ask()

        if not choice:
            print("You have not entered anything!")
            continue

        start_date = choice.strip()

        try:
            datetime.strptime(start_date, "%Y-%m-%d")

        except ValueError:
            print("The date is in the wrong format, it needs to be YYYY-MM-DD!")
            continue
        
        return start_date
    



