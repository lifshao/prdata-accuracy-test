import csv
def csvgz_s3based(bucket, ):
    pass
class PRRepos(object):
    def open(self):
        raise NotImplementedError
    def get_market_summary(self, summgrps):
        raise NotImplementedError
    def get_branding_details(self, brandingname):
        raise NotImplementedError
    def close(self):
        raise NotImplementedError
class CSV_PRRepos(PRRepos):
    def __init__(self, csvfile, targets):
        self.csvfile = csvfile
        self.targets = targets
    def open(self):
        self.f = open(self.csvfile, newline='')
    def close(self):
        try:
            self.f
        except AttributeError:
            return
        self.f.close()
    def get_market_summary(self, summgrps):
        '''
        {
            "name": "markte_summary",
            "details": summgrps,
            "data": {
                "group1": {"groupvalue1":{"target1":"", "target2":""...}...}, "group2"...
            }
        }
        '''
        self.f.seek(0)
        reader = csv.DictReader(self.f)
        dictrs = {"name": "markte_summary", "details": summgrps}
        data = {}
        dictrs['data'] = data
        for row in reader:
            for grp in summgrps:
                grpdata = data.setdefault(grp, {})
                targetdict = grpdata.setdefault(row[grp], {(target, 0) for target in self.targets})
                for target in targetdict.keys():
                    targetdict[target] = targetdict[target] + float(row[target])
        return dictrs
    def get_branding_details(self, brandingname):
        '''
        {
            "name": "branding_details",
            "details": brandingname,
            "data": {
                "brandingname": [{"target1":"", "target2":""...}...]
            }
        }
        '''
        self.f.seek(0)
        reader = csv.DictReader(self.f)
        dictrs = {"name": "branding_details", "details": brandingname}
        brandingdata = []
        data = {brandingname: brandingdata}
        dictrs['data'] = data
        for row in reader:
            if brandingname == row['Branding Name']:
                brandingdata.append({(target, row[target])for target in self.targets})
        return dictrs