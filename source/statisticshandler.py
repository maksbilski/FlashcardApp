from matplotlib.ticker import MaxNLocator
import calendar
import matplotlib.pyplot as plt
from datetime import datetime
import locale
import json


STATISTICS_SOURCEFILE_PATH = "data/stats.json"


def load_stats_data(path=STATISTICS_SOURCEFILE_PATH):
    """
    Loads and returns the data from a JSON file located at the provided path.
    If no path is provided, it uses the default path
     defined in STATISTICS_SOURCEFILE_PATH.

    :param path: str, the path to the JSON file containing the statistics data.
    :return: dict, the data stored in the JSON file.
    """
    with open(path, 'r') as filehandle:
        data = json.load(filehandle)
        return data


class StatisticsHandler:
    '''
    This class stores all data about user's learing progress
    and user's usage of the application.
    It provides methods that update stats and save them in the sourcefile.
    '''
    def __init__(self) -> None:
        '''
        Initialization method.
        Calls load_stats_data function so it can store all
        data from the source file to stats attribute
        Sets the locale to English so the month string is proper for display.
        '''
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        self.stats = load_stats_data()

    def get_total_stats(self) -> None:
        """
        Retrieves the total statistics for the user's activity
        such as total minutes spent using the app, total test sessions count,
        total review sessions count, and total card reviews count.

        :return: A string representing the total statistics in the format
        """
        total_minutes_spent = round(self.stats['total'].get('seconds') / 60)
        total_test_session_count = self.stats['total'].get('test_sessions')
        total_review_sessions_count = self.stats['total'].get('review_sessions') # NOQA
        total_cards_review_count = self.stats['total'].get('cards_reviewed')
        return (f"Total minutes spent using the app: {total_minutes_spent}\n"
                f"Total test sessions count: {total_test_session_count}\n"
                f"Total review sessions count: {total_review_sessions_count}\n"
                f"Total card reviews count: {total_cards_review_count}\n")

    def plot_daily_stats(self, datapiece: str) -> None:
        """
        Generates a bar plot that shows the
        daily statistics of a specific data piece for the current month.
        The x-axis represents the days of the current month
        and the y-axis represents the data piece specified by the user.
        The datapiece argument can hold "minutes", "review_sessions",
        "test_sessions" or "card_reviews".

        :param datapiece: str, the data piece that the user wants
            to show on the y-axis
        :param date: datetime, the date that the user wants
            to display the statistics for, current date will
            be used if not specified.
        """
        current_date = datetime.now()
        current_year = current_date.strftime("%Y")
        current_month = current_date.strftime("%B")
        formatted_string = datapiece.replace("_", " ").capitalize()
        title_string = f"Daily {formatted_string} in " + current_month + " " + current_year

        current_month_data = self.stats['yearly'][str(current_date.year)][str(current_date.month)]
        x = current_month_data.keys()
        if datapiece == 'minutes':
            y = [
                value['seconds'] / 60
                for value in current_month_data.values()
                ]
        else:
            y = [value[datapiece] for value in current_month_data.values()]

        plt.figure(num=title_string)

        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.bar(x, y, color="blueviolet")
        plt.xlabel('Day', fontsize=9, fontweight='bold')
        plt.ylabel(formatted_string, fontsize=9, fontweight='bold')
        plt.title(title_string, fontsize=16, fontweight='bold')
        plt.grid(True, axis='y')
        plt.xticks(rotation=30, fontsize=6.5)
        plt.show(block=False)


    def get_monthly_total(self, year=None, month=None) -> str:
        """
        This method calculates the total data
        for a given month in a given year.
        It takes two integer arguments, 'year'
        and 'month' and returns a string
        containing the total minutes, total
        test sessions, total review sessions,
        and total cards reviewed during that month and year.

        :param year: an integer representing the year
            for which to calculate the data.
        :param month: an integer representing the month
            for which to calculate the data.
        """
        if year is None:
            year = datetime.now().year
        if month is None:
            month = datetime.now().month
        month_word = calendar.month_name[month]
        year = str(year)
        month = str(month)
        yearly_stats = self.stats['yearly']
        total_minutes = 0
        total_test_sessions = 0
        total_review_sessions = 0
        total_cards_reviewed = 0
        for day in yearly_stats[year][month].keys():
            total_minutes += round(yearly_stats[year][month][day]['seconds'] / 60) # NOQA
            total_test_sessions += yearly_stats[year][month][day]['test_sessions'] # NOQA
            total_review_sessions += yearly_stats[year][month][day]['review_sessions'] # NOQA
            total_cards_reviewed += yearly_stats[year][month][day]['cards_reviewed'] # NOQA
        return (f"Total minutes in {month_word} of year {year}: {total_minutes}\n" # NOQA
                f"Total test sessions in {month_word} of year {year}: {total_test_sessions}\n"  # NOQA
                f"Total review sessions in {month_word} of year {year}: {total_review_sessions}\n"  # NOQA
                f"Total cards reviewed in {month_word} of year {year}: {total_cards_reviewed}\n")  # NOQA

    def update_data(self, **kwargs) -> None:
        """
        Updates the statistics of the current year, month and day
        in the self.stats['yearly] dictionary
        Also updates the statistics of total time using the app.

        :param kwargs: dict, Key-value pairs representing
            the statistics to update
        """
        current_year = str(datetime.now().year)
        current_month = str(datetime.now().month)
        current_day = str(datetime.now().day)
        self._create_json_nesting(current_year, current_month, current_day)
        for key, value in kwargs.items():
            self.stats['yearly'][current_year][current_month][current_day][key] += value # NOQA
            self.stats['total'][key] += value

    def update_source_file(self, path=STATISTICS_SOURCEFILE_PATH) -> None:
        """
        Writes the current state of the statistics to a JSON file
        at the specified file path.

        :param path: str, the file path of the JSON file to write to
        """
        with open(path, 'w') as filehandle:
            json.dump(self.stats, filehandle)

    def _create_json_nesting(self, year, month, day) -> None:
        """
        In case the json nesting for passed year, month, day doesn't exist
        creates a nested dictionary a for storing statistics for
        a specific year, month, and day.

        :param year: str, the year for which to create the dictionary
        :param month: str, the month for which to create the dictionary
        :param day: str, the day for which to create the dictionary
        """
        default_values = {
            "seconds": 0,
            "test_sessions": 0,
            "review_sessions": 0,
            "cards_reviewed": 0
        }
        keys = ['yearly', year, month, day]
        nested_dict = self.stats
        for key in keys:
            nested_dict.setdefault(key, {})
            nested_dict = nested_dict[key]
        if not nested_dict:
            nested_dict.update(default_values)


if __name__ == "__main__":
    instance = StatisticsHandler()
    instance.plot_daily_stats("minutes")
