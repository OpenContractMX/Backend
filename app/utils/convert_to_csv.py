from app.main import GET_contracts
import pandas as pd


def convert_to_csv(list: list) -> dict:
    # info = pd.DataFrame()
    dict_test = dict()
    dict_test["buyer_name"] = list[0][2]
    return dict_test
