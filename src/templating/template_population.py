import copy
import re

from src.templating.data_loading import load_data
from src.templating.tempalte_loading import load_template


def get_template_variables(template_str):
    pattern = r'\{\{\s*(\w+)\s*\}\}'
    variables = re.findall(pattern, template_str)
    variables = list(set(variables))
    return variables


def validate_template_variables(vars_and_values):
    for var_name, var_value in vars_and_values.items():
        assert len(var_value.strip()) != 0, f"Data variable {var_name} is empty."


def populate_template(template_str, vars_and_values):
    validate_template_variables(vars_and_values)

    populate_template_str = copy.deepcopy(template_str)
    for var_name, var_value in vars_and_values.items():
        var_search_string = "{{ " + var_name + " }}"
        populate_template_str = populate_template_str.replace(var_search_string, var_value)
    
    return populate_template_str


def get_populated_template(template_category, template_name):
    template_str = load_template(template_category, template_name + ".txt")
    template_variables = get_template_variables(template_str)

    vars_and_values = {}
    for var_name in template_variables:
        data_file_name = var_name + ".txt"
        var_value = load_data(data_file_name)
        vars_and_values[var_name] = var_value
    
    populated_template_str = populate_template(template_str, vars_and_values)
    return populated_template_str
