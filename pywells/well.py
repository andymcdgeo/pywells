import lasio
import pandas as pd
import dlisio

class Well:

    def __init__(self, fname):
        self._las_file = self.load_from_las(fname)

        #Convert header items to attributes
        for k, v in self.header.items():
            for sk, sv in v.items():
                if sk == 'value':
                    setattr(self, k, sv)

    def __str__(self) -> str:
        return f'pywells Well Object - UWI: {self.uwi}, Well Name: {self.wellname}'
        
    def load_from_las(self, fname):
        las_file = lasio.read(fname)
        self.wellname = las_file.well.WELL.value
        self.uwi = las_file.well.UWI.value

        # Convert the data to a pandas dataframe
        self.well_data = las_file.df()
        self.well_data.reset_index(inplace=True)

        # Create a simple dictionary of mnemonics & values
        self.header = {}
        for item in las_file.well:
            self.header[item.mnemonic] = {'description':item.descr, 'value':item.value}

        self.curve_info = {}
        for item in las_file.curves:
            self.curve_info[item.mnemonic] = {'description':item.descr, 'units':item.unit}

        self.params = {}
        
        for item in las_file.params:
            self.params[item.mnemonic] = {'description':item.descr}

        return las_file

    @classmethod
    def load_from_dlis(cls, fname):
        pass

    def header_table(self):
        """
        Generate a pandas dataframe of the well header information.

        Returns
        -------
        dataframe
            Returns a dataframe of the well header information
        """
        #Create dataframe of header
        # header_df = pd.DataFrame(self.header.items(), columns=['Mnemonic', 'Value'])
        header_df = pd.DataFrame.from_dict(self.header, orient='index')
        header_df.reset_index(inplace=True)
        header_df.rename(columns={'index':'mnemonic'}, inplace=True)
        return header_df
        

    def curve_table(self):
        """
        Generate a pandas dataframe of the well's curve information

        Returns
        -------
        dataframe
            Returns a dataframe of the well's curve information
        """
        #Create dataframe of curve info
        curve_df = pd.DataFrame.from_dict(self.curve_info, orient='index')
        curve_df.reset_index(inplace=True)
        curve_df.rename(columns={'index':'mnemonic'}, inplace=True)
        return curve_df
    
    def param_table(self):
        #Create dataframe of parameters
        param_df = pd.DataFrame.from_dict(self.params, orient='index')
        param_df.reset_index(inplace=True)
        param_df.rename(columns={'index':'mnemonic'}, inplace=True)
        return param_df

    def curve_names(self):
        return list(self.curve_info.keys())