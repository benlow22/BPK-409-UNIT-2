#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:42:43 2021

@author: benjaminlow
"""

"""Import Libraries"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import Lab2FunctionsNoPlot as l2f
import EEfunctions as EE



"MAIN CODE SUBMISSIO 1.0"

#Question 1 - diagram

#Question 2 - Each member's Resting HR

"""Import resting File"""

column_names = [
    "ecg",
    "t"
]

restingecg_Ben = pd.read_csv("Lab2RestingData_Ben.txt",
    names = column_names, sep = '\t', skiprows = 5000, skipfooter = 5000, engine = 'python')

# Change time to seconds
        #Ben
restingecg_Ben.t = restingecg_Ben.t/1000
Wn = 0.1
b, a = scipy.signal.butter(4, Wn, 'low', analog = False)
filt_restingecg_Ben = scipy.signal.filtfilt(b, a, restingecg_Ben.ecg)
plt.figure(1)
plt.plot(restingecg_Ben.t, restingecg_Ben.ecg, color = "b", label = 'Raw ECG')
plt.plot(restingecg_Ben.t, filt_restingecg_Ben, color = "orange", label = ' Filtered ECG')
plt.xlim([43,48])
plt.xlabel('Time [s]')  
plt.ylabel('ECG Amplitude [mV]')
plt.title("Q2 Ben's ECG Measure")
plt.legend()


        #Chase
restingecg_Chase = pd.read_csv('RestingECGLab2_Chase.txt',
                         names=column_names, sep = '\t', skiprows= 10000, skipfooter= 5000, engine = 'python')
restingecg_Chase.t = restingecg_Chase.t/1000

Wn = 0.1
b, a = scipy.signal.butter(4, Wn, 'low', analog = False)
filt_restingecg_Chase = scipy.signal.filtfilt(b, a, restingecg_Chase.ecg)


plt.figure(2)
plt.plot(restingecg_Chase.t, restingecg_Chase.ecg, label = 'Raw ECG')
plt.plot(restingecg_Chase.t, filt_restingecg_Chase, label = 'Filtered ECG')
plt.axis([320, 325, 270, 410])
plt.title("Q2 Chase's Resting ECG Measure")
plt.xlabel("Time (s)")
plt.ylabel("ECG Amplitude (mV)")
plt.legend()


        #Eugene
file = 'Lab2RestingECG_Eugene.txt'

restingecg_Eugene = pd.read_csv(file, names = column_names, sep = '\t', skiprows= 5000, skipfooter= 5000, engine = 'python')

#change time to seconds
restingecg_Eugene.t = restingecg_Eugene.t/1000

Wn = 0.1
b, a = scipy.signal.butter(4, Wn, 'low', analog = False)
filt_restingecg_Eugene = scipy.signal.filtfilt(b, a, restingecg_Eugene.ecg)

plt.figure(3)
plt.plot(restingecg_Eugene.t, restingecg_Eugene.ecg, label = 'Raw ECG')
plt.plot(restingecg_Eugene.t, filt_restingecg_Eugene, label = 'Filtered ECG')
plt.xlim([100,105])
plt.xlabel('Time (sec)')  
plt.ylabel('ECG Amplitude (mV)')
plt.title("Q2 Eugene's Resting ECG Measure")
plt.legend()

#Jakob
restingecg_Jakob = pd.read_csv('Lab2Part1_4JAKOB1.txt',
                         names=column_names, sep = '\t', skiprows= 60600, skipfooter= 17000, engine = 'python')
restingecg_Jakob.t = restingecg_Jakob.t/1000

Wn = 0.1
b, a = scipy.signal.butter(4, Wn, 'low', analog = False)
filt_restingecg_Jakob = scipy.signal.filtfilt(b, a, restingecg_Jakob.ecg)


plt.figure(4)
plt.plot(restingecg_Jakob.t, restingecg_Jakob.ecg, label = 'Raw ECG')
plt.plot(restingecg_Jakob.t, filt_restingecg_Jakob, label = 'Filtered ECG')
plt.axis([590, 595, 280, 370])
plt.title("Q2 Jakob's Resting ECG Measure")
plt.xlabel("Time (s)")
plt.ylabel("ECG Amplitude (mV)")
plt.legend()

#question 3 - written

#Question 4 - 5s if Chase filtered ECG with peaks
peaks,_ = scipy.signal.find_peaks(filt_restingecg_Chase, height = 380)

plt.figure(5)
plt.plot(restingecg_Chase.t, filt_restingecg_Chase, label = 'Filtered ECG')
plt.plot(restingecg_Chase.t[peaks], filt_restingecg_Chase[peaks], "x", label = 'R-Wave Peak')
plt.axis([320, 325, 270, 410])
plt.title("Q4 Filtered ECG Signal with R-Wave Peaks Labelled")
plt.xlabel("Time (s)")
plt.ylabel("ECG Amplitude (mV)")
plt.legend(loc = 'right')

