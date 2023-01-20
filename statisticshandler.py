from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
from datetime import datetime
import json


STATISTICS_SOURCEFILE_PATH = "source/stats.json"


def load_stats_data(path=STATISTICS_SOURCEFILE_PATH):
    with open(path, 'r') as filehandle:
        data = json.load(filehandle)
        return data


class StatisticsHandler:
    '''
    This class stores all data about user's learing progress
    and user's usage of the application. It provides all method
    that update the data and dump it to the files.
    '''
    def __init__(self) -> None:
        '''
        Initialization method.
        Calls load_stats_data function so it can store all
        data from the source file to stats attribute
        '''
        self.stats = load_stats_data()

    def get_total_stats(self) -> None:
        """
        Retrieves the total statistics for the user's activity
        such as total hours spent using the app, total test sessions count,
        total review sessions count, and total card reviews count.

        :return: A string representing the total statistics in the format
        """
        total_hours_spent = self.stats['total'].get('hours')
        total_test_session_count = self.stats['total'].get('test_sessions')
        total_review_sessions_count = self.stats['total'].get('review_sessions') # NOQA
        total_cards_review_count = self.stats['total'].get('cards_reviewed')
        return (f"Total hours spent using the app: {total_hours_spent}\n"
                f"Total test sessions count: {total_test_session_count}\n"
                f"Total review sessions count: {total_review_sessions_count}\n"
                f"Total card reviews count: {total_cards_review_count}\n")

    def plot_daily_hours_in_current_month(self, datapiece: str) -> None: # NOQA
        """
        Generates a bar plot that shows the
        daily statistics of a specific data piece for the current month.
        The x-axis represents the days of the current month
        and the y-axis represents the data piece specified by the user.
        The datapiece argument can hold "hours", "review_sessions",
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
        title_string = f"Daily {formatted_string} in " + current_month + " " + current_year # NOQA

        current_month_data = self.stats['yearly'][str(current_date.year)][str(current_date.month)] # NOQA
        x = current_month_data.keys()
        y = [value[datapiece] for value in current_month_data.values()]

        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.bar(x, y, color="blueviolet")
        plt.xlabel('Day', fontsize=9, fontweight='bold')
        plt.ylabel(formatted_string, fontsize=9, fontweight='bold')
        plt.title(title_string, fontsize=16, fontweight='bold')
        plt.grid(True, axis='y')
        plt.xticks(rotation=30, fontsize=6.5)

    def get_monthly_total(self, year: str, month: str) -> str:
        """
        This method calculates the total data
        for a given month in a given year.
        It takes two integer arguments, 'year'
        and 'month' and returns a string
        containing the total hours, total
        test sessions, total review sessions,
        and total cards reviewed during that month and year.

        :param year: an integer representing the year
            for which to calculate the data.
        :param month: an integer representing the month
            for which to calculate the data.
        """
        yearly_stats = self.stats['yearly']
        total_hours = 0
        total_test_sessions = 0
        total_review_sessions = 0
        total_cards_reviewed = 0
        for day in yearly_stats[year][month].keys():
            total_hours += yearly_stats[year][month][day]['hours']
            total_test_sessions += yearly_stats[year][month][day]['test_sessions'] # NOQA
            total_review_sessions += yearly_stats[year][month][day]['review_sessions'] # NOQA
            total_cards_reviewed += yearly_stats[year][month][day]['cards_reviewed'] # NOQA
        return (f"Total hours in month {month} of year {year}: {total_hours}\n" # NOQA
                f"Total test sessions in month {month} of year {year}: {total_test_sessions}\n"  # NOQA
                f"Total review sessions in month {month} of year {year}: {total_review_sessions}\n"  # NOQA
                f"Total cards reviewed in month {month} of year {year}: {total_cards_reviewed}\n")  # NOQA

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
        default_values = {
            "hours": 0,
            "test_sessions": 0,
            "review_sessions": 0,
            "cards_reviewed": 0
        }
        keys = ['yearly', current_year, current_month, current_day]
        nested_dict = self.stats
        for key in keys:
            nested_dict.setdefault(key, {})
            nested_dict = nested_dict[key]
        if not nested_dict:
            nested_dict.update(default_values)

        for key, value in kwargs.items():
            self.stats['yearly'][current_year][current_month][current_day][key] += value # NOQA
            self.stats['total'][key] += value


if __name__ == "__main__":
    instance = StatisticsHandler()
    instance.plot_daily_hours_in_current_month("hours")
    plt.show()
