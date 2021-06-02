from app.utils.validate_category import validate_category
from app.utils.validate_month import validate_month
from app.utils.validate_trimester import validate_trimester
from app.utils.validate_year import validate_year
from app.utils.general_contracts_validations import general_contracts_validations
from app.utils.json_formating import json_formating_year
from app.utils.json_formating import json_formating_month_trimester

from datetime import datetime

d1 = datetime.strptime("2018-09-02", "%Y-%m-%d")
d2 = datetime.strptime("2018-09-22", "%Y-%m-%d")

json_form_year =[[123,"4","2","title","comprador","01/09/2018",400000,"MX",d1,d2],[123,"4","2","title","comprador","01/09/2018",400000,"MX",d1,d2]] 
json_form_month =[[42,"Arrendamiento de Vehiculos","Secretaría de Comunicaciones y Transportes","2016-04-27T10:15:30",1595948.0,"MXN"],
                [43,"Convenio de Ampliación en Tiempo y Monto para el Arrendamiento de Vehículos","Secretaría de Comunicaciones y Transportes",
                "2016-04-27T10:15:30",319189.6,"MXN"]]

#Category
def test_should_pass_category_validation():
    assert validate_category("seguridad") == True 

def test_should_pass_category_validation():
    assert validate_category("educacion") == True 

def test_should_pass_category_validation():
    assert validate_category("salud") == True 

def test_should_pass_category_validation():
    assert validate_category("energia") == True 

def test_should_pass_category_validation():
    assert validate_category("economia") == True 

def test_should_pass_category_validation():
    assert validate_category("gobernacion") == True 

def test_should_pass_category_validation():
    assert validate_category("medio_ambiente") == True 

def test_should_pass_category_validation():
    assert validate_category("comunicacion_transporte") == True 

def test_should_pass_category_validation():
    assert validate_category("social") == True 

def test_should_pass_category_validation():
    assert validate_category("investigacion") == True 

def test_should_pass_category_validation():
    assert validate_category("trabajo") == True 

def test_should_not_pass_category_validation():
    assert validate_category("category") == False 


#Month
def test_should_pass_month_validation():
    assert validate_month(0) == True 

def test_should_pass_month_validation():
    assert validate_month(12) == True 

def test_should_not_pass_month_validation():
    assert validate_month(13) == False


#Trimester
def test_should_pass_trimester_validation():
    assert validate_trimester(0) == True

def test_should_pass_trimester_validation():
    assert validate_trimester(4) == True 

def test_should_not_pass_trimester_validation():
    assert validate_trimester(13) == False 


#Year
def test_should_pass_year_validation():
    assert validate_year(2015) == True

def test_should_pass_year_validation():
    assert validate_year(2018) == True 

def test_should_not_pass_year_validation():
    assert validate_year(2000) == False 
    

# Full petition validation
def  test_should_pass_validation():
    
    assert general_contracts_validations("comunicacion_transporte",2016,None,None) == print("Pass validation")

def  test_should_pass_year_json_formating():
    response = json_formating_year(json_form_year)
    assert response == {
                        "contracts_number": 2,
                        "inversion": 800000,
                        "execution_mean": 0.67,
                        "top_ten": [
                        {
                            "id": 123,
                            "month": 4,
                            "trimester": 2,
                            "title": "title",
                            "buyer_name": "comprador",
                            "date": "01/09/2018",
                            "amount": 400000,
                            "currency": "MX"
                        },
                        {
                            "id": 123,
                            "month": 4,
                            "trimester": 2,
                            "title": "title",
                            "buyer_name": "comprador",
                            "date": "01/09/2018",
                            "amount": 400000,
                            "currency": "MX"
                        }
                        ],
                        "months": {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 2,
                        5: 0,
                        6: 0,
                        7: 0,
                        8: 0,
                        9: 0,
                        10: 0,
                        11: 0,
                        12: 0
                        }
                        }



def  test_should_pass_month_trimester_json_formating():
    response = json_formating_month_trimester(json_form_month)
    assert  response == {
                        "contracts": [
                        {
                            "id": 42,
                            "title": "Arrendamiento de Vehiculos",
                            "buyer_name": "Secretaría de Comunicaciones y Transportes",
                            "date": "2016-04-27T10:15:30",
                            "amount": 1595948.0,
                            "currency": "MXN"
                        },
                        {
                            "id": 43,
                            "title": "Convenio de Ampliación en Tiempo y Monto para el Arrendamiento de Vehículos",
                            "buyer_name": "Secretaría de Comunicaciones y Transportes",
                            "date": "2016-04-27T10:15:30",
                            "amount": 319189.6,
                            "currency": "MXN"
                        }
                        ],
                        "contracts_number": 2
                    }