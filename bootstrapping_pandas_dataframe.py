# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:01:21 2019

@author: mh iyer

Description: Bootstrapping  or 'sampling with replacement'
Given a labelled dataset, generate multiple samples by sampling with replacement randomly

Equivalent to picking marbles out of a jar- pick the first one, put it back, pick the second one, put it back, and so on for N samples
Bootstrapping may result in:
    a) Over-representation of samples: As samples are randomly picked, some may appear several times
    e.g. picking the same blue marble several times even though there are other blue marbles and other marbles with different colours
    
    b) Under-representation of samples: Again, as samples are randomly picked, some may not appear at all!
    e.g. completely ignoring yellow marbles while blue, red and silver marbles may be picked (appear at least once)
    
    The above situations may be ameliorated by adjusting the number of trials - there isn't a golden rule to do this, it is dataset dependent and you may wish to do some trial and error
    

Input: pandas dataframe containing desired data
    num_trials: how many sets of data you require
    
    It is assumed that the number of generated examples in each generated dataframe is the same as the number of examples in the original dataset
    e.g. if you started out with 100 examples, each of the generated datasets will contain 100 examples
    
"""

import pandas as pd
import random

# create sample data if no data is input
def create_dataset():
    
    # I used this website for inspiration:
    # https://www.python-course.eu/Decision_Trees.php
    
    data = pd.DataFrame({"toothed":["True","True","True","False","True","True","True","True","True","False"],
                     "hair":["True","True","False","True","True","True","False","False","True","False"],
                     "breathes":["True","True","True","True","True","True","False","True","True","True"],
                     "legs":["True","True","False","True","True","True","False","False","True","True"],
                     "species":["Mammal","Mammal","Reptile","Mammal","Mammal","Mammal","Reptile","Reptile","Mammal","Reptile"]})
    return(data)
    

# create bootstrap class
class Bootstrap:
    def __init__(self, dataset, num_trials=2):
        self.dataset = dataset
        self.target_size = len(self.dataset)
        self.num_trials = num_trials
        
        # get the number of examples present in the dataset
        self.num_examples = len(self.dataset)
        
        # generate lists for storing the generated data
        self.bootstrapped_data = []
        
    
    def generate_data(self):
        
        # loop through the number of trials
        for i in range(0, self.num_trials):
            # generate a set of random numbers
            # these correspond to the INDICES of the examples which will be used in the current data generation trial
            # e.g. if 0 is one of the indices, the first example in the dataset will be used
            random_indices = [random.randint(0,self.num_examples-1) for i in range(self.num_examples)]

            # initialize an empty pandas dataframe
            df = pd.DataFrame()
            
            # build the new dataset by invoking the examples using their indices
            for index in random_indices:
                df = df.append(self.dataset.iloc[index])
            
            # append the pandas dataframe
            self.bootstrapped_data.append(df)
            
        return (self.bootstrapped_data)
    

# an illustration to show how the class may be used in practice
if __name__ == "__main__":
    # create dataset if you don't have one ready
    dataset = create_dataset()
    
    # create bootstrap object
    b = Bootstrap(dataset, num_trials = 3)
    
    # get your bootstrapped data!
    bootstrapped_data = b.generate_data()
    
    # look at the first dataframe generated
    print(bootstrapped_data[0])
    
            