
import pandas as pd
import sqlite3
import os

def create_dataframe(path):
    if os.path.exists(path):
        conn = sqlite3.connect(path)
        df = pd.read_sql_query("""
                               select video_id,category_id,'de' as language from DEvideos
                               union
                               select video_id,category_id,'us' as language from USvideos
                               union
                               select video_id,category_id,'gb' as language from GBvideos
                               union
                               select video_id,category_id,'fr' as language from FRvideos
                               union
                               select video_id,category_id,'ca' as language from CAvideos;
                               """,conn)
        return(df)
    else:
        raise ValueError("Incorrect Path provided")


def test_create_dataframe(df):
    name_check = sorted(['video_id', 'category_id', 'language']) == sorted(df.columns)
    key_check = len(pd.unique(df[['video_id','language']].values.ravel('K'))) == len(df)
    nrow_check = len(df) >= 10
    return(name_check and key_check and nrow_check)
