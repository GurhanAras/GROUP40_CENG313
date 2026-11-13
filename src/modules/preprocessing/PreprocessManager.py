from pandas import DataFrame

from .GeoClefCSVFeaturePreprocessor import GeoClefCSVFeaturePreprocessor
from .GeoClefCSVLabelPreprocessor import GeoClefCSVLabelPreprocessor

class PreprocessManager:
    def __init__(self, df: DataFrame, categorical_columns: list[str]):
        raw_features = (df.groupby("surveyId", as_index=False).first())
        self.feature_preprocessor = GeoClefCSVFeaturePreprocessor(categorical_columns)
        self.features = self.feature_preprocessor.fit_transform(raw_features)
        
        raw_labels = (df.groupby("surveyId", as_index=False).agg(list))
        
        self.label_preprocessor = GeoClefCSVLabelPreprocessor()
        self.labels = self.label_preprocessor.fit_transform(raw_labels)
        