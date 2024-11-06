import pandas as pd

@pd.api.extensions.register_dataframe_accessor("Recdf")
class RecDataFrame:
    def __init__(self,pandas_obj):
        super().__init__()
        self._validate(pandas_obj)
        self._obj = pandas_obj
            
    @staticmethod
    def _validate(obj):
        # verify there is a column latitude and a column longitude
        if "Country" not in obj.columns or "Language Family" not in obj.columns or "Language" not in obj.columns:
            raise AttributeError("Must have 'Country', 'Language Family' and 'Language'.")
    
    def df_restr(self,country,fam,lang ):
        if country != "":
            print(country)
            print((self._obj['Country'] == country )&(self._obj['Language Family'] == fam) &(self._obj['Language'] == lang) )
            self = self._obj.loc[(self._obj['Country'] == country )&(self._obj['Language Family'] == fam) &(self._obj['Language'] == lang)]
            return self  
        else:
            self = self._obj.loc[(self._obj['Language Family'] == fam) &(self._obj['Language'] == lang)]
            return self
        

