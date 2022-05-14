# Stationary Noise Cleaning API documentation

<!--
## Contents

#### 1. [Summary](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#1-summary-1)
#### 2. [Voice Assistant Overview](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#2-voice-assistant-overview-1)
#### 3. [What is Stationary Noise and Non-Stationary noise?](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#3-what-is-stationary-noise-and-non-stationary-noise-1)
#### 4. [Limitations](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#4-limitations-1)
#### 5. [Dataset](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#5-dataset-1)
#### 6. [Environment](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#6-environment-1)
#### 7. [Pre-Requisites](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#7-pre-requisites-1)
#### 8. [Dependencies](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#8-dependencies-1)
#### 9. [Clean a sample Audio file](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#9-clean-a-sample-audio-file-1)
#### 10. [Stationary Noise Cleaning using <code>noisereduce</code> API](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#10-stationary-noise-cleaning-using-noisereduce-api-1)
#### 11. [Removing Stationary noise for Deep Learning Model Training](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#11-removing-stationary-noise-for-deep-learning-model-training-1)
#### 12. [Steps for cleaning the AVICAR dataset](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#12-steps-for-cleaning-the-avicar-dataset-1)
#### 13. [Sample Output](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#13-sample-output-1)
#### 14. [Future Work](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#14-future-work-1)
#### 15. [References](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#15-references-1)
#### 16. [Source Code](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Stationary%20Noise%20Cleaning.md#16-source-code-1)

-->

## 1. Summary

This API documentation provides information about pre-processing audio datasets which has a Stationary Noise in the background. The primary use case for this documentation is for a **Car Voice Assistant.** The Voice Assistant device is placed on the dashboard of a car where the driver asks for route guidance to a destination. The Voice Assistant responds with a route map and voice guidance to the destination, while displaying the map on the device.

Car Voice Assistants encounter issues like background noise that occurs in the interior of car when the car is moving. This documentation provides solution to remove the background noise from the audio to improve quality of response from the Car Voice Assistant.

## 2. Voice Assistant Overview

Voice Assistants are devices like Google Assistant, Siri and Alexa products developed by Google, Apple and Amazon respectively. These assistants capture human voice on the utterance of wake word (eg: "Hey Google") and responds with an action on the device. Action can either be a voice output or a screen display or both.

## 3. What is Stationary Noise and Non-Stationary noise?

Stationary noise is a steady stream of noise that is constant and occurs in the background at a constant frequency, throughout the length of the audio. Example: A moving car interior has a low pitch humming noise throughout the entire travel time in the car.

Non-Stationary noises are variable noises with different frequencies and pitch that occurs in the background of the whole audio. Example : Music playing inside the car, other passengers talking, baby crying and the likes of it.

This documentation focuses on Stationary Noise.


## 4. Limitations

1. The moving car does not have passengers other than the driver. The voice input is given by a driver or 1 user.

2. The Stationary Noise for this API covers noises from inside of the moving car

    - When the car window is down

    - When the car window is up

  Both the noises have a difference in pitch but have a constant frequency throughout the entire audio.


