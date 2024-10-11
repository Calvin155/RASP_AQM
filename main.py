import random
import time
from app.influx_database.influx import InfluxDBHandler

influx_db = InfluxDBHandler()
print("Starting Test")
while True:
    random_integer = random.randint(1, 500)
    influx_db.random_num_test(random_integer)
    print(random_integer)
    print("Successfully Written To RSP_1 AQM Database")
    time.sleep(5)
##Calvin