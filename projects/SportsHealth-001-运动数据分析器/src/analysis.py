"""
统计分析模块

对清洗后的运动数据进行统计分析：心率、步数、运动时间等。
所有计算基于真实数据，不使用硬编码或伪造数值。
"""

import pandas as pd


def heart_rate_stats(df: pd.DataFrame, hr_col: str = "heart_rate") -> dict:
    """计算心率统计指标。

    Args:
        df: 清洗后的 DataFrame
        hr_col: 心率列名

    Returns:
        包含 max/min/mean/std 的字典
    """
    if hr_col not in df.columns:
        raise ValueError(f"心率列 '{hr_col}' 不存在，可用列：{list(df.columns)}")

    hr = df[hr_col].dropna()
    return {
        "max": float(hr.max()),
        "min": float(hr.min()),
        "mean": float(hr.mean()),
        "std": float(hr.std()),
    }


def daily_steps(df: pd.DataFrame, steps_col: str = "steps", date_col: str = "date") -> pd.Series:
    """统计每日总步数。

    Args:
        df: 清洗后的 DataFrame
        steps_col: 步数列名
        date_col: 日期列名

    Returns:
        按日期分组的步数总和
    """
    if steps_col not in df.columns or date_col not in df.columns:
        raise ValueError(f"缺少必要列，可用列：{list(df.columns)}")

    return df.groupby(date_col)[steps_col].sum()


def daily_exercise_time(df: pd.DataFrame, time_col: str = "exercise_minutes", date_col: str = "date") -> pd.Series:
    """统计每日运动时长（分钟）。"""
    if time_col not in df.columns or date_col not in df.columns:
        raise ValueError(f"缺少必要列，可用列：{list(df.columns)}")

    return df.groupby(date_col)[time_col].sum()


def print_summary(df: pd.DataFrame) -> None:
    """打印数据概览。"""
    print("=" * 50)
    print("数据概览")
    print("=" * 50)
    print(f"总行数: {len(df)}")
    print(f"列名: {list(df.columns)}")
    print("\n缺失值统计:")
    print(df.isnull().sum())
    print("\n描述性统计:")
    print(df.describe())
