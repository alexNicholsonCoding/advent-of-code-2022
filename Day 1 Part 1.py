"""Advent of Code Day 1
Created by Alex 02/12/22"""

#Open text file in read mode
input_day1 = open("input_day1.txt", "r")

#Read file:
cals_text = input_day1.read()



def highest_cal(cals):
    temp_total = 0
    high_total = 0

    # splitting the file data into lines
    for line in cals_text:
        cal_lines = cals_text.split('\n\n')
        for group in cal_lines:
            split_group = group.split()
            temp_group = []
            for cal in split_group:
                temp_group.append(int(cal))
            temp_total = sum(temp_group)
            print(temp_total)
            if temp_total >= high_total:
                high_total = temp_total

    print(high_total)
    return (high_total)

highest_cal(cals_text)

