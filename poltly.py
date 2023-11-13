# -*- coding: utf-8 -*-
"""poltly.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TvSS5qrsTLTsKhuV-DIB9gzbIX_elkkb
"""

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1,2,3,4,5] , y=[3,4,5,6,7] , mode='markers' ))
fig.show()

"""Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
scatter plot for age and fare columns in the titanic dataset.

"""

import seaborn as sns

tips = sns.load_dataset('tips')

fig = go.Figure(data = [go.Histogram(x = tips.total_bill)])
fig.show()

tips



"""Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express."""

import plotly.express as px
df = px.data.tips()
fig = px.box(df, y="total_bill")
fig.show()



"""Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
column with the color parameter.

"""

import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="sex", y="total_bill", color="sex", pattern_shape="smoker")
fig.show()



"""Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
the color parameter.
Note: Use "sepal_length", "sepal_width", "petal_length", "petal_width" columns only with the
dimensions parameter.
"""

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter3d(x=tips.total_bill, y=tips.tip , mode='markers' ,z =tips['size'] ))
fig.show()



"""Q5. What is Distplot? Using Plotly express, plot a distplot.

The distplot figure factory displays a combination of statistical representations of numerical data, such as histogram, kernel density estimation or normal curve, and rug plot.
"""

import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

data = np.random.randn(200)
res = sn.distplot(data)
plt.show()