## 5. Dataset

  - AVICAR Dataset used is an open source dataset with audio recorded in a moving car. Dataset name : ["avicar_somedigits.zip"](http://www.isle.illinois.edu/sst/AVICAR/)

  - User speaks alphabets or words or numbers.

  - Dataset is designed to be used for training Deep Learning models.

  - Maximum duration of audio is 9 seconds or less (audio length <=9 seconds)

  - Total number of audio files 10023 files


## 6. Environment

  - Jupyter Notebook version 6.4.5


## 7. Pre-Requisites

The following libraries should be installed

> ```
> !pip install librosa   # python package for analysis of audio files
> !pip install noisereduce # python package for cleaning audio background
> !pip install soundfile # python package to read and write audio files
>
>```

## 8. Dependencies

##### Import Libraries

>```
>import numpy as np
>import pandas as pd
>import matplotlib.pyplot as plt
>from glob import glob
>from IPython.display import Audio
>import librosa as lr
>import librosa.display
>import os
>import io
>import sys
>from scipy.io import wavfile
>import noisereduce as nr
>import soundfile as sf
>from noisereduce.generate_noise import band_limited_noise
>
>```

## 9. Clean a sample Audio file


#### <code>Step 1.</code> Set directory path for loading AVICAR audio files

>```
>data_dir='/Downloads/avicar_somedigits'
>audio_files=glob(data_dir + '/*.wav')
>len(audio_files)
>
>```

<code>Note:</code> This dataset is loaded from local machine. Substitute the <code>data_dir</code> with your local path.


# [](#displayline)

#### <code>Step 2.</code> Load 1 Audio file


>```
>data, rate = sf.read(audio_files[0])  # read the first audio file
>np.shape(data)  # Array size is 15153
>
>```

- <code> data </code> audio file is converted into an array

- <code> rate </code> sampling rate

# [](displayline)

#### <code>Step 3.</code> Find Sampling rate

>```
>print(rate) # sampling rate is 16Khz
>
>```

# [](displayline)


#### <code> Step 4.</code> Listen to the Audio

>```
>Audio(data=audio_files[0], autoplay=True)
>
>```

[Raw_audio_files_0.wav](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Raw_audio_files_0.wav)

# [](displayline)


#### <code>Step 5.</code> Find duration of the Audio

>```
>file_name=audio_files[0]
>dur_avi=lr.get_duration(y=data, sr=rate)
>print(dur_avi)  # Duration is .9470635 seconds
>
>```

# [](displayline)

#### <code> Step 6.</code> Plot Amplitude over Time waveform

Graph is plotted using <code>matplotlib</code> library.

>```
>fig, ax = plt.subplots(figsize=(15,3))
>ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
>ax.plot(data)
>
>```

![Plot Amplitude over time](https://github.com/Faridacoding/API-Documentation-Samples/blob/195d0ec4eec173f6360c7255e092182237a80473/Machine%20Learning%20Voice%20Assistant/Voiceassistant_waveforem.jpg)

# [](displayline)

#### <code> Step 7.</code> Dataset Inferences

- The first audio file in the AVICAR dataset has a male voice speaking the word **"Done"** in a moving car environment.

- The background noise of the moving car (humming noise) is captured along with the human voice during audio recording. This background noise is a stationary noise and it should be removed.

- Duration of the first audio file = 0.9470625 seconds

- The spectrum graph shows distorted amplitude wave
    - Spectrum shows wavy spikes throughout the length of the audio.
    - These wavy spikes implies background noise of the moving car.

# [](displayline)

## 10. Stationary Noise Cleaning using <code>noisereduce</code> API

<code>noisereduce</code> API is based on an algorithm on **Fourier Analysis** and **Spectral Noise Gating.** The author of this algorithm and the related Github repo can be found [here.](https://timsainburg.com/noise-reduction-python.html)

The <code>noisereduce</code> algorithm requires two inputs:

1. A **noise audio clip containing stationary noise.**

2. A **signal audio clip containing the signal** and the noise intended to be removed.

# [](displayline)


#### <code>Step 1.</code> Creating the signal for the Audio  

This code creates a synthetic noise signal and adds it to the original audio.

- The length of the audio <code>noise_len</code> is **standardized to 1 sec.**

- The frequency of the synthetic signal <code>noise</code> is set in the range **10KHz - 20Khz**

- The audio file array and the noise array are combined together and stored in variable <code>audio_clip_band_limited.</code> This is a simple mathematical matrix addition technique.

>```
>noise_len = 1 # seconds
>noise = band_limited_noise(min_freq=10000, max_freq = 20000, >samples=len(data), samplerate=rate)*10
>noise_clip = noise[:rate*noise_len]
>audio_clip_band_limited = data+noise
>
>```

# [](displayline)


#### <code> Step 2:</code> Plot Graph for Modified Audio with Synthetic signal

>```
>fig, ax = plt.subplots(figsize=(15,3))
>ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
>ax.plot(audio_clip_band_limited)
>
>```

![Modified Audio with Synthetic signal](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Modified%20Audio%20with%20Synthetic%20signal.jpg)

# [](displayline)

#### <code>Step 3:</code> Removing noise

- This code removes the synthetic signal that was added in Step 2.

- The **frequencies** for both **synthetic signal and background audio signal overlap each other.** And, when the <code>noisereduce</code> algorithm is applied on the Audio, the background noise is removed along with the synthetic signal that was added previously.

>```
>reduced_noise = nr.reduce_noise(y = >audio_clip_band_limited,n_std_thresh_stationary=1.5,sr=rate,stationary=True)
>
>```

# [](displayline)

#### <code>Step 4:</code> Listen to the Cleaned audio

>```
>Audio(data=reduced_noise, rate=rate, autoplay=True)
>
>```

[Cleaned Audio](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Cleaned_AF1_35D_D0_C1_M3.wav)

# [](displayline)

#### <code>Step 5:</code> Plot Graph for the Cleaned Audio

>```
>fig, ax = plt.subplots(figsize=(20,3))
>ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
>ax.plot(reduced_noise, color ="green")
>
>```

![Cleaned Audio waveform](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Cleaned%20Audio%20graph.jpg)


- The straight line implies silence in audio.
- The waveform is a clean audio without the background noise which represents the male voice uttering the word **"Done"**



# [](displayline)

## 11. Removing Stationary noise for Deep Learning Model Training

- Machine Learning Models require large datasets for training a model to achieve higher prediction scores (accuracy metrics) for that model. Similarly, for Deep learning models, a larger dataset with small size is required for model training to be successful and to have higher accuracy metrics. AVICAR is designed to be used for these types of use cases.

- In the previous section, a sample cleaning with single audio file was tested. In this section, the entire dataset will be cleaned using the steps discussed in the previous section. This cleaned dataset can be used for training Deep Learning models.

## 12. Steps for cleaning the AVICAR dataset

>> 1. Create a function for the adding synthetic noise to the audio <code>S_noise_reducer(data,length,rate)</code>
>>
>>
>> 2. Iterate the dataset inside a loop and clean each audio.


# [](displayline)


#### <code> Step 1:</code> Create a function <code>S_noise_reducer()</code>

- This function adds a **signal** or **synthetic noise** to the audio.

- The audio length is **not standardized.** The cleaned audio length remains same as the original audio length.

>```
>def S_noise_reducer(data,length,rate):
>
>    noise_len = int(length) # seconds
>    noise = band_limited_noise(min_freq=10000, max_freq = 20000, samples=len(data), samplerate=rate)*10
>    noise_clip = noise[:rate*noise_len]
>    audio_clip_band_limited = data+noise
>
>    return(audio_clip_band_limited)
>```

# [](displayline)

#### <code> Step 2:</code> Iterate dataset inside a loop

>```
>audio_dur=[]
>for file in range(0, len(audio_files),1):
>    file_name=os.path.basename(audio_files[file])
>    print(file,file_name)
>    
>    #Read the first audio file
>    audio, sfreq=lr.load(audio_files[file])
>    time=np.arange(0,len(audio))/sfreq
>    
>    #find the audio duration
>    duration_avi=lr.get_duration(y=audio, sr=sfreq)
>    #print('Audio Duration or length:',duration_avi)
>    audio_dur.append(duration_avi)
>    
>    #Plot audio over time( Orginal Audio)
>    print('Original_',file_name)
>    fig, ax=plt.subplots(figsize=(20,3))
>    ax.plot(time,audio)
>    ax.set(xlabel='Time(s)',ylabel='Sound Amplitude')
>    plt.show()
>    
>    
>    #Stationary noise removal
>    #Step1: Add noise
>    audio_clip_band_limited=S_noise_reducer(audio,duration_avi,sfreq)
>    reduced_noise = nr.reduce_noise(y = audio_clip_band_limited,n_std_thresh_stationary=1.5,sr=rate,stationary=True)
>    
>    #Plot Cleaned waveform
>    print('Cleaned_',file_name)
>    fig, ax=plt.subplots(figsize=(20,3))
>    ax.plot(time,reduced_noise,color="green")
>    plt.show()
>    
>    print('*****************************************************************************')
>    
>    #Save the Cleaned file
>    sf.write('Cleaned_avicar_somedigits/Cleaned_'+file_name, reduced_noise, sfreq)
>
>```


## 13. Sample output

![Sample Output](https://github.com/Faridacoding/API-Documentation-Samples/blob/main/Machine%20Learning%20Voice%20Assistant/Sample%20Original%20and%20Cleaned%20Audio%20file.png)


## 14. Future Work

- This algorithm can be improvised using Speech-to-text API (Google's API) to convert the clean audio file to text.

- This text can then be fed into the Voice Assistant for response generation.

## 15. References

1. **AVICAR Dataset**
     - AVICAR Dataset - Stationary noise dataset (car driving noise + driver/passenger noise)
     - Link : http://www.isle.illinois.edu/sst/AVICAR/


2. **Noisereduce API**
     - Link : https://timsainburg.com/noise-reduction-python.html

     - Github repo: https://github.com/timsainb/noisereduce


## 16. Source Code

[Voice Assistant Stationary Noise Cleaning](https://github.com/Faridacoding/Hashnode/blob/main/Voice%20Assistant%20Stationary%20Noise%20Cleaning%20final.ipynb)