#Question5 - each member's mean HR, HRV(SD)

# Chase's HR
d_ecg, peaks_d_ecg = l2f.decg_peaks(restingecg_Chase.ecg, restingecg_Chase.t)
Rwave_peaks_d_ecg = l2f.d_ecg_peaks(d_ecg, peaks_d_ecg, restingecg_Chase.t, 0.4, 0.5)
restingecg_Rwave_t = l2f.Rwave_peaks(restingecg_Chase.ecg, d_ecg, Rwave_peaks_d_ecg, restingecg_Chase.t)
RR_interval = np.diff(restingecg_Rwave_t)
plt.plot(RR_interval)
heartrate_resting_Chase = (1/RR_interval)*60
Wn = 0.2
b2, a2 = scipy.signal.butter(4, Wn, 'low', analog = False) #find a good value for Wn
filt_heartrate_Chase = scipy.signal.filtfilt(b2, a2, heartrate_resting_Chase) 
#plt.figure(5)
#plt.plot(filt_heartrate_Chase)
avg = sum(filt_heartrate_Chase)/len(filt_heartrate_Chase)
print("Chase's average HR = ", round(avg,2))
print("Chase's HRV = ", np.std(filt_heartrate_Chase))
print ('\n')

# Ben's HR


d_ecg, peaks_d_ecg = l2f.decg_peaks(restingecg_Ben.ecg,restingecg_Ben.t)
Rwave_peaks_d_ecg = l2f.d_ecg_peaks(d_ecg, peaks_d_ecg, restingecg_Ben.t, 0.6, 0.7)
resting_Rwave_t = l2f.Rwave_peaks(restingecg_Ben.ecg, d_ecg, Rwave_peaks_d_ecg, restingecg_Ben.t)
RR_interval_Ben = np.diff(resting_Rwave_t)
heartrate_Ben = (1/RR_interval_Ben)*60
print("Ben's average HR =", sum(heartrate_Ben)/len(heartrate_Ben))
print("Ben's HRV = ", np.std(heartrate_Ben))


Wn = 0.1
b, a = scipy.signal.butter(4, Wn, 'low', analog = False)
filt_restingecg_Eugene = scipy.signal.filtfilt(b, a, restingecg_Eugene.ecg)

peaks,_ = scipy.signal.find_peaks(filt_restingecg_Eugene, height = 330)

# step1
d_ecg, peaks_d_ecg = l2f.decg_peaks(restingecg_Eugene.ecg, restingecg_Eugene.t)
# step2
Rwave_peaks_d_ecg = l2f.d_ecg_peaks(d_ecg, peaks_d_ecg, restingecg_Eugene.t, 0.9, 1.3)
# step3
resting_Rwave_t = l2f.Rwave_peaks(restingecg_Eugene.ecg, d_ecg, Rwave_peaks_d_ecg, restingecg_Eugene.t)



# Eugene's HR
RR_interval_Eugene = np.diff(resting_Rwave_t)


heartrate_Eugene = (1/RR_interval_Eugene)*60


b2, a2 = scipy.signal.butter(4, Wn, 'low')
filt_heartrate_Eugene = scipy.signal.filtfilt(b2, a2, heartrate_Eugene)


print ('\n')
print ("Eugene's Mean Resting HR =", sum(filt_heartrate_Eugene/len(filt_heartrate_Eugene)))
print ("Eugenes HRV =", np.std(filt_heartrate_Eugene))

#Jakob's HR

d_ecg, peaks_d_ecg = l2f.decg_peaks(restingecg_Jakob.ecg, restingecg_Jakob.t)
# step2
Rwave_peaks_d_ecg = l2f.d_ecg_peaks(d_ecg, peaks_d_ecg, restingecg_Jakob.t, 0.1, 0.3)
# step3
resting_Rwave_t = l2f.Rwave_peaks(restingecg_Jakob.ecg, d_ecg, Rwave_peaks_d_ecg, restingecg_Jakob.t)
# HR
RR_interval_Jakob = np.diff(resting_Rwave_t[1:20])
heartrate_Jakob = (1/RR_interval_Jakob)*60
b2, a2 = scipy.signal.butter(4, Wn, 'low')
filt_heartrate_Jakob = scipy.signal.filtfilt(b2, a2, heartrate_Jakob)


print ('\n')
print ("Jakob's Mean Resting HR =", sum(filt_heartrate_Jakob/len(filt_heartrate_Jakob)))
print ("Jakob's HRV =", np.std(filt_heartrate_Jakob))
print ('\n')



