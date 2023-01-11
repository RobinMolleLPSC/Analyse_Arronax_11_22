import numpy as np
import os
import scipy
import Fichier_trc as fichier
import readTrc as rT
import matplotlib.pyplot as plt

adresse = "C:\\Users\\molle\\Documents\\LPSC_Stage\\ARRONAX\\ARRONAX_11_22\\Data\\SamEndommagement\\PointB\\PointB_02\\"
nom_fichier_C1 = "C1--BasseIntensiteTroisRun--"
nom_fichier_C2 = "C2--PointB_02--"
nom_fichier_C3 = "C3--PointB_02--"
nom_fichier_C4 = "C4--BasseIntensiteTroisRun--"

for file in [adresse]:


    C1 = [0.0 for i in range(2500002)]
    C2 = [0.0 for i in range(2500002)]
    C3 = [0.0 for i in range(2500002)]
    C4 = [0.0 for i in range(2500002)]

    filename = nom_fichier_C1
    os.chdir(adresse)
    integrale_file = [];
    print("Ouverture de " + filename)
    nombre_waveform = 10
    # for i in range(nombre_waveform,nombre_waveform+1):
    #     waveform = str(i).zfill(5)
    #     if(os.path.isfile(filename + str(waveform) + '.trc')):
    #         time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
    #
    #         # print(len(time))
    #         # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
    #         # plt.xlabel("Time (ns)")
    #         # plt.ylabel("Amplitude (mV)")
    #         # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
    #         for j in range(len(amplitude)):
    #             C1[j] = (amplitude[j]+C1[j]*i)/(i+1)

    filename = nom_fichier_C2
    os.chdir(adresse)
    integrale_file = []
    print("Ouverture de " + filename)
    for i in range(nombre_waveform):
        waveform = str(i).zfill(5)
        if(os.path.isfile(filename + str(waveform) + '.trc')):
            time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
            # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
            # plt.xlabel("Time (ns)")
            # plt.ylabel("Amplitude (mV)")
            # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
            for j in range(len(amplitude)):
                C2[j] = (amplitude[j]+C2[j]*i)/(i+1)

    filename = nom_fichier_C3
    os.chdir(adresse)
    integrale_file = [];
    print("Ouverture de " + filename)
    for i in range(nombre_waveform):
        waveform = str(i).zfill(5)
        if(os.path.isfile(filename + str(waveform) + '.trc')):
            time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
            # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
            # plt.xlabel("Time (ns)")
            # plt.ylabel("Amplitude (mV)")
            # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
            for j in range(len(amplitude)):
                C3[j] = (amplitude[j]+C3[j]*i)/(i+1)
    #
    # filename = nom_fichier_C4
    # os.chdir(adresse)
    # integrale_file = [];
    # print("Ouverture de " + filename)
    # for i in range(nombre_waveform):
    #     waveform = str(i).zfill(5)
    #     if(os.path.isfile(filename + str(waveform) + '.trc')):
    #         time, amplitude, _ = rT.readTrc(filename + str(waveform) + '.trc')
    #         # plt.plot([ x * 1E9 for x in time], [y for y in amplitude], label="SAM")
    #         # plt.xlabel("Time (ns)")
    #         # plt.ylabel("Amplitude (mV)")
    #         # plt.title("Waveform Alpha 64MeV on diamond of 550µm")
    #         for j in range(len(amplitude)):
    #             C4[j] = (amplitude[j]+C4[j]*i)/(i+1)


plt.figure()
# plt.plot([time[k]*1E9 for k in range(len(time))],[C1[k]*1E3 for k in range(len(C1))],label="Gandalf Front - 150V - 1V/µm")
plt.plot([time[k]*1E9 for k in range(len(time))],[C2[k] for k in range(len(C2))],label="Waveform point D fluence nulle : SAM")
plt.plot([time[k]*1E9 for k in range(len(time))],[C3[k] for k in range(len(C3))],label="PM")
# plt.plot([time[k]*1E9 for k in range(len(time))],[C4[k]*1E3 for k in range(len(C4))],label="Sam Front - 0V - 0.55V/µm")

plt.title("Waveform point D fluence nulle : SAM")
plt.xlabel("Time (ns)")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.show()

