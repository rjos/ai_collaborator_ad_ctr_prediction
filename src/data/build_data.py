from tqdm.auto import tqdm
import pandas as pd
import numpy as np
import pickle
import gc


def load_data(path: str, separator: str = ',', label_column: str = 'label', chunk_size: int = 1_000_000, frac_sample:float = 1.) -> pd.DataFrame:
    """
    """

    data_df = pd.DataFrame()

    for chunk_df in tqdm(pd.read_csv(path, sep=separator, iterator=True, chunksize=chunk_size)):
        sample_chunk_df = chunk_df.groupby(label_column, group_keys=False).apply(lambda group: group.sample(frac=frac_sample))
        sample_chunk_df = reduce_mem_usage(sample_chunk_df)

        data_df = pd.concat([data_df, sample_chunk_df], ignore_index=True)

    return reduce_mem_usage(data_df)


def load_pickle(path: str) -> pd.DataFrame:
    """
    """

    data_df = None

    with open(path, 'rb') as input_dataset:
        data_df = pickle.load(input_dataset)

    return data_df


def save_pickle(filepath: str, df: pd.DataFrame):
    """
    """

    with open(filepath, 'wb') as output_dataset:
        pickle.dump(df, output_dataset)


def reduce_mem_usage(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    
    for col in df.columns:
        col_type = df[col].dtype

        if col_type.name != 'object' or col_type.name != 'category':
            c_min = df[col].min()
            c_max = df[col].max()
            
            if col_type.name[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.uint8).min and c_max < np.iinfo(np.uint8).max:
                    df[col] = df[col].astype(np.uint8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.uint16).min and c_max < np.iinfo(np.uint16).max:
                    df[col] = df[col].astype(np.uint16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.uint32).min and c_max < np.iinfo(np.uint32).max:
                    df[col] = df[col].astype(np.uint32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
                elif c_min > np.iinfo(np.uint64).min and c_max < np.iinfo(np.uint64).max:
                    df[col] = df[col].astype(np.uint64)
            elif col_type.name[:5] == 'float':
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        elif col_type.name != 'datetime':
            df[col] = df[col].astype('category')

    gc.collect()
    return df