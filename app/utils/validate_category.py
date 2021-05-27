def validate_category(category):
    
    valid_categories = ["seguridad","salud","energia","economia","gobernacion","medio_ambiente","comunicacion_transporte","social","investigacion","trabajo"]
    
    if category in valid_categories:
        return True

    return False
