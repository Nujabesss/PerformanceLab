import json
import sys
def report(values, tests, report):
        with open(values, 'r', encoding='utf-8') as f:
            values_data = json.load(f)
        with open(tests, 'r', encoding='utf-8') as f:
            tests_data = json.load(f)
        values_lookup = {item['id']: item['value'] for item in values_data['values']}
        def populate_values(tests_structure):
            for item in tests_structure:
                if 'id' in item and item['id'] in values_lookup:
                    item['value'] = values_lookup[item['id']]
                if 'values' in item:
                    populate_values(item['values'])
        populate_values(tests_data['tests'])
        with open(report, 'w', encoding='utf-8') as f:
            json.dump(tests_data, f, indent=4)

values=  sys.argv[1]
tests = sys.argv[2]
reports = sys.argv[3]

report(values, tests,reports)