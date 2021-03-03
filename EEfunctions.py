#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:32:48 2021

@author: benjaminlow
"""

"Energy Expenditure functions"

def Overal_EE_high(HR_lst, RestingHR, Weight):
    for i in HR_lst:
        EE_sum = 0
        EE_sum = EE_sum + 1.012 - 0.0154 * (i-RestingHR) + 0.01140 * Weight + 0.00192 * (i - RestingHR) * Weight
    return EE_sum

#def EE_high(HR_lst,)
def EE_high_lst(HR_lst, RestingHR, Weight):
    EE_lst = []
    for i in range(len(HR_lst)):
        HRnet = HR_lst[i]  - RestingHR
        EE_data = 1.012 - 0.0154 * HRnet + 0.01140 * Weight + 0.00192 * HRnet * Weight
        EE_lst.append(EE_data)
    return EE_lst




def EE_lowActivity_HRnet_M(Heartrate_lst, weight):
    for i in Heartrate_lst:
        HR = i    
        EE = float(0.438 + 0.0210 * HR + 0.00750 * weight + 0.00122 * HR * weight)
        EE_heartrate = []
        EE_heartrate[i] = EE
    return EE_heartrate