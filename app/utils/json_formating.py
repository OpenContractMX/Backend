def json_formating(result):
    json = dict()
    json['contracts'] = list()
    invertion = 0
    time_differences = list()
    for entry in result:
        json_entry = dict()
        json_entry['id'] = entry[0]
        json_entry['month'] = entry[1]
        json_entry['trimester'] = entry[2]
        json_entry['title'] = entry[3]
        json_entry['buyer_name'] = entry[4]
        json_entry['date'] = entry[5]
        json_entry['amount'] = entry[6]
        json_entry['currency'] = entry[7]
        json['contracts'].append(json_entry)
        invertion += entry[6]
        time_differences.append((entry[9]-entry[8]).days)
    json['contracts_number'] = len(result)
    json['inversion'] =  round(invertion, 2)
    json['execution_mean'] = sum(time_differences)/len(result)
    return json