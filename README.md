# Ski jumping analysis
Here you can find some ski jumping analysis based on Kaggle datasets. It contains results of almost 4000 ski jumping competitions organized between (roughly)
2008 and 2022. I focused only on Men competitions. The project has three parts:
- Analysis connected with overall trends in ski jumping
- Tkinter app with individual stats
- Jump length prediction

# Stack
Pandas, Numpy, Matplotlib, Tkinter, Scikit-Learn

# Overall analysis
In this section I analysed the correlation between different factors like wind compensation, speed or distance. I created heatmaps
grouped by the hill type. After that, I analysed wind conditions in different places and distiguished these with the most changeable weather.

# Tkinter app
In this app user can enter the surname and name of ski jumper and check some stats: favourite hills (based on average of coefficient = distance/k-point),
jumps over hill size, average jury note points and average wind compensation. Moreover, below you can see a histogram showing the distribution of distances achieved by the ski jumper.



![Zrzut ekranu 2025-03-03 120037](https://github.com/user-attachments/assets/84e1f4cf-6256-48a6-8837-059e41707737)




# Jump prediction
This is a machine learning project where I created a simple linear regression model to predict the length of jump based on speed, wind compensation,
k-point and hill-size. Here you can find, when we can predict it well and when it is difficult.
