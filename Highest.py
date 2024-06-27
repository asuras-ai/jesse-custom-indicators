from typing import Union

import numpy as np
import talib

from jesse.helpers import get_candle_source, slice_candles


def Highest(candles: np.ndarray, period: int = 180, source_type: str = "high", sequential: bool = False) -> Union[
    float, np.ndarray]:
    """
    Recent Highest value

    :param candles: np.ndarray
    :param period: int - default: 180
    :param source_type: str - default: "high"
    :param sequential: bool - default: False

    :return: float | np.ndarray
    """

    if len(candles.shape) == 1:
        source = candles
    else:
        candles = slice_candles(candles, sequential)
        source = get_candle_source(candles, source_type=source_type)

    Highest = talib.MAX(source, timeperiod=period)
    

    return Highest if sequential else Highest[-1]
