from heapq import nlargest

def json_formating_year(result):
    json = dict()
    json['contracts'] = list()
    invertion = 0
    time_differences = list()
    months = list()
    for entry in result:
        if entry[7] == "TEST":
            pass
        else:
            json_entry = dict()
            json_entry['id'] = entry[0]
            json_entry['month'] = int(entry[1])
            json_entry['trimester'] = int(entry[2])
            json_entry['title'] = entry[3]
            json_entry['buyer_name'] = entry[4]
            json_entry['date'] = entry[5]
            json_entry['amount'] = entry[6]
            json_entry['currency'] = entry[7]
            json['contracts'].append(json_entry)
            invertion += entry[6]
            time_differences.append((entry[9]-entry[8]).days)
            months.append(int(entry[1]))
    json['contracts_number'] = len(result)
    json['inversion'] =  round(invertion, 2)
    json['execution_mean'] = round( (sum(time_differences)/len(result))/30, 2)
    top_ten = nlargest(10, json['contracts'], key=lambda item: item["amount"])
    json["top_ten"] = top_ten
    json["months"] = CountFrequency(months)
    json.pop("contracts", None)
    return json

def json_formating_month_trimester(result):
    json = dict()
    json['contracts'] = list()
    for entry in result:
        if entry[5] == "TEST":
            pass
        else:
            json_entry = dict()
            json_entry['id'] = entry[0]
            json_entry['title'] = entry[1]
            json_entry['buyer_name'] = entry[2]
            json_entry['date'] = entry[3]
            json_entry['amount'] = entry[4]
            json_entry['currency'] = entry[5]
            json['contracts'].append(json_entry)
    json['contracts_number'] = len(result)
    return json


def CountFrequency(my_list):
  
    freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq