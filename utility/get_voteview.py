import pandas as pds
import numpy as np

def get_ideology_df(session, chamber):

    '''
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    sessions = np.arange(1, 117)

    try:
        if int(session) in sessions:

            session = str(session)
            while len(session) != 3:
                session = "0" + session

            if chamber.title() == 'House':
                url = 'https://voteview.com/static/data/out/members/H{}_members.csv'.format(session)

            elif chamber.title() == 'Senate':
                url = 'https://voteview.com/static/data/out/members/S{}_members.csv'.format(session)

            else:
                print('The chamber must either be House or Senate!')
                return None
    
            ideology_df = pds.read_csv(url)

            return ideology_df

        else:
            print('The session must be between 1 and 116!')
            return None
    except:
        print('The session must be convertable to an integer!')
        return None

df = get_ideology_df('115', 'senate')

print(df.keys())