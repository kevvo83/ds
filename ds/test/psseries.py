import pandas as ps
import numpy as np
import unittest


class PlayWithPsSeries(unittest.TestCase):

    # My notes, for My reference for when I forget

    def test_createSeries(self):
        result = False

        # First way of Declaring a Pandas Series
        # For python 2.7, the order of the index-vs-data will not be guaranteed
        ser1 = ps.Series({'Canada':'Hockey',
                          'USA':'Football',
                          'Brazil':'Football',
                          'Spain':'Football'})
        if ser1.loc['Brazil'] == 'Football':
            result = True

        # Second way of Declaring a Pandas Series - order of Indexes is guaranteed
        ser2 = ps.Series(data=['Moose','Bear','Tiger','Silat','Merlion'], index=['Canada','Russia','India','Malaysia','Singapore'])
        if ser2.loc['Malaysia']=='Silat':
            result = result and True

        s1 = ps.Series(data=5, index=['a','b','c','d','e'], dtype=np.float)

        # Data in Series are aligned by Label - so you're operating on val1 + val1 in the case below, and dont need to worry about
        # the value not being there (will return NaN in this case)
        sres = s1[1:] + s1[:-2]
        if sres.hasnans:
            result = result and True
        else:
            result = result and False

        self.assertTrue(result)


    def test_playDataFrames(self):
        result = False

        # In Python, Lists/Dicts/Sets are mutable
        # other variables like floats, strings, etc. are not mutable

        # Dataframes are not mutable
        purchases = ps.DataFrame(data={'item':'Toothpaste', 'user':'Simon', 'cost':10.5}, index=['Shop1'])

        purchase1 = ps.DataFrame(data={'item':'Washing Powder', 'user':'Tesla','cost':19.5}, index=['Shop2'])
        purchase2 = ps.DataFrame(data={'item':'Toothpaste', 'user':'Nikolay','cost':9.5}, index=['Shop3'])

        purchases = purchases.append(purchase1)
        purchases = purchases.append(purchase2)

        if len(purchases)==3:
            result=True

        df2 = ps.DataFrame(np.random.randint(0,100,(5,5),np.int8), index=['var1','var2','var3','var4','var5'], columns=['col1','col2','col3','col4','col5'])

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()