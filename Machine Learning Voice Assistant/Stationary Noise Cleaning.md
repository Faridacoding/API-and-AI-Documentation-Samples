# Stationary Noise Cleaning API documentation

## Contents

#### 1. [Summary](#addlink)
#### 2. [Voice Assistant Overview](#addlink)
#### 3. [What is Stationary Noise and Non-Stationary noise?](#addlink)
#### 4. [Limitations](#addlink)
#### 5. [Dataset](#addlink)
#### 6. [Environment](#addlink)
#### 7. [Pre-Requisites](#addlink)
#### 8. [Dependencies](#addlink)
#### 9. [AVICAR Dataset](#addlink)

## Summary

This API documentation provides information about pre-processing audio datasets which has a Stationary Noise in the background. The primary use case for this documentation is for a **Car Voice Assistant.** The Voice Assistant device is placed in the dashboard of a car where the driver asks for route guidance to a destination. The Voice Assistant responds with a route map and voice guidance to the destination, while displaying the map on the device. Car Voice Assistants encounter issues like background noise that occurs in the interior of car when the car is moving. This documentation provides solution to remove the background noise from the audio to improve quality of response by the Car Voice Assistant.

## Voice Assistant Overview

Voice Assistants are devices like Google Assistant, Siri and Alexa products developed by Google, Apple and Amazon respectively. These assistants capture human voice on the utterance of wake word (eg: "Hey Google") and responds with an action on the device. Action can be either be a voice output or a screen display or both.

## What is Stationary Noise and Non-Stationary noise?

Stationary noise is a steady stream of noise that is constant and occurs in the background at a constant frequency, throughout the length of the audio. Example: A moving car interior has a low pitch humming noise throughout the entire travel time in the car.

Non-Stationary noises are variable noises with different frequencies and pitch that occurs in the background of the whole audio. Example : Music playing inside the car, other passengers talking, baby crying and the likes of it.

This documentation focuses on Stationary Noise.


## Limitations

1. The moving car does not have passengers other than the driver. The voice input is given by driver or 1 user.

2. The Stationary Noise for this API covers noises from inside of the moving car

    - When the car window is down

    - When the car window is up

  Both the noises have a difference in pitch but have a constant frequency throughout the entire audio.


## Dataset

  - AVICAR Dataset used is an open source dataset with audio recorded in a moving car. Dataset name : ["avicar_somedigits.zip"](http://www.isle.illinois.edu/sst/AVICAR/)

  - User speaks alphabets or words or number.

  - Dataset designed to be used for training Deep Learning models.

  - Maximum duration of audio is 3 seconds or less (audio length <=3 seconds)

  - Total number of audio files 10023 files


## Environment

  - Jupyter Notebook version 6.4.5


## Pre-Requisites

The following libraries should be installed

```
!pip install librosa   # python package for analysis of audio files
!pip install noisereduce # python package for cleaning audio background
!pip install soundfile # python package to read and write audio files

```

## Dependencies

##### Import Libraries

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
from IPython.display import Audio
import librosa as lr
import librosa.display
import os
import io
import sys
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise

```

## AVICAR Dataset


#### 1. Set directory path for loading AVICAR audio files

```
data_dir='/Downloads/avicar_somedigits'
audio_files=glob(data_dir + '/*.wav')
len(audio_files)

```

<code>Note:</code> This dataset is loaded from local machine. Substitute the <code>data_dir</code> with your local path.


# [](#displayline)

#### 2. Load 1 Audio file


```
data, rate = sf.read(audio_files[0])  # read the first audio file
np.shape(data)  # Array size is 15153

```

- <code> data </code> audio file is converted into an array

- <code> rate </code> sampling rate

# [](displayline)

#### 3. Find Sampling rate

```
print(rate) # sampling rate is 16Khz

```

# [](displayline)


#### 4. Listen to the Audio

```
Audio(data=audio_files[0], autoplay=True)

```

# [](displayline)


#### 5. Find duration of the Audio

```
file_name=audio_files[0]
dur_avi=lr.get_duration(y=data, sr=rate)
print(dur_avi)  # Duration is .9470635 seconds

```

# [](displayline)

#### 6. Plot Amplitude over Time waveform

```
fig, ax = plt.subplots(figsize=(15,3))
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
ax.plot(data)

```

![Plot Amplitude over time](https://github.com/Faridacoding/API-Documentation-Samples/blob/195d0ec4eec173f6360c7255e092182237a80473/Machine%20Learning%20Voice%20Assistant/Voiceassistant_waveforem.jpg)



## Stationary Noise Cleaning using Noisereduce API




## References
