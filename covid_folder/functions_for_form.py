import pandas as pd
import datetime as dt
import numpy as np
from chart_functions import Lollipop, tree_map, donut_chart, area_graph, pie_chart
from tkinter import messagebox
from utils.get_month_as_dict import months_of_the_year
from utils.get_all_regions import region_list

covid_df = pd.read_csv('covid_dataset/specimenDate_ageDemographic-unstacked.csv', low_memory=False)

# select only needed columns
covid_df = covid_df[["areaType", "areaCode", "areaName", "date", "newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+"]]

# total cases per day
covid_df["newCasesBySpecimenDate-Total"] = (covid_df["newCasesBySpecimenDate-0_59"] + covid_df["newCasesBySpecimenDate-60+"])

# replace missing values
covid_df.replace([np.inf, -np.inf], np.nan, inplace=True)
covid_df.fillna(0, inplace=True)

# get daily percent change in infection rate 
covid_df["%changeInfectionRate-Total"] = (covid_df.groupby("areaName")["newCasesBySpecimenDate-Total"].pct_change() * 100)
covid_df["%changeInfectionRate-60+"] = (covid_df.groupby("areaName")["newCasesBySpecimenDate-60+"].pct_change() * 100)
covid_df["%changeInfectionRate-0_59"] = (covid_df.groupby("areaName")["newCasesBySpecimenDate-0_59"].pct_change() * 100)

# convert values for the date column to datetime
covid_df["date"] = pd.to_datetime(covid_df["date"])

def validate_form_inputs( day_from, day_to, month_from, month_to, year_from, year_to ):
    try:
        date_from_val = dt.datetime( day=int(day_from),month=int(months_of_the_year()[month_from]),year=int(year_from) )
        date_to_val = dt.datetime( day=int(day_to), month=int(months_of_the_year()[month_to]), year=int(year_to) )  
    except:
        messagebox.showinfo("showinfo", "you have entered an invalid date")
        
    if date_from_val > date_to_val:
       return messagebox.showinfo("showinfo", "Error!! end date cannot be before start date!")
    else:
        return { "date_from": date_from_val, "date_to" : date_to_val }
  

def plot_area_type(day_from, selected_month, selected_year):
    date_range = validate_form_inputs(day_from, day_to="1", month_from=selected_month, year_from=selected_year, month_to="December", year_to="2020")
        
    if type(date_range) is dict: 
        date_from = date_range["date_from"]
        df = covid_df.loc[((covid_df["date"] == date_from))]
        if(len(df) <= 0):
            return messagebox.showinfo("showinfo", "There is no data available for this day")
        else:
            df = df.groupby(["areaType"], as_index=False)[[ "newCasesBySpecimenDate-Total"]].sum()
            df = df[["areaType","newCasesBySpecimenDate-Total"]]
            
            graph_title =  "Covid cases by area type for " + day_from + "/" + selected_month + "/" + selected_year 
            colors = np.array(["blue", "orange",  "gold", "#E6CCB2", "brown"])
            explode = (0.05, 0.05, 0.05, 0.08, 0.05)

            donut_chart(graph_title, df["newCasesBySpecimenDate-Total"], df["areaType"], colors, explode)
            
def monthly_stop_and_search( month_from, month_to, selected_year):
    date_range = validate_form_inputs("1", "1", month_from=month_from, month_to=month_to, year_from=selected_year, year_to="2020")
    if month_from == month_to:
        return messagebox.showinfo("showinfo", "can't compare same month")
    elif type(date_range) is dict: 
        
        date_range_date_from = date_range["date_from"]
        date_range_date_to = date_range["date_to"]

        chart_title =  "Total monthly cases from " + month_from + " to " + month_to + ", " + selected_year
        df = covid_df.loc[(covid_df["date"] >= date_range_date_from) & (covid_df["date"] <= date_range_date_to)]
        df = covid_df.groupby(df['date'])['newCasesBySpecimenDate-Total'].sum().sort_values()
        df = df.reset_index()
        df['months'] = pd.DatetimeIndex(df['date']).month_name()
        df = df.groupby('months')['newCasesBySpecimenDate-Total'].sum()
        df = df.reset_index()
        labels = df.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
        tree_map(chart_title, df["newCasesBySpecimenDate-Total"], labels )
    else:
        return messagebox.showinfo("showinfo", "Invalid date selected")
            
    
def plot_change_and_pct_change(day_from, day_to, month_from, month_to, year_from, year_to, selected_region):
    date_range = validate_form_inputs(day_from, day_to, month_from, month_to, year_from, year_to)
    
    if selected_region not in region_list():
        return messagebox.showinfo("showinfo", "Invalid region selected.")
        
    if type(date_range) is dict: 
        date_from = date_range["date_from"]
        date_to = date_range["date_to"]
        df = covid_df.loc[((covid_df["areaName"] == selected_region) & (covid_df["date"] >= date_from) & (covid_df["date"] <= date_to))]
        
        if(len(df) <= 0):
            return messagebox.showinfo("showinfo", "No data available for this range")
        
        chart_title =  "Daily and percentage change in covid cases for " + selected_region + " from " + day_from + "-" +  month_from + "-" + year_from + " to " + day_to + "-" + month_to + "-" + year_to
        
        area_graph(chart_title, "Change in total daily cases", "Percentage change in total daily cases by age group", df, "date", "%changeInfectionRate-Total", "Total daily cases", "%changeInfectionRate-0_59", "%changeInfectionRate-60+", "cases count", legends=["Age Group 0-59", "Age Group 60+"])
    
    

def plot_compare_two_areas_monthly_cases( selected_month, selected_year, region_one, region_two):
    date_range = validate_form_inputs("1", "1", selected_month, "December", selected_year, selected_year)
    
    if region_one == region_two:
        return messagebox.showinfo("showinfo", "You cannot compare values from the same region")
    
    if type(date_range) is dict: 
        # date_from = date_range["date_from"]
        chart_title =  "Total cases between " + region_one + " and " + region_two + " in " +  selected_month + " , 2020"
        
        region_one_df = covid_df.loc[(covid_df['areaName'] == region_one)]
        region_two_df = covid_df.loc[(covid_df['areaName'] == region_two)]
        
        region_one_df['month'] = pd.DatetimeIndex(region_one_df['date']).month_name()
        region_one_df = region_one_df.groupby('month')['newCasesBySpecimenDate-Total'].sum()
        region_one_df = region_one_df.reset_index()
        
        region_two_df['month'] = pd.DatetimeIndex(region_two_df['date']).month_name()
        region_two_df = region_two_df.groupby('month')['newCasesBySpecimenDate-Total'].sum()
        region_two_df = region_two_df.reset_index()
        
        region_one_df = region_one_df[(region_one_df['month'] == selected_month)]
        region_two_df = region_two_df[(region_two_df['month'] == selected_month)]
        
        if(len(region_one_df) <= 0) or (len(region_two_df) <= 0):
            return messagebox.showinfo("showinfo", "No data available for this month")
        else:
            pie_chart(chart_title, [region_one_df.iloc[0]['newCasesBySpecimenDate-Total'],region_two_df.iloc[0]['newCasesBySpecimenDate-Total']], [region_one,
region_two])

