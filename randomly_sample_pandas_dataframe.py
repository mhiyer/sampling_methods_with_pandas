# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:01:21 2019

@author: mh iyer

Description: Randomly sample a pandas dataframe
Given a labelled dataset, generate a sampled dataframe by randomly selecting examples 


Input: pandas dataframe containing desired data
    target_size: the number of samples to be present in the target dataset

Output: Sampled dataset with number of examples = target_size
    
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
class RandomSampling:
    # initialize
    def __init__(self, dataset, target_size):
        # dataset to be sampled
        self.dataset = dataset
        
        # get number of examples in dataset
        self.num_examples = len(self.dataset)
        
        # number of samples to be present in the sampled dataset
        self.target_size = target_size
        
        # initialize list for storing the generated data
        self.sampled_data = []
        
    
    # function to randomly sample data
    def generate_randomly_sampled_data(self):
        
        # generate a set of random numbers WITHOUT repetition
        # these correspond to the INDICES of the examples which will be used in the current data generation trial
        # e.g. if 0 is one of the indices, the first example in the dataset will be used
        random_indices = random.sample(range(0,self.num_examples), self.target_size)
        
        # initialize an empty pandas dataframe
        df = pd.DataFrame()
        
        # build the new dataset by invoking the examples using their indices
        for index in random_indices:
            df = df.append(self.dataset.iloc[index])
        
        # append the pandas dataframe
        self.sampled_data = df
        
        return (self.sampled_data)
    

# an illustration to show how the class may be used in practice
if __name__ == "__main__":
    # create dataset if you don't have one ready
    dataset = create_dataset()
    
    # create bootstrap object
    b = RandomSampling(dataset, target_size = 5)
    
    # get your bootstrapped data!
    sampled_data = b.generate_randomly_sampled_data()
    
    # look at the first dataframe generated
    print(sampled_data)
    
            