from pandas import DataFrame
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

class GeoClefCSVFeaturePreprocessor(ColumnTransformer):
    """Preprocessor for features"""
    def __init__(self, column_to_encode):
        self.column_to_encode=column_to_encode # check sklearn's BaseEstimator parent class for more
        
        super().__init__(
            [
                ('categorical', OneHotEncoder(handle_unknown='ignore', sparse_output=True), self.column_to_encode),
            ],
            remainder='passthrough'
        )
        
