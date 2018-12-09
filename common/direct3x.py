def login(username, password, env='prod'):
    serv = Direct_Service(username, password, env)
    serv.login()
    return serv
class Direct_Service:
    '''Represent direct3.x service by one's login.
    Get information from a module/component and return as:
    {
        "name": "",
        "data": {},
        "otherinfo..."
    }'''
    def __init__(self, username, password, env):
        self.username = username
        self.password = password
        self.env = env
    def login(self):
        pass
    def get_assetflows(self, market, **kargs):
        '''Get information from Asset Flows module'''
        pass
    def get_invesmentlist(self, listname, **kargs):
        '''Get information from an invesment list'''
        pass
    def get_searchcriteria(self, critername, **kargs):
        '''Get information from a search criteria'''
        pass