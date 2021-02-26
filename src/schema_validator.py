from schemas import Schemas

from schema import Schema
from collections import defaultdict
from datetime import datetime
import json


class SchemaValidator:

    def generate_report(events_count):
        print("Event\t\t\tdate\t\tcount")
        print("-------------------------------------------------------------------")
        for event_name, values in events_count.items():
            for date, count in values.items():
                print("%s\t\t\t%s\t\t%s" % (event_name, date, count))


    if __name__ == "__main__":

        data_path = 'resources/data/'
        data_id = 'input.json'
        schema_data = Schemas.schemas[data_id]
        events_count = {}

        with open(data_path+data_id, 'r') as data:
            for event in data:
                event_dict = json.loads(event)
                try:
                    schema_data.validate(event_dict)
                except Exception as e:
                    print(e)
                    continue
                events_count[event_dict['event']] = defaultdict(int)
                events_count[event_dict['event']][str(datetime.fromisoformat(event_dict['timestamp']).date())] += 1

        generate_report(events_count)
