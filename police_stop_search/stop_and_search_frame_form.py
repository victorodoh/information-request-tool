import tkinter as tk
from utils.tk_label_and_dropdown import tkinter_label, tkinter_menu_dropdown
from police_stop_search.fetch_request import render_police_force_list
from police_stop_search.functions_for_form import plot_stop_search_by_age_range_resulting_in_arrest, plot_self_defined_ethnicity, plot_legislation_outcome, plot_stop_and_search_by_type
from utils.clear_frame import clear_window
from datetime import date
from utils.get_month_as_dict import months_of_the_year

list_of_months = list(months_of_the_year().keys())
current_list_of_years = [2020, 2021, 2022]

def stop_search_by_age_range_resulting_in_arrest(window_frame):
    clear_window(window_frame)
    
    tkinter_label(window_frame, "Select month: ", x=240, y=70)
    month_var = tk.StringVar(window_frame)
    month_var.set(list_of_months[0]) 
    tkinter_menu_dropdown(window_frame, month_var, list_of_months, x=240, y=95)
    
    tkinter_label(window_frame, "Select year: ", x=240, y=145)
    year_var = tk.StringVar(window_frame)
    year_var.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_var, current_list_of_years, x=240, y=170)
    
    police_force_list = list(render_police_force_list().keys())
    tkinter_label(window_frame, "Select police force: ", x=240, y=225)
    get_police_force = tk.StringVar(window_frame)
    get_police_force.set(police_force_list[0])
    tkinter_menu_dropdown(window_frame, get_police_force, police_force_list, x=240, y=250)
    
    function = lambda: plot_stop_search_by_age_range_resulting_in_arrest(
        month_var.get(),
        year_var.get(),
        get_police_force.get(),
    )
    
    tk.Button(window_frame, text="view result" , command=function).place(x=240, y=320)

def self_defined_ethnicity(window_frame):
    clear_window(window_frame)
    
    tkinter_label(window_frame, "Select month: ", x=240, y=70)
    month_var = tk.StringVar(window_frame)
    month_var.set(list_of_months[0]) 
    tkinter_menu_dropdown(window_frame, month_var, list_of_months, x=240, y=95)

    tkinter_label(window_frame, "Select year: ", x=240, y=145)
    year_var = tk.StringVar(window_frame)
    year_var.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_var, current_list_of_years, x=240, y=170)
    
    render_police_force_list = list(render_police_force_list().keys())
    tkinter_label(window_frame, "Select police force: ", x=240, y=225)
    get_police_force = tk.StringVar(window_frame)
    get_police_force.set(render_police_force_list[0])
    tkinter_menu_dropdown(window_frame, get_police_force, render_police_force_list, x=240, y=250)
    
    function = lambda: plot_self_defined_ethnicity(
        month_var.get(),
        year_var.get(),
        get_police_force.get(),
    )
    
    tk.Button(window_frame, text="view result of self defined ethnicity" , command=function).place(x=240, y=320)
    
def legislation_outcome_form(window_frame):
    clear_window(window_frame)
    
    tkinter_label(window_frame, "Select month: ", x=240, y=70)
    month_var = tk.StringVar(window_frame)
    month_var.set(list_of_months[0]) 
    tkinter_menu_dropdown(window_frame, month_var, list_of_months, x=240, y=95)

    tkinter_label(window_frame, "Select year: ", x=240, y=145)
    year_var = tk.StringVar(window_frame)
    year_var.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_var, current_list_of_years, x=240, y=170)
    
    police_force_list = list(render_police_force_list().keys())
    tkinter_label(window_frame, "Select police force: ", x=240, y=225)
    get_police_force = tk.StringVar(window_frame)
    get_police_force.set(police_force_list[0])
    tkinter_menu_dropdown(window_frame, get_police_force, police_force_list, x=240, y=250)
    
    function = lambda: plot_legislation_outcome(
        month_var.get(),
        year_var.get(),
        get_police_force.get(),
    )
    
    tk.Button(window_frame, text="view result" , command=function).place(x=240, y=320)
    

def stop_and_search_by_type(window_frame):
    clear_window(window_frame)
    
    tkinter_label(window_frame, "Select month: ", x=240, y=70)
    month_var = tk.StringVar(window_frame)
    month_var.set(list_of_months[0]) 
    tkinter_menu_dropdown(window_frame, month_var, list_of_months, x=240, y=95)

    tkinter_label(window_frame, "Select year: ", x=240, y=145)
    year_var = tk.StringVar(window_frame)
    year_var.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_var, current_list_of_years, x=240, y=170)
    
    list_of_police_force = list(render_police_force_list().keys())
    tkinter_label(window_frame, "select police force: ", x=240, y=225)
    get_police_force = tk.StringVar(window_frame)
    get_police_force.set(list_of_police_force[0])
    tkinter_menu_dropdown(window_frame, get_police_force, list_of_police_force, x=240, y=250)
    
    function = lambda: plot_stop_and_search_by_type(
        month_var.get(),
        year_var.get(),
        get_police_force.get(),
    )
    
    tk.Button(window_frame, text="view stop and search by type" , command=function).place(x=240, y=320)