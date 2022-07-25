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

def get_one_hot(votes_df, ideology_df):
    
    '''
        votes_df -> the dataframe encoding votes that is used to get V.
        ideology_df -> this stores party information.
    '''
    
    ids = ideology_df['icpsr']
    
    p_ids = np.zeros((ids.shape[0]))

    for idx, c_id in enumerate(np.unique(votes_df['icpsr'])):
        p_ids[idx] = ideology_df[c_id == ids]['party_code']
        
    unq_parties = np.unique(p_ids)
    
    one_hot = np.zeros((p_ids.shape[0], unq_parties.shape[0]))
    
    for idx, p in enumerate(unq_parties):
        
        one_hot[:, idx] = (p == p_ids).astype(int)
    
    return one_hot, p_ids

def get_adjacency(V):
    
    '''
        V -> the array containing voting trends.
    '''
    
    N = V.shape[0]
    A = np.zeros((N, N))
    
    for idx, v_0 in enumerate(V):
        for jdx, v_1 in enumerate(V):

            if idx != jdx:
                locs = v_0 == v_1
                sim = np.sum(locs)/locs.shape[0]
                A[idx, jdx] = sim
                
    return A