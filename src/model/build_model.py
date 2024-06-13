from sklearn.preprocessing import MinMaxScaler
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from typing import Tuple


def make_pipeline(clf: BaseEstimator, scaler_range:Tuple[int, int] = (0.2, 0.8)) -> Pipeline:
    """
    """

    return Pipeline(steps=[
        ("min_max", MinMaxScaler(feature_range=scaler_range)),
        ("clf", clf)
    ])