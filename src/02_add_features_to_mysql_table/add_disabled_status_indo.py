import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.insert_update import InsertUpdate
from utils.select_cols import SelectCols
from utils.create_cols import CreateCols
from tqdm import tqdm
from utils.get_disabled_status_by_repo import GetDisabledStatus

'''
    If there is no column inside your table for the word2vec vector result. 
    Uncomments the following line to `Create Column if not exist`
'''
create_column = CreateCols().create_cols(
    {
        "colName": "Disabled_Status",
        "type": "FLOAT"
    }
)


# get all repo name from mysql preload repo namae
repos_name = SelectCols().col_name('full_name')
repos_name_list = [item[0] for item in repos_name ]

# x = GetSize('twbs','bootstrap').get()
# print(x)

for repo_name in tqdm(repos_name_list):
    repo_owner_name_list = repo_name.split('/')
    Disabled_Status_list = GetDisabledStatus(repo_owner_name_list[0], repo_owner_name_list[1]).get()
    InsertUpdate('Disabled_Status').update_val(repo_name, Disabled_Status_list)