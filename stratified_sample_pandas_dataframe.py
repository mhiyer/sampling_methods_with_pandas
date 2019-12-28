# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:27:22 2019

@author: mh iyer


Description: Perform stratified sampling on a pandas dataframe
Given a labelled dataset, generate stratified samples by specifying the attribute to group the examples by
e.g. if there is a column 'Shoe Color', with values 'blue', 'green' and 'black', stratified sampling may be done to obtain 
three sets of samples - those with blue shoe colors, those with green shoe colors and those with black shoe colors. These are referred to as groups
In this case the attribute to group by is 'Shoe Color'

Inputs:  ->pandas dataframe containing desired data
        ->ratio: a number between 0 and 1 that is used to extract a certain number of samples from each group, 
             e.g if ratio=0.5, then 50% of the samples from EACH GROUP will be extracted and presented as the output
        -> attribute_name: the attribute that will be used to group the dataframe by feature

Output: Sampled dataset 
    
"""

import pandas as pd

# create sample data if no data is input
def create_dataset():
    
    # the renowned iris-dataset, by now a staple in ML assignments!
    df = pd.read_csv(r'iris.csv')
    return(df)
    

# create bootstrap class
class StratifiedSampling:
    # initialize
    def __init__(self, dataset, ratio, attribute):
        # dataset to be sampled
        self.dataset = dataset
        
        # get number of examples in dataset
        self.ratio = ratio
        
        # number of samples to be present in the sampled dataset
        self.attribute = attribute

        # initialize list for storing the generated data
        self.sampled_data = pd.DataFrame()
        
        # initialize a dictionary for storing subsets of the data- each list corresponds to those samples with a common feature
        # the keys are the unique value for the attribute chosen
        # the values are the samples that have the unique value (key) in common
        self.sampled_data_subsets = {}
        
    
    # function to randomly sample data
    def generate_stratified_samples_data(self):
        # group by the attribute the user has input
        # get unique values for the attribute column
        values = self.dataset[self.attribute].unique()
        
        # loop through values to generate groups
        for value in values:
            # get ALL the samples that have this value in common
            subset_current_value_entire = self.dataset[self.dataset[self.attribute]==value]
            
            # now use self.ratio to get a particular number of samples from the subset
            # get the number of samples to extract - just ratio multiplied by the number of examples present in the subset defined above
            # round it as you can't have 0.2 of a sample!
            
            num_samples =  round(self.ratio*len(subset_current_value_entire))
            
            # get partial subset - num_samples examples of the entire subset
            subset_current_value_part = subset_current_value_entire[0:num_samples]
            
            # update dictionary
            self.sampled_data_subsets[value] = subset_current_value_part
                       
            # concatenate with self.sampled_data
            self.sampled_data = pd.concat([self.sampled_data, self.sampled_data_subsets[value]])

        # reset index for self.sampled_data, else it will be a mess 
        self.sampled_data.index = range(0,len(self.sampled_data))
        
        return self.sampled_data, self.sampled_data_subsets
    

# an illustration to show how the class may be used in practice
if __name__ == "__main__":
    # create dataset if you don't have one ready
    # we need the index to number the examples! please keep that in mind if you wish to input your own dataset
    dataset = create_dataset()

    # create object
    b = StratifiedSampling(dataset, ratio = 0.1, attribute = 'species')         
    
    # get your data!
    sampled_data, sampled_data_subsets = b.generate_stratified_samples_data()