import json  # for working with json
import pprint  # for pretty printing

if __name__ == '__main__':
    with open('database.json', 'r') as iowrap:
        json_data = json.load(iowrap)
    pp = pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None)
    pp.pprint(json_data)
    # alternatively, save the data with intend
    ## with open('database_pretty.json', 'w') as iowrap:
        ##json.dump(json_data, iowrap, indent=4)
