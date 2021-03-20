import scipy.io.wavfile as wav
import numpy as np
import os

df = np.genfromtxt("ecg.csv", delimiter=',')
wav.write('input_ecg.wav', 500, df)

df = np.genfromtxt("pcg.csv", delimiter=',')
wav.write('input_pcg.wav', 4000, df)

os.remove('output_ecg.mp3')
os.remove('output_pcg.mp3')
os.system('ffmpeg -i input_ecg.wav output_ecg.mp3')
os.system('ffmpeg -i input_pcg.wav output_pcg.mp3')
os.remove('input_ecg.wav')
os.remove('input_pcg.wav')