#Question 6 - Class' histograms
column_names_HRV = [
    "name",
    "HR",
    "HRV",
]
class_data = pd.read_excel('Class_Data.xlsx',
            names = column_names_HRV)


HR_Values = class_data['HR'].values.tolist()
HRV_Values = class_data['HRV'].values.tolist()


plt.figure(6)
plt.hist(HR_Values, bins = [45,50,55,60,65,70,75,80,85,90,95,100], rwidth = 0.95) # bins = how many columns 
plt.title("Q6.1 Histogram of Class' HR") 
plt.xlabel('Hear Rate[BPM]')
plt.ylabel('Frequency')
print("Class' mean HR = ", sum(class_data['HR'])/len(class_data['HR']))
plt.figure(7)
plt.hist(HRV_Values, bins = [0,5,10,15,20,25], rwidth = 0.95)
plt.title("Q6.2 Histogram of Class' HRV") 
plt.xlabel('Heart Rate Variability [SD]')
plt.ylabel('Frequency')
#print("median HRV = ", st.median(class_data['HRV']))
#print("mean HRV = ", sum(class_data['HRV'])/len(class_data['HRV']))


#Question 7 - Chace exercise filtered HR
bikeecg_Chase = pd.read_csv('ExerciseBike_Chase.txt',
                      names=column_names, sep = '\t', skiprows= 5000, skipfooter= 5000, engine = 'python')

bikeecg_Chase.t = bikeecg_Chase.t/1000

Wn = 0.1
b, a = scipy.signal.butter(4, Wn, 'low', analog = False)
filt_bikeecg_Chase = scipy.signal.filtfilt(b, a, bikeecg_Chase.ecg)

d_ecg, peaks_d_ecg = l2f.decg_peaks(bikeecg_Chase.ecg, bikeecg_Chase.t)
Rwave_peaks_d_ecg = l2f.d_ecg_peaks(d_ecg, peaks_d_ecg, bikeecg_Chase.t, 0.4, 0.5)
bikeecg_Rwave_t = l2f.Rwave_peaks(bikeecg_Chase.ecg, d_ecg, Rwave_peaks_d_ecg, bikeecg_Chase.t)

RR_interval = np.diff(bikeecg_Rwave_t)
heartrate_bike_Chase = (1/RR_interval)*60

Wn = 0.1
b2, a2 = scipy.signal.butter(4, Wn, 'low', analog = False) 
filt_heartrate_Chase = scipy.signal.filtfilt(b2, a2, heartrate_bike_Chase) 
heartrate_bike_chase_X = l2f.newX_axis(RR_interval)

plt.figure(8)
plt.plot(heartrate_bike_chase_X, filt_heartrate_Chase)
plt.title("Q7 Filtered Heart Rate During Stationary Bike Exercise Experiment")
plt.xlabel('Time (s)')
plt.ylabel('Heart Rate (bpm)')

#Question 8 - Chase increase exercise workload
plt.figure(9)
plt.plot(heartrate_bike_chase_X,filt_heartrate_Chase)
plt.axis([60, 240, 45, 130])
plt.title("Q8 Heart Rate During Increased Workload on Stationary Bike")
plt.xlabel('Time (s)')
plt.ylabel('Heart Rate (bpm)')       

#Question 9 - Chase decrease exercise workload
plt.figure(10)
plt.plot(heartrate_bike_chase_X,filt_heartrate_Chase)
plt.axis([240, 480, 45, 135]) 
plt.title("Q9 Heart Rate During Decreased Workload on Stationary Bike")
plt.xlabel('Time(s)')
plt.ylabel('Heart Rate (bpm)') 

#Question 10 - written

#Question 11 - EE over time

Chase_EE_lst = EE.EE_high_lst(filt_heartrate_Chase, 47.1, 56.7)

plt.figure(11)
plt.plot(heartrate_bike_chase_X,Chase_EE_lst)
plt.title("Q11 Energy Expenditure Exercise Experiment")
plt.xlabel('Time (s)')
plt.ylabel('Predicted Energy Expenditure [kcal/min]')

#Question 12 - total EE
EE_sum = np.sum(Chase_EE_lst/filt_heartrate_Chase)
print("total EE = ", round(EE_sum,2), "kcal")

#Question 12 - total EE
EE_sum = np.sum(Chase_EE_lst/filt_heartrate_Chase)
print("total EE = ", round(EE_sum,2), "kcal")

print("total EE in Chocolate bars = ", round(EE_sum/500,2), "500kcal bars")
print("total EE in Joules = ", round(EE_sum*4184,2), "Joules")
print("total EE in %Daily EE = ", round(EE_sum/2000,2), "%")

#Question 13 - DONE
