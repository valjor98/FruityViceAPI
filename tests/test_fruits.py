import os
import csv
from pytest_bdd import scenario, given, when, then
import pytest
from FruityViceAPI.script import fetch_and_export_to_csv

def teardown_function():
    if os.path.exists('test_family.csv'):
        os.remove('test_family.csv')
    if os.path.exists('test_genus.csv'):
        os.remove('test_genus.csv')

# Gherkin Scenarios
@scenario('test_fruits.feature', 'Fetch fruits by family')
def test_fetch_by_family():
    pass

@scenario('test_fruits.feature', 'Fetch fruits by genus')
def test_fetch_by_genus():
    pass

@given("I have a valid base URL")
def valid_base_url():
    pass

@when('I request fruits from the family "Rosaceae"')
def fetch_by_family():
    fetch_and_export_to_csv(filename='test_family.csv', family='Rosaceae')

@when('I request fruits from the genus "Malus"')
def fetch_by_genus():
    fetch_and_export_to_csv(filename='test_genus.csv', genus='Malus')

@then("I should receive a list of fruits from that family")
def check_fruits_by_family():
    assert os.path.exists('test_family.csv')
    
    with open('test_family.csv', 'r') as f:
        reader = csv.DictReader(f)
        fruits = list(reader)

    for fruit in fruits:
        assert fruit['family'] == 'Rosaceae'
    teardown_function()

@then("I should receive a list of fruits from that genus")
def check_fruits_by_genus():
    assert os.path.exists('test_genus.csv')
    
    with open('test_genus.csv', 'r') as f:
        reader = csv.DictReader(f)
        fruits = list(reader)

    for fruit in fruits:
        assert fruit['genus'] == 'Malus'
    teardown_function()
