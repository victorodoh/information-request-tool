from tkinter import messagebox
import pandas as pd
from police_stop_search.fetch_request import return_stop_and_search_cases
from utils.get_month_as_dict import months_of_the_year
import numpy as np
from chart_functions import horizontal_lollipop_chart, bar_chart_, scattered_plot, pie_chart, donut_chart
 

def get_stop_search_cases(selected_month, selected_year, selected_police_force):
    date = selected_year + "-" + months_of_the_year()[selected_month]
    # this function returns a dictionary with a length of two
    result = return_stop_and_search_cases(selected_police_force, date)["data"]
    if result == []:
        return messagebox.showinfo("showinfo", "There is no data for this  month selected")
    else: 
        return result
    
def plot_self_defined_ethnicity(selected_month, selected_year, police_force_selected):
    df = pd.DataFrame.from_dict(get_stop_search_cases(selected_month, selected_year, police_force_selected))
    outcome = df.groupby(['self_defined_ethnicity'], as_index=False).count()
    graph_title = "Stop and search cases of self defined ethnicity for " + police_force_selected + " in " + selected_month + ", " + selected_year
    bar_chart_(graph_title, outcome, outcome["involved_person"], outcome["self_defined_ethnicity"] )

def plot_legislation_outcome(selected_month, selected_year, selected_police_force):
    df = pd.DataFrame.from_dict(get_stop_search_cases(selected_month, selected_year, selected_police_force))
    outcome = df.groupby(['legislation'], as_index=False).count()
    title = "Stop and search cases by legislation \n for " + selected_police_force + " in " + selected_month + ", " + selected_year
    if len(outcome["involved_person"]) == 3:
        colors = np.array(["#94D2BD","gold", "#FFB703"])
    elif len(outcome["involved_person"]) == 3:
        colors = np.array(["#94D2BD","gold", "#FFB703", "#E6CCB2"])
    elif len(outcome["involved_person"]) == 5:
        colors = np.array(["#94D2BD","gold", "#FFB703", "#E6CCB2", "#9B2226"])
        
    scattered_plot(title, outcome["legislation"], outcome["involved_person"], colors)
    
def plot_stop_and_search_by_type(selected_month, selected_year, police_force_selected):
    df = pd.DataFrame.from_dict(get_stop_search_cases(selected_month, selected_year, police_force_selected))
    outcome = df.groupby(["type"], as_index=False)[["involved_person"]].count()
    chart_title = "Stop and Search Cases Breakdown by Ethnicity \nfor " + police_force_selected + " in " + selected_month + ", " + selected_year
    pie_chart(chart_title, outcome["involved_person"], outcome["type"])
    
    
def plot_stop_search_by_age_range_resulting_in_arrest(Month, Year, SelectedPoliceForce):
    df = pd.DataFrame.from_dict(get_stop_search_cases(Month, Year, SelectedPoliceForce))
    df = df.loc[df['outcome'] == "Arrest"]
    df = df.reset_index()
    outcome = df.groupby(["age_range"], as_index=False)[["involved_person"]].count()
    title = "Stop and search cases by age range that resulted in arrest for \n " + SelectedPoliceForce + " in " + Month + ", " + Year
    maximum_value=outcome.max()
    # determine the max value in the data
    maximum = maximum_value['involved_person'] 
        
    horizontal_lollipop_chart(outcome.index, outcome["involved_person"], outcome["age_range"], maximum, graph_title=title, data=outcome)
    