from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

INFLUX_URL = "http://192.168.1.23:8086"
INFLUX_TOKEN = "Hhu1M0J0xkpwyJVWkPENnlkj1W5XmKY3QBOPJr_5txwvNRmS1eNY5X98qrSdQQb588I5L0JmpEXsLMBLJL6Vjw=="
INFLUX_ORG = "AQM"
INFLUX_BUCKET = "Air_Quality_Metrics"
INFLUX_PORT = 8086

class InfluxDBHandler:
    def __init__(self):
        self.url = INFLUX_URL
        self.token = INFLUX_TOKEN
        self.org = INFLUX_ORG
        self.bucket = INFLUX_BUCKET
        self.port = INFLUX_PORT
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def random_num_test(self, rand_num):
        try:
            point = Point("Air Quality Limerick").tag("location", "Limerick").field("temperature", rand_num)
            self.write_api.write(bucket=self.bucket, org=self.org, record=point)
            print(f"Successfully wrote: {rand_num}")
        except Exception as ex:
            print("Error Writing to Database: " + str(ex))
