from typing import Union

import numpy as np
import talib

from jesse.helpers import get_candle_source, slice_candles


def Lowest(candles: np.ndarray, period: int = 180, source_type: str = "low", sequential: bool = False) -> Union[
    float, np.ndarray]:
    """
    Recent Lowest value

    :param candles: np.ndarray
    :param period: int - default: 180
    :param source_type: str - default: "low"
    :param sequential: bool - default: False

    :return: float | np.ndarray
    """

    if len(candles.shape) == 1:
        source = candles
    else:
        candles = slice_candles(candles, sequential)
        source = get_candle_source(candles, source_type=source_type)

    Lowest = talib.MIN(source, timeperiod=period)
    

    return Lowest if sequential else Lowest[-1]

