from datetime import datetime


class DataQualityCheck:

    def __init__(self, column_types: dict):
        """
        in this case, all the value may be string, but still have it's real data type
        :param column_types: dictionary type, such as {"column_name": str}
        """
        self.column_types = column_types
        self.event_columns = set(column_types.keys())

    @staticmethod
    def check_date_type_with_dash(date_string):
        return datetime.strptime(date_string, "%Y-%m-%d")

    def check_event_data_quality(self, data: dict):
        return self.check_missing_column(data) \
               + self.check_incorrect_column(data) \
               + self.check_incorrect_data(data) \
               + [data]

    def check_missing_column(self, data):
        missing_columns = []
        if self.event_columns.difference(data.keys()):
            missing_column = self.event_columns.difference(data.keys())
            missing_columns.append({"error_message": 'Missing column [{}]'.format(missing_column)})
        return missing_columns

    def check_incorrect_column(self, data):
        incorrect_columns = []
        data_columns = set(data.keys())
        if data_columns.difference(self.event_columns):
            incorrect_column = data_columns.difference(self.event_columns)
            incorrect_columns.append({"error_message": 'Incorrect column [{}]'.format(incorrect_column)})
        return incorrect_columns

    def check_incorrect_data(self, data):
        incorrect_datas = []
        for column_name, column in data.items():
            if column_name in self.column_types:
                if column:
                    try:
                        # 資料型態不正確
                        self.column_types[column_name](column)
                    except ValueError:
                        incorrect_datas.append({"error_message": "column [{}] got a wrong data type".format(column_name)})
                else:
                    # 缺失值
                    incorrect_datas.append({"error_message": 'data of column [{}] lost'.format(column_name)})
        return incorrect_datas


if __name__ == "__main__":
    sample_data = {"ad_network": "FOO",
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
    print(event_data_quality_check.check_event_data_quality(sample_data))