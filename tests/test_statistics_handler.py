from source.statisticshandler import StatisticsHandler
from freezegun import freeze_time
import pytest


@pytest.fixture(autouse=True)
def json_data_setup():
    json_data = {
        "yearly": {
            "2022": {
                "1": {
                    "1": {
                        "seconds": 72000,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "2": {
                        "seconds": 54000,
                        "test_sessions": 1,
                        "review_sessions": 2,
                        "cards_reviewed": 3
                    },
                    "3": {
                        "seconds": 90000,
                        "test_sessions": 3,
                        "review_sessions": 4,
                        "cards_reviewed": 5
                    }
                },
                "2": {
                    "1": {
                        "seconds": 64800,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "2": {
                        "seconds": 79200,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "3": {
                        "seconds": 79200,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    }
                }
            },
            "2023": {
                "1": {
                    "1": {
                        "seconds": 86400,
                        "test_sessions": 1,
                        "review_sessions": 2,
                        "cards_reviewed": 3
                    },
                    "2": {
                        "seconds": 82800,
                        "test_sessions": 3,
                        "review_sessions": 4,
                        "cards_reviewed": 5
                    },
                    "3": {
                        "seconds": 72000,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    }
                },
                "2": {
                    "1": {
                        "seconds": 75600,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "2": {
                        "seconds": 90000,
                        "test_sessions": 2,
                        "review_sessions": 3,
                        "cards_reviewed": 4
                    },
                    "3": {
                        "seconds": 82800,
                        "test_sessions": 1,
                        "review_sessions": 2,
                        "cards_reviewed": 3
                    }
                }
            }
        },
        "total": {
            "seconds": 36000,
            "test_sessions": 2,
            "review_sessions": 3,
            "cards_reviewed": 4
        }
    }
    yield json_data
    json_data = None  # tear down


def test_get_total_stats(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    expected_output = (
        "Total minutes spent using the app: 600\n"
        "Total test sessions count: 2\n"
        "Total review sessions count: 3\n"
        "Total card reviews count: 4\n"
    )
    assert obj.get_total_stats() == expected_output


def test_get_monthly_total(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    excepcted_output_1 = (
        "Total minutes in January of year 2022: 3600\n"
        "Total test sessions in January of year 2022: 6\n"
        "Total review sessions in January of year 2022: 9\n"
        "Total cards reviewed in January of year 2022: 12\n"
    )
    excepcted_output_2 = (
        "Total minutes in February of year 2022: 3720\n"
        "Total test sessions in February of year 2022: 6\n"
        "Total review sessions in February of year 2022: 9\n"
        "Total cards reviewed in February of year 2022: 12\n"
    )
    assert obj.get_monthly_total(2022, 1) == excepcted_output_1
    assert obj.get_monthly_total(2022, 2) == excepcted_output_2


@freeze_time("Jan 1st, 2022")
def test_update_data_with_existing_key(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    obj.update_data(seconds=2, test_sessions=1, review_sessions=1, cards_reviewed=1) # NOQA
    assert obj.stats['yearly']['2022']['1']['1']['seconds'] == 72002
    assert obj.stats['yearly']['2022']['1']['1']['test_sessions'] == 3
    assert obj.stats['yearly']['2022']['1']['1']['review_sessions'] == 4
    assert obj.stats['yearly']['2022']['1']['1']['cards_reviewed'] == 5
    assert obj.stats['total']['seconds'] == 36002
    assert obj.stats['total']['test_sessions'] == 3
    assert obj.stats['total']['review_sessions'] == 4
    assert obj.stats['total']['cards_reviewed'] == 5


@freeze_time("Jan 11st, 2022")
def test_update_data_with_non_existing_day_key(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    obj.update_data(seconds=2, test_sessions=1, review_sessions=1, cards_reviewed=1) # NOQA
    assert obj.stats['yearly']['2022']['1']['11']['seconds'] == 2
    assert obj.stats['yearly']['2022']['1']['11']['test_sessions'] == 1
    assert obj.stats['yearly']['2022']['1']['11']['review_sessions'] == 1
    assert obj.stats['yearly']['2022']['1']['11']['cards_reviewed'] == 1
    assert obj.stats['yearly']['2022']['1']['2']['seconds'] == 54000
    assert obj.stats['yearly']['2022']['1']['2']['test_sessions'] == 1
    assert obj.stats['yearly']['2022']['1']['2']['review_sessions'] == 2
    assert obj.stats['yearly']['2022']['1']['2']['cards_reviewed'] == 3
    assert obj.stats['total']['seconds'] == 36002
    assert obj.stats['total']['test_sessions'] == 3
    assert obj.stats['total']['review_sessions'] == 4
    assert obj.stats['total']['cards_reviewed'] == 5


@freeze_time("May 5th, 2022")
def test_update_data_with_non_existing_month_key(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    obj.update_data(seconds=2, test_sessions=1, review_sessions=1, cards_reviewed=1) # NOQA
    assert obj.stats['yearly']['2022']['5']['5']['seconds'] == 2
    assert obj.stats['yearly']['2022']['5']['5']['test_sessions'] == 1
    assert obj.stats['yearly']['2022']['5']['5']['review_sessions'] == 1
    assert obj.stats['yearly']['2022']['5']['5']['cards_reviewed'] == 1
    assert obj.stats['total']['seconds'] == 36002
    assert obj.stats['total']['test_sessions'] == 3
    assert obj.stats['total']['review_sessions'] == 4
    assert obj.stats['total']['cards_reviewed'] == 5


@freeze_time("May 5th, 2024")
def test_update_data_with_non_existing_year_key(json_data_setup):
    obj = StatisticsHandler()
    obj.stats = json_data_setup
    obj.update_data(seconds=2, test_sessions=1, review_sessions=1, cards_reviewed=1) # NOQA
    assert obj.stats['yearly']['2024']['5']['5']['seconds'] == 2
    assert obj.stats['yearly']['2024']['5']['5']['test_sessions'] == 1
    assert obj.stats['yearly']['2024']['5']['5']['review_sessions'] == 1
    assert obj.stats['yearly']['2024']['5']['5']['cards_reviewed'] == 1
    assert obj.stats['total']['seconds'] == 36002
    assert obj.stats['total']['test_sessions'] == 3
    assert obj.stats['total']['review_sessions'] == 4
    assert obj.stats['total']['cards_reviewed'] == 5
