# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:27:06 2019

@author: mh iyer
Description: Systematically sample a pandas dataframe
Given a labelled dataset, generate a systematically sampled dataframe by selecting every 'kth' example


Input: pandas dataframe containing desired data
    k: every kth example (starting from 0) will be selected
    
Output: Systematically Sampled dataset 
    
"""

import pandas as pd

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
    

# create class
class SystematicSampling:
    # initialize
    def __init__(self, dataset, k):
        # dataset to be sampled
        self.dataset = dataset
        
        # get number of examples in dataset
        self.num_examples = len(self.dataset)
        
        # number of samples to be present in the sampled dataset
        self.k = k
        
        # initialize list for storing the generated data
        self.sampled_data = []
        
    
    # function to randomly sample data
    def generate_systematically_sampled_data(self):
        
        # generate numbers in steps of k
        indices = [x for x in range(0,self.num_examples,self.k)]
        
        # initialize an empty pandas dataframe
        df = pd.DataFrame()
        
        # build the new dataset by invoking the examples using their indices
        for index in indices:
            df = df.append(self.dataset.iloc[index])
        
        # append the pandas dataframe
        self.sampled_data = df
        
        return (self.sampled_data)
    

# an illustration to show how the class may be used in practice
if __name__ == "__main__":
    # create dataset if you don't have one ready
    dataset = create_dataset()
    
    # create object
    b = SystematicSampling(dataset, k = 3)
    
    # get your data!
    sampled_data = b.generate_systematically_sampled_data()
    
    # look at the dataframe generated
    print(sampled_data)
    
            
