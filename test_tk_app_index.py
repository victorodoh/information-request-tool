import pandas as pd
import pytest
import warnings
from utils.tk_label_and_dropdown import tkinter_label, tkinter_menu_dropdown
from utils.get_month_as_dict import months_of_the_year
from utils.get_all_regions import region_list
from utils.get_month_as_dict import months_of_the_year
from police_stop_search.fetch_request import render_police_force_list
from police_stop_search.stop_and_search_frame_form import stop_search_by_age_range_resulting_in_arrest, self_defined_ethnicity, stop_and_search_by_type, legislation_outcome_form
from covid_folder.covid_frame_forms import plot_area_type_form, change_and_pct_change_form, monthly_stop_and_search_form, compare_two_areas_monthly_cases
from covid_folder.functions_for_form import validate_form_inputs
import unittest
import requests
from police_stop_search.fetch_request import return_stop_and_search_cases
from tk_app_index import tk_app

class HelperModules(unittest.TestCase):

    @pytest.mark.asyncio
    # this will start the tkinter window without launching it
    async def _start_app(self):
        self.app.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.app = tk_app()
        self._start_app()

    def tearDown(self):
        self.app.destroy()
    
    ########## this tests verifies if a label from tkinter is returned ##########
    def test_tkinter_label(self):
        Label = tkinter_label(self.app, "This is a test label", 0, 0).winfo_class()
        self.assertEqual(Label, "Label")
    
    ########## this tests verifies that a Menubutton from tkinter is returned ##########
    def test_tkinter_menu_dropdown(self):
        MenuDropdown = tkinter_menu_dropdown(self.app, 10, ["1", "2"], 0, 0).winfo_class()
        self.assertEqual(MenuDropdown, "Menubutton")
        
    ########## this test checks that a dictionary is returned from the months_of_the_year functions ##########
    def test_months_of_the_year(self):
        Months = months_of_the_year()
        self.assertIsInstance(Months, dict)
        
    ########## this tests if data type is a list ##########
    def test_region_list(self):
        RegionList = region_list()
        self.assertIsInstance(RegionList, list)
        
class StopAndSearchModule(unittest.TestCase):
    
    async def _start_app(self):
        self.app.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.app = tk_app()
        self._start_app()

    def tearDown(self):
        self.app.destroy()
        
    ########## this tests that the function to fetch police force returns a dictionary
    def test_PoliceForceDictionary(self):
        PoliceList = render_police_force_list()
        Type = isinstance(PoliceList, dict)
        self.assertEqual(Type, True)
        
    # tests if stop & search api returns a status code of 200
    def test_return_stop_and_search_cases(self):
        response = requests.get("https://data.police.uk/api/stops-force?force=essex&date=2021-06")
        self.assertEqual(response.status_code, 200)
        
        # tests this returns a tuple 
    def test_FetchCasesRequest(self):
        cases = return_stop_and_search_cases("Bedfordshire Police", "2021-07")
        self.assertIsInstance(cases, dict)

    # Checks the length of widgets
    def getFormWidgetLength(self, function, expected):
        Form = self.app.winfo_children()[-1]
        function(Form)
        NoOfWidgetsOnForm = len(Form.winfo_children())
        self.assertEqual(NoOfWidgetsOnForm, expected)
        
    # this tests if all widgets; label, Menubutton, button for plot_area_type_form function renders
    def test_plot_area_type_form(self): 
        self.getFormWidgetLength(plot_area_type_form, 7)
        
    # this tests if all widgets; label, Menubutton, button for change_and_pct_change_form function renders
    def test_plot_area_type_form(self): 
        self.getFormWidgetLength(change_and_pct_change_form, 15)
        
    # this tests if all widgets; label, Menubutton, button for monthly_stop_and_search_form function renders
    def test_monthly_stop_and_search_form(self): 
        self.getFormWidgetLength(monthly_stop_and_search_form, 7)
        
    # this tests if all widgets; label, Menubutton, button for compare_two_areas_monthly_cases function renders
    def test_compare_two_areas_monthly_cases(self): 
        self.getFormWidgetLength(compare_two_areas_monthly_cases, 9)
        

class CovidModules(unittest.TestCase):

    async def _start_app(self):
        self.app.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.app = tk_app()
        self._start_app()

    def tearDown(self):
        self.app.destroy()
        
    # Checks the length of widgets
    def getFormWidgetLength(self, function, expected):
        Form = self.app.winfo_children()[-1]
        function(Form)
        NoOfWidgetsOnForm = len(Form.winfo_children())
        self.assertEqual(NoOfWidgetsOnForm, expected)
        
    # this tests if all widgets; label, Menubutton, button for TwoAreasStopAndSearchArrestResult function renders
    def test_TwoAreasStopAndSearchArrestResult(self): 
        self.getFormWidgetLength(stop_search_by_age_range_resulting_in_arrest, 9)
        
    # this tests if all widgets; label, Menubutton, button for AgeRange function renders
    def test_AgeRange(self): 
        self.getFormWidgetLength(self_defined_ethnicity, 7)
        
    # this tests if all widgets; label, Menubutton, button for stop_and_search_by_type function renders
    def test_stop_and_search_by_type(self): 
        self.getFormWidgetLength(stop_and_search_by_type, 7)
        
    # this tests if all widgets; label, Menubutton, button for TwoAreasStopAndSearchArrestResult function renders
    def test_legislation_outcome_form(self): 
        self.getFormWidgetLength(legislation_outcome_form, 7)

        

if __name__ == "__main__":
    unittest.main(verbosity=2)