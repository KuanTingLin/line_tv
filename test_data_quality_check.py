import unittest
from data_quality_check import DataQualityCheck


class TestDataQualityCheck(unittest.TestCase):

    def test_check_event_data_quality_incorrect_data(self):
        test_data = {"ad_network": "FOO",
                     "date": "2019/06/05",
                     "app_name": "",
                     "request": "100",
                     "revenue": "0.00365325",
                     "imp": "abc",
                     "app_version": "1.0.0"}
        event_column_types = {"ad_network": str,
                              "date": DataQualityCheck.check_date_type_with_dash,
                              "app_name": str,
                              "unit_id": int,
                              "request": int,
                              "revenue": float,
                              "imp": int}
        event_data_quality_check = DataQualityCheck(event_column_types)
        self.assertEqual(len(event_data_quality_check.check_event_data_quality(test_data)), 6)
        self.assertEqual(event_data_quality_check.check_event_data_quality(test_data),
                         [{"error_message": "Missing column [{'unit_id'}]"},
                          {"error_message": "Incorrect column [{'app_version'}]"},
                          {"error_message": "column [date] got a wrong data type"},
                          {"error_message": "data of column [app_name] lost"},
                          {"error_message": "column [imp] got a wrong data type"},
                          test_data])

    def test_check_event_data_quality_correct_data(self):
        correct_data = {"ad_network": "FOO",
                        "date": "2019-06-05",
                        "app_name": "LINETV",
                        "unit_id": "55665201314",
                        "request": "100",
                        "revenue": "0.00365325",
                        "imp": "23"}
        event_column_types = {"ad_network": str,
                              "date": DataQualityCheck.check_date_type_with_dash,
                              "app_name": str,
                              "unit_id": int,
                              "request": int,
                              "revenue": float,
                              "imp": int}
        event_data_quality_check = DataQualityCheck(event_column_types)
        self.assertEqual(len(event_data_quality_check.check_event_data_quality(correct_data)), 1)
        self.assertEqual(event_data_quality_check.check_event_data_quality(correct_data)[0], correct_data)

    def test_check_missing_column(self):
        test_data = {"ad_network": "FOO",
                     "date": "2019/06/05",
                     "app_name": "",
                     "request": "100",
                     "revenue": "0.00365325",
                     "imp": "abc",
                     "app_version": "1.0.0"}
        event_column_types = {"ad_network": str,
                              "date": DataQualityCheck.check_date_type_with_dash,
                              "app_name": str,
                              "unit_id": int,
                              "request": int,
                              "revenue": float,
                              "imp": int}
        event_data_quality_check = DataQualityCheck(event_column_types)
        self.assertEqual(event_data_quality_check.check_missing_column(test_data),
                         [{"error_message": "Missing column [{'unit_id'}]"}])

    def test_check_incorrect_column(self):
        test_data = {"ad_network": "FOO",
                     "date": "2019/06/05",
                     "app_name": "",
                     "request": "100",
                     "revenue": "0.00365325",
                     "imp": "abc",
                     "app_version": "1.0.0"}
        event_column_types = {"ad_network": str,
                              "date": DataQualityCheck.check_date_type_with_dash,
                              "app_name": str,
                              "unit_id": int,
                              "request": int,
                              "revenue": float,
                              "imp": int}
        event_data_quality_check = DataQualityCheck(event_column_types)
        self.assertEqual(event_data_quality_check.check_incorrect_column(test_data),
                         [{"error_message": "Incorrect column [{'app_version'}]"}])

    def test_check_incorrect_data(self):
        test_data = {"ad_network": "FOO",
                     "date": "2019/06/05",
                     "app_name": "",
                     "request": "100",
                     "revenue": "0.00365325",
                     "imp": "abc",
                     "app_version": "1.0.0"}
        event_column_types = {"ad_network": str,
                              "date": DataQualityCheck.check_date_type_with_dash,
                              "app_name": str,
                              "unit_id": int,
                              "request": int,
                              "revenue": float,
                              "imp": int}
        event_data_quality_check = DataQualityCheck(event_column_types)
        self.assertEqual(event_data_quality_check.check_incorrect_data(test_data),
                         [{"error_message": "column [date] got a wrong data type"},
                          {"error_message": "data of column [app_name] lost"},
                          {"error_message": "column [imp] got a wrong data type"}])


if __name__ == '__main__':
    unittest.main()

