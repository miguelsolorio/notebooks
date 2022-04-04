# import required modules
import pandas as pd
import matplotlib.pyplot as plt
stdData = [['S1', 'M', 13, 123, 46],
        ['S2', 'M', 12, 134, 82],
        ['S3', 'F', 14, 114, 77],
        ['S4', 'M', 13, 136, 74],
        ['S5', 'F', 13, 107, 56],
        ['S6', 'F', 12, 121, 80],
        ['S7', 'M', 14, 113, 76],
        ['S8', 'F', 15, 123, 95],
        ['S9', 'F', 14, 112, 78],
        ['S10', 'M', 15, 100,60] ]
# creating the dataframe from the above data
df = pd.DataFrame(stdData, columns = ['ID', 'Gender','Age', 'Height(cm)','Marks'] )
df.hist()# create histogram for the numeric data(Age, Height,Marks)
plt.show() #displaying the plot

