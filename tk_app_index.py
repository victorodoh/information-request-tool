from tkinter import ttk
import tkinter as tk
from covid_folder.covid_frame_forms import plot_area_type_form, change_and_pct_change_form, monthly_stop_and_search_form, compare_two_areas_monthly_cases
from police_stop_search.stop_and_search_frame_form import stop_search_by_age_range_resulting_in_arrest, self_defined_ethnicity, stop_and_search_by_type, legislation_outcome_form

def tk_app():

    root = tk.Tk()
    root.geometry("920x730")
    root.title("C2397722")

    tab = ttk.Notebook(root)
    covid_tab_control = tk.Frame(tab)
    stop_and_search_tab_control = tk.Frame(tab)

    tab.add(covid_tab_control, text="Covid visualisation tab")
    tab.add(stop_and_search_tab_control, text="Stop and Search visualisation tab")
    tab.pack(expand=1, fill="both")
 
    tk.Button(covid_tab_control, text="Result of area type on a given day" , command= lambda: plot_area_type_form(covid_form)).place(x=170, y=60)
    tk.Button(covid_tab_control, text= "Change and percentage change in daily cases", command=lambda: change_and_pct_change_form(covid_form)).place(x=420, y=60)
    tk.Button(covid_tab_control, text="Covid cases count by month" , command=lambda: monthly_stop_and_search_form(covid_form)).place(x=200, y=90)
    tk.Button(covid_tab_control, text= "Compare two areas covid cases by month", command=lambda: compare_two_areas_monthly_cases(covid_form)).place(x=425, y=90) 


    #######################################################################################################################################################################################################################################   Covid Visualisation   ####################################################################
    
    
    tk.Button(stop_and_search_tab_control, text="Stop and search result by age range that resulted in arrest" , command=lambda: stop_search_by_age_range_resulting_in_arrest(stop_search_form)).place(x=90, y=60)
    
    tk.Button(stop_and_search_tab_control, text="Result of self defined ethnicity",command=lambda: self_defined_ethnicity(stop_search_form)).place(x=500, y=60)
    tk.Button(stop_and_search_tab_control, text="Stop and search result by legislation" , command=lambda: legislation_outcome_form(stop_search_form)).place(x=150, y=95)
    tk.Button(stop_and_search_tab_control, text="Type of stop and search conducted" , command=lambda: stop_and_search_by_type(stop_search_form)).place(x=430, y=95)
    
    covid_form = tk.Frame(covid_tab_control, width=800, height=550)
    covid_form.place(x=100, y=120)

    stop_search_form = tk.Frame(stop_and_search_tab_control, width=800, height=600)
    stop_search_form.place(x=100, y=125)
    
    return root

if __name__ == "__main__":
    tk_app().mainloop()