from statisticshandler import StatisticsHandler
from freezegun import freeze_time
import pytest


@pytest.fixture(autouse=True)
def json_data_setup():
    json_data = {
        "yearly": {
            "2022": {
                "1": {
                    "1": {
                        "hours": 20,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "2": {
                        "hours": 15,
                        "test_sessions": 1,
                        "review_sessions": 2,
                        "cards_reviewed": 3
                    },
                    "3": {
                        "hours": 25,
                        "test_sessions": 3,
                        "review_sessions": 4,
                        "cards_reviewed": 5
                    }
                },
                "2": {
                    "1": {
                        "hours": 18,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "2": {
                        "hours": 22,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "3": {
                        "hours": 22,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    }
                }
            },
            "2023": {
                "1": {
                    "1": {
                        "hours": 24,
                        "test_sessions": 1,
                        "review_sessions": 2,
                        "cards_reviewed": 3
                    },
                    "2": {
                        "hours": 23,
                        "test_sessions": 3,
                        "review_sessions": 4,
                        "cards_reviewed": 5
                    },
                    "3": {
                        "hours": 20,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    }
                },
                "2": {
                    "1": {
                        "hours": 21,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "2": {
                        "hours": 25,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "3": {
                        "hours": 23,
                        "test_sessions": 1,
                        "review_sessions": 2,
                        "cards_reviewed": 3
                    }
                }
            }
        },
        "total": {
            "hours": 10,
            "test_sessions": 2,
            "review_sessions": 3,
            "cards_reviewed": 4
        }
    }
    yield json_data
    json_data = None  # tear down


def test_get_total_stats_returns_correct_values(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    expected_output = (
        "Total hours spent using the app: 10\n"
        "Total test sessions count: 2\n"
        "Total review sessions count: 3\n"
        "Total card reviews count: 4\n"
    )
    assert obj.get_total_stats() == expected_output


def test_get_total_stats_handles_missing_keys(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = {"total": {}}
    expected_output = (
        "Total hours spent using the app: None\n"
        "Total test sessions count: None\n"
        "Total review sessions count: None\n"
        "Total card reviews count: None\n"
    )
    assert obj.get_total_stats() == expected_output


def test_get_monthly_total(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    excepcted_output_1 = (
        "Total hours in month 1 of year 2022: 60\n"
        "Total test sessions in month 1 of year 2022: 6\n"
        "Total review sessions in month 1 of year 2022: 9\n"
        "Total cards reviewed in month 1 of year 2022: 12\n"
    )
    excepcted_output_2 = (
        "Total hours in month 2 of year 2022: 62\n"
        "Total test sessions in month 2 of year 2022: 6\n"
        "Total review sessions in month 2 of year 2022: 9\n"
        "Total cards reviewed in month 2 of year 2022: 12\n"
    )
    assert obj.get_monthly_total('2022', '1') == excepcted_output_1
    assert obj.get_monthly_total('2022', '2') == excepcted_output_2


@freeze_time("Jan 1st, 2022")
def test_update_data_with_existing_key(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    obj.update_data(hours=2, test_sessions=1, review_sessions=1, cards_reviewed=1) # NOQA
    assert obj.stats['yearly']['2022']['1']['1']['hours'] == 22
    assert obj.stats['yearly']['2022']['1']['1']['test_sessions'] == 3
    assert obj.stats['yearly']['2022']['1']['1']['review_sessions'] == 4
    assert obj.stats['yearly']['2022']['1']['1']['cards_reviewed'] == 5
    assert obj.stats['total']['hours'] == 12
    assert obj.stats['total']['test_sessions'] == 3
    assert obj.stats['total']['review_sessions'] == 4
    assert obj.stats['total']['cards_reviewed'] == 5


@freeze_time("Jan 11st, 2022")
def test_update_data_with_non_existing_day_key(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    obj.update_data(hours=2, test_sessions=1, review_sessions=1, cards_reviewed=1) # NOQA
    assert obj.stats['yearly']['2022']['1']['11']['hours'] == 2
    assert obj.stats['yearly']['2022']['1']['11']['test_sessions'] == 1
    assert obj.stats['yearly']['2022']['1']['11']['review_sessions'] == 1
    assert obj.stats['yearly']['2022']['1']['11']['cards_reviewed'] == 1
    assert obj.stats['yearly']['2022']['1']['2']['hours'] == 15
    assert obj.stats['yearly']['2022']['1']['2']['test_sessions'] == 1
    assert obj.stats['yearly']['2022']['1']['2']['review_sessions'] == 2
    assert obj.stats['yearly']['2022']['1']['2']['cards_reviewed'] == 3
    assert obj.stats['total']['hours'] == 12
    assert obj.stats['total']['test_sessions'] == 3
    assert obj.stats['total']['review_sessions'] == 4
    assert obj.stats['total']['cards_reviewed'] == 5


@freeze_time("May 5th, 2022")
def test_update_data_with_non_existing_month_key(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    obj.update_data(hours=2, test_sessions=1, review_sessions=1, cards_reviewed=1) # NOQA
    assert obj.stats['yearly']['2022']['5']['5']['hours'] == 2
    assert obj.stats['yearly']['2022']['5']['5']['test_sessions'] == 1
    assert obj.stats['yearly']['2022']['5']['5']['review_sessions'] == 1
    assert obj.stats['yearly']['2022']['5']['5']['cards_reviewed'] == 1
    assert obj.stats['total']['hours'] == 12
    assert obj.stats['total']['test_sessions'] == 3
    assert obj.stats['total']['review_sessions'] == 4
    assert obj.stats['total']['cards_reviewed'] == 5


@freeze_time("May 5th, 2024")
def test_update_data_with_non_existing_year_key(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    obj.update_data(hours=2, test_sessions=1, review_sessions=1, cards_reviewed=1) # NOQA
    assert obj.stats['yearly']['2024']['5']['5']['hours'] == 2
    assert obj.stats['yearly']['2024']['5']['5']['test_sessions'] == 1
    assert obj.stats['yearly']['2024']['5']['5']['review_sessions'] == 1
    assert obj.stats['yearly']['2024']['5']['5']['cards_reviewed'] == 1
    assert obj.stats['total']['hours'] == 12
    assert obj.stats['total']['test_sessions'] == 3
    assert obj.stats['total']['review_sessions'] == 4
    assert obj.stats['total']['cards_reviewed'] == 5
