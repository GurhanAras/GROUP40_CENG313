from modules import read_csv
from modules.preprocessing import PreprocessManager

def main():
    pa_path = "data/PresenceAbsenceSurveys/GLC25_PA_metadata_train.csv"
    # po_path = "data/PresenceOnlyOccurrences/GLC25_PO_metadata_train.csv"
     
    pa_df = read_csv(pa_path, row_count=50)
    
    # metadata_columns = [
    #     "lon", "lat", "year",
    #     "geoUncertaintyInM", "areaInM2",
    #     "region", "country"
    # ]
    categorical_columns = ["region", "country"]
    
    manager = PreprocessManager(pa_df, categorical_columns)
    
    print(manager.features[:5])
    print(manager.labels[:5])


if __name__ == "__main__":
    main()

