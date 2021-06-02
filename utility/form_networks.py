import numpy as np

def get_voting_array(df, drop = True):
    
    '''
        df -> the congressional dataframe for a particular session
        drop -> remove people who don't vote, a flag of Yes or No
    '''
    
    ids = df['icpsr']
    unq_ids = np.unique(ids)
    
    bills = df['rollnumber']
    unq_bills = np.unique(bills)
    
    V = np.zeros((unq_ids.shape[0], unq_bills.shape[0]))
    
    to_drop = []
    
    for idx, c_id in enumerate(unq_ids):
        
        c_df = df[df['icpsr'] == c_id]
        c_bills = np.array((c_df['rollnumber'])) - 1
        c_cast = c_df['cast_code']
        
        V[idx, c_bills] = c_cast
        
        if np.sum(c_cast) == 0:
            to_drop.append(idx)
            
    if drop == True:
        V = np.delete(V, to_drop, axis = 0)
        
    return V