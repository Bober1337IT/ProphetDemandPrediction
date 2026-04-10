import pandas as pd
import numpy as np


def get_mock_data():
    """
    Generates synthetic e-commerce sales data for testing and demonstration.
    Returns a DataFrame with 'ds' (datestamp) and 'y' (value) columns.
    """
    # Create a range of 100 consecutive days starting from 2023-01-01
    dates = pd.date_range(start="2023-01-01", periods=100, freq="D")

    # 1. Trend: A steady linear increase in sales from 50 to 200 units
    trend = np.linspace(50, 200, 100)

    # 2. Seasonality: A weekly cycle (7-day sine wave) simulating higher weekend sales
    seasonal = 30 * np.sin(np.arange(100) * (2 * np.pi / 7))

    # 3. Noise: Random daily fluctuations to make the data look realistic
    noise = np.random.normal(0, 10, 100)

    # Combine all components into the final target value 'y'
    y = trend + seasonal + noise

    # Prophet model requires specific column names: 'ds' for dates and 'y' for values
    df = pd.DataFrame({'ds': dates, 'y': y})

    return df