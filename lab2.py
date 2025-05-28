import math
import statistics
import random


def main(): 
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
    display_main_menu() 
    num_list = get_user_input() 
    print(num_list)
    print("average = " + str(statistics.mean(num_list)))
    print("min = " + str(min(num_list)))
    print("max = " + str(max(num_list)))
    print("sum = " + str(sum(num_list)))
    print("std dev = " + str(statistics.stdev(num_list)))
    print("variance = " + str(statistics.variance(num_list)))
    
    
def display_main_menu(): #print out the name of the lab and prompt user for input
    print("Enter some numbers separated by commas (e.g. 5, 67, 32, 12): ")
    return 

def get_user_input(): #get user input and convert it to a list of floats
    number_input = input()
    input_list = number_input.split(",")
    float_list = list(map(float, input_list))
    return float_list
    
def calc_average_temperature( tempList): #calculate the average temperature from a list of temperatures
    return round(sum(tempList)/len(tempList), 2)

def calc_min_max_temperature(tempList): #calculate the minimum and maximum temperature from a list of temperatures
    min_max_list = [min(tempList), max(tempList)]
    return min_max_list

def sort_temperature_list(tempList): #sort the list of temperatures in ascending order
    return sorted(tempList)

def calc_median_temperature(tempList):# calculate the median temperature from a list of temperatures
    sorted_list = sorted(tempList)
    i = len(sorted_list)
    mid = i // 2
    if i % 2 == 0:
        return round(((sorted_list[mid - 1] + sorted_list[mid]) / 2), 2)
    else:
        return sorted_list[mid]


def calc_median_temperature_stat(tempList):
    return statistics.median(tempList)


if __name__ == "__main__": 
    main() 

    