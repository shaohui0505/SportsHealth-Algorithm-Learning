"""
数据读取与清洗模块

负责从 data/raw/ 读取运动数据 CSV，完成基本清洗后输出到 data/processed/。
"""

import pandas as pd
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


def load_csv(filename: str) -> pd.DataFrame:
    """读取原始 CSV 数据。

    Args:
        filename: data/raw/ 目录下的文件名，例如 "sports_data.csv"

    Returns:
        原始 DataFrame
    """
    filepath = RAW_DATA_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(
            f"数据文件不存在：{filepath}\n"
            f"请将运动数据 CSV 放入 {RAW_DATA_DIR} 目录。"
        )
    df = pd.read_csv(filepath)
    print(f"已读取 {filepath.name}，共 {len(df)} 行，{len(df.columns)} 列")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """数据清洗：处理缺失值、类型转换、时间列解析。

    根据实际数据结构调整此函数。
    """
    df = df.copy()

    # TODO: 根据实际列名调整
    # 示例：如果有时间列，转换为 datetime
    # if "timestamp" in df.columns:
    #     df["timestamp"] = pd.to_datetime(df["timestamp"])

    # 删除全空行
    df = df.dropna(how="all")

    return df


def save_processed(df: pd.DataFrame, filename: str) -> Path:
    """保存清洗后的数据到 data/processed/。"""
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PROCESSED_DATA_DIR / filename
    df.to_csv(out_path, index=False)
    print(f"已保存清洗后数据到 {out_path}")
    return out_path


if __name__ == "__main__":
    # 使用示例
    raw = load_csv("sports_data.csv")  # 替换为实际文件名
    cleaned = clean_data(raw)
    save_processed(cleaned, "sports_data_cleaned.csv")
