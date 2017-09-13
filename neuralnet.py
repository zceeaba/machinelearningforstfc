import numpy as np
import sklearn
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import pandas as pd
from readsqltables import readsqltable

from readdata import readdatac
class neuralnet:
    def __init__(self):
        self.rd=readdatac()
        self.rd.readsqltable()
        self.personview=self.rd.personlist
        self.isisview=self.rd.isislist
        self.generatepandasdataframe()
        self.readcsv()

    def generatepandasdataframe(self):
        personviewdf=pd.DataFrame(self.personview)
        isisviewdf=pd.DataFrame(self.isisview)
        print(personviewdf)
        print(isisviewdf)

    def readcsv(self):
        #proposals=pd.read_excel('C:\\Users\\Sif49882\\PycharmProjects\\machinelearningforstfc\\proposal-funding.csv',skiprows=1,encoding = "ISO-8859-1", error_bad_lines=False,delim_whitespace=True)
        proposalfunding=pd.read_excel('C:\\Users\\Sif49882\\PycharmProjects\\machinelearningforstfc\\proposal-funding.xlsx')
        proposals=pd.read_excel('C:\\Users\\Sif49882\\PycharmProjects\\machinelearningforstfc\\proposals.xlsx')
        proposalinvestigators=pd.read_excel('C:\\Users\\Sif49882\\PycharmProjects\\machinelearningforstfc\\proposal-investigators.xlsx')
        print(proposalfunding)

    def readmysqltables(self):
        rd=readsqltable()
        rd.readprojectfundview()

    def createlogisticregression(self):
        clf=sklearn.linear_model.LogisticRegressionCV()




nn=neuralnet()

"""
#Generate a dataset and plot it
np.random.seed(0)
X,y=make_moons(200,noise=0.20)
plt.scatter(X[:,0],X[:,1],s=40,c=y,cmap=plt.cm.Spectral)
plt.show()

clf=sklearn.linear_model.LogisticRegressionCV()
clf.fit(X,y)

#Helper function to plot a decision boundary
def plot_decision_boundary():
    print("Plot decision boundary")

plot_decision_boundary(lambda x:clf.predict(x))
plt.title("Logistic Regression")

"""

