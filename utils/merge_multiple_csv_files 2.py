import pandas as pd
import os

# This is the path where you want to search
path = r'/Users/Henry/Desktop/github'

# this is the extension you want to detect
extension = '.csv'

Empty_CSV_File_Name_List = []
def GetCsvFileNameList(path):
    for root, dirs_list, files_list in os.walk(path):
        for file_name in files_list:
            if os.path.splitext(file_name)[-1] == extension:
                Empty_CSV_File_Name_List.append(file_name)
    return Empty_CSV_File_Name_List


CSV_File_Name_List = GetCsvFileNameList(path)

Empty_Dataframe_List = []

def GetAllCsvDataFrame(CSV_File_Name_List):
    for file_name in CSV_File_Name_List:
        df = pd.read_csv(path+"/"+file_name)
        Empty_Dataframe_List.append(df)
    return Empty_Dataframe_List

Dataframe_List = GetAllCsvDataFrame(CSV_File_Name_List)


def ConcatAllDataFrame():
    result = pd.concat(Dataframe_List)
    return result

All_data_frame = ConcatAllDataFrame()
Final_data_frame = All_data_frame.drop_duplicates()
Reindex_Data_Frame = Final_data_frame.reindex()
a = Reindex_Data_Frame.drop(Reindex_Data_Frame.columns[0] , axis='columns')
# a.to_csv("/Users/Henry/Desktop/processedGitHubData.csv")


