import pandas
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

initialDf = pandas.read_csv('initialScore.csv')
intervention1Df = pandas.read_csv('intervention1.csv')
intervention2Df = pandas.read_csv('intervention2.csv')

initialList = initialDf['Math_score'].tolist()
intervention2List = intervention2Df['Math_score'].tolist()

initialMean = statistics.mean(initialList)
initialStDev = statistics.stdev(initialList)
intervention2Mean = statistics.mean(intervention2List)
intervention2StDev = statistics.stdev(intervention2List)

def random_set_of_means(counter):
    dlist = []

    for i in range(0, counter):
        random_index = random.randint(0, len(initialList)-1)
        value = initialList[random_index]
        dlist.append(value)
    
    mean = statistics.mean(dlist)

    return mean

meanList = []

def setup():
    for i in range(0, 1000):
        set_of_means = random_set_of_means(100)
        meanList.append(set_of_means)
    
    mean_mean = statistics.mean(meanList)
    mean_st_dev = statistics.stdev(meanList)

    first_st_dev_start = mean_mean - mean_st_dev
    first_st_dev_end = mean_mean + mean_st_dev

    second_st_dev_start = mean_mean - (2 * mean_st_dev)
    second_st_dev_end = mean_mean + (2 * mean_st_dev)

    third_st_dev_start = mean_mean - (3 * mean_st_dev)
    third_st_dev_end = mean_mean + (3 * mean_st_dev)

    fig = ff.create_distplot([meanList], ['Initial Score'], show_hist=False)
    fig.add_trace(go.Scatter(x=[initialMean, initialMean], y=[0, 0.17], mode='lines', name='Initial Mean'))
    fig.add_trace(go.Scatter(x=[intervention2Mean, intervention2Mean], y=[0, 0.17], mode='lines', name='Mean of students who got fun sheets'))
    fig.add_trace(go.Scatter(x=[second_st_dev_start, second_st_dev_start], y=[0, 0.17], mode='lines', name='2nd Standard Deviation End', marker=dict(color="cadetblue")))
    fig.add_trace(go.Scatter(x=[third_st_dev_start, third_st_dev_start], y=[0, 0.17], mode='lines', name='3nd Standard Deviation End', marker=dict(color="tomato")))
    fig.add_trace(go.Scatter(x=[second_st_dev_end, second_st_dev_end], y=[0, 0.17], mode='lines', name='2nd Standard Deviation End', marker=dict(color="cadetblue")))
    fig.add_trace(go.Scatter(x=[third_st_dev_end, third_st_dev_end], y=[0, 0.17], mode='lines', name='3nd Standard Deviation End', marker=dict(color="tomato")))

    fig.show()

    z_score = (mean_mean - intervention2Mean) / mean_st_dev
    print(z_score)

setup()