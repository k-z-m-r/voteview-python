from pandas import read_csv
from numpy import arange

def generate_df(loc, session, chamber):

    '''
        loc -> the type of data being located.
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    sessions = arange(1, 117)

    try:
        if int(session) in sessions:

            session = str(session)
            while len(session) != 3:
                session = "0" + session

            if chamber.title() == 'House':
                url = 'https://voteview.com/static/data/out/{}/H{}_{}.csv'.format(loc, session, loc)

            elif chamber.title() == 'Senate':
                url = 'https://voteview.com/static/data/out/{}/S{}_{}.csv'.format(loc, session, loc)

            else:
                print('The chamber must either be House or Senate!')
                return None

            df = read_csv(url)

            return df

        else:
            print('The session must be between 1 and 116!')
            return None
    except:
        print('The session must be convertable to an integer!')
        return None

def get_ideology(session, chamber):

    '''
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    return generate_df('members', session, chamber)

def get_bills(session, chamber):

    '''
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    return generate_df('rollcalls', session, chamber)

def get_votes(session, chamber):

    '''
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    return generate_df('votes', session, chamber)

    
def get_parties(session, chamber):

    '''
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    return generate_df('parties', session, chamber)