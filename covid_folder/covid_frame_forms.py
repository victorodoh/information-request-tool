
import tkinter as tk
from utils.tk_label_and_dropdown import tkinter_label, tkinter_menu_dropdown
from utils.clear_frame import clear_window
from utils.get_all_regions import region_list
from covid_folder.functions_for_form import plot_change_and_pct_change, monthly_stop_and_search, plot_compare_two_areas_monthly_cases, plot_area_type
from utils.get_month_as_dict import months_of_the_year

list_of_days = list(range(1, 32))

current_list_of_years = [2020]

list_of_months = list(months_of_the_year().keys())

def plot_area_type_form(window_frame): 
    # this clears any information on the frame before rendering a new widget
    clear_window(window_frame)

    tkinter_label(window_frame, "Select day: ", x=270, y=50)
    day_from = tk.StringVar(window_frame)
    day_from.set(list_of_days[10]) 
    tkinter_menu_dropdown(window_frame, day_from, list_of_days, x=270, y=70)
    
    tkinter_label(window_frame, "Select month: ", x=270, y=120)
    month_var = tk.StringVar(window_frame)
    month_var.set(list_of_months[6])
    tkinter_menu_dropdown(window_frame, month_var, list_of_months, x=270, y=140)
    
    tkinter_label(window_frame, "Select year: ", x=270, y=190)
    year_list = tk.StringVar(window_frame)
    year_list.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_list, current_list_of_years, x=270, y=210)
    
    
    function = lambda: plot_area_type(
        day_from.get(),
        month_var.get(),
        year_list.get(),
    )
    
    tk.Button(window_frame, text="View" , command=function).place(x=270, y=280)
    
def monthly_stop_and_search_form(window_frame):
    clear_window(window_frame)
        
    tkinter_label(window_frame, "Select start month", x=270, y=50)
    start_month_var = tk.StringVar(window_frame)
    start_month_var.set(list_of_months[2])
    tkinter_menu_dropdown(window_frame, start_month_var, list_of_months, x=270, y=70)
    
    tkinter_label(window_frame, "Select end month", x=270, y=120)
    end_month_var = tk.StringVar(window_frame)
    end_month_var.set(list_of_months[8])
    tkinter_menu_dropdown(window_frame, end_month_var, list_of_months, x=270, y=140)
    
    tkinter_label(window_frame, "Year", x=270, y=190)
    year_list = tk.StringVar(window_frame)
    year_list.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_list, current_list_of_years, x=270, y=210)
    
    function = lambda: monthly_stop_and_search(
        start_month_var.get(),
        end_month_var.get(),
        year_list.get(),
    )
    
    tk.Button(window_frame, text="View" , command=function).place(x=270, y=280)
    
    
def change_and_pct_change_form(window_frame):
    
    # this clears any information on the frame before rendering a new widget
    clear_window(window_frame)
    tkinter_label(window_frame, "Select start day", x=180, y=50)
    day_from = tk.StringVar(window_frame)
    day_from.set(list_of_days[3]) 
    tkinter_menu_dropdown(window_frame, day_from, list_of_days, x=180, y=70)
    
    tkinter_label(window_frame, "Select end day", x=370, y=50)
    day_to = tk.StringVar(window_frame)
    day_to.set(list_of_days[16])
    tkinter_menu_dropdown(window_frame, day_to, list_of_days, x=370, y=70)
    
    tkinter_label(window_frame, "Select start month", x=180, y=120)
    month_from = tk.StringVar(window_frame)
    month_from.set(list_of_months[2])
    tkinter_menu_dropdown(window_frame, month_from, list_of_months, x=180, y=140)
    
    tkinter_label(window_frame, "Select end month", x=370, y=120)
    month_to = tk.StringVar(window_frame)
    month_to.set(list_of_months[3])
    tkinter_menu_dropdown(window_frame, month_to, list_of_months, x=370, y=140)
    
    tkinter_label(window_frame, "Select start year", x=180, y=190)
    year_from = tk.StringVar(window_frame)
    year_from.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_from, current_list_of_years, x=180, y=210)
    
    tkinter_label(window_frame, "Select end Year", x=370, y=190)
    year_to = tk.StringVar(window_frame)
    year_to.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_to, current_list_of_years, x=370, y=210)
    
    Regions = tk.StringVar(window_frame)
    Regions.set(region_list()[0])
    tkinter_label(window_frame, text="Select a region: ", x=270, y=260)
    tkinter_menu_dropdown(window_frame, Regions, region_list(), x=250, y=280)
    
    function = lambda: plot_change_and_pct_change(
        day_from.get(),
        day_to.get(),
        month_from.get(),
        month_to.get(),
        year_from.get(),
        year_to.get(),
        Regions.get()
    )
    
    tk.Button(window_frame, text="View" , command=function).place(x=280, y=340)


def compare_two_areas_monthly_cases(window_frame):
    clear_window(window_frame)
    tkinter_label(window_frame, "Select month", x=270, y=50)
    month_var = tk.StringVar(window_frame)
    month_var.set(list_of_months[2])
    tkinter_menu_dropdown(window_frame, month_var, list_of_months, x=270, y=70)
    
    
    tkinter_label(window_frame, "Select year", x=270, y=120)
    year_list = tk.StringVar(window_frame)
    year_list.set(current_list_of_years[0])
    tkinter_menu_dropdown(window_frame, year_list, current_list_of_years, x=270, y=140)
    
    
    tkinter_label(window_frame, "First Region", x=270, y=190)
    region_one = tk.StringVar(window_frame)
    region_one.set(region_list()[0])
    tkinter_menu_dropdown(window_frame, region_one, region_list(), x=270, y=210)
    
    tkinter_label(window_frame, "Second Region", x=270, y=260)
    region_two = tk.StringVar(window_frame)
    region_two.set(region_list()[1])
    tkinter_menu_dropdown(window_frame, region_two, region_list(), x=270, y=280)
    
    
    function = lambda: plot_compare_two_areas_monthly_cases(
        month_var.get(),
        year_list.get(),
        region_one.get(),
        region_two.get()
    )
    
    tk.Button(window_frame, text="View" , command=function).place(x=290, y=340)