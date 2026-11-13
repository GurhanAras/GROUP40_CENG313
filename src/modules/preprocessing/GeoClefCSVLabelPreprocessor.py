from sklearn.preprocessing import MultiLabelBinarizer

class GeoClefCSVLabelPreprocessor(MultiLabelBinarizer):
    def __init__(self):
        super().__init__(sparse_output=True)
    
    