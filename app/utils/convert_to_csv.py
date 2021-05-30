import pandas as pd


def convert_to_csv(list: list) -> None:
    columns = [
        "_id",
        "buyer_id",
        "buyer_name",
        "cycle",
        "date",
        "expedition_day",
        "expedition_month",
        "expedition_trimester",
        "expedition_year",
        "tag",

        "Party_name",
        "Party_id",
        "Party_roles",
        "Party_identifier_schema",
        "Party_identifier_uri",
        "Party_street_address",
        "Party_locality_address",
        "Party_region_address",
        "Party_postal_code",
        "Party_country_name",
        "Party_contact_name",
        "Party_contact_email",
        "Party_contact_telephone",
        "Party_contact_fax",
        ]
    info = pd.DataFrame(list,columns=columns)
    info.to_csv("download.csv",index=False)



    """for entry in list:
        
        row = [
            entry[1],
            entry[2],
            entry[3],
            entry[4],
            entry[5],
            entry[6],
            entry[7],
            entry[8],
            entry[9],
            entry[10],
            entry[12],
            entry[13],
            entry[14],
            entry[15],
            entry[16],
            entry[17],
            entry[18],
            entry[19],
            entry[20],
            entry[21],
            entry[22],
            entry[23],
            entry[24],
            entry[25],
        ]
        append_series =  pd.Series(row, index = columns)
        info = info.append(append_series, ignore_index=True)"""
    