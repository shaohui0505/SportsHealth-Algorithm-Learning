"""
可视化模块

绘制心率曲线、步数曲线、运动时长柱状图等。
绘图脚本只读取已计算的真实结果，不生成任何伪造数值。
"""

import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

# 设置中文字体（Windows）
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def plot_heart_rate(df: pd.DataFrame, hr_col: str = "heart_rate", time_col: str = "timestamp") -> Path:
    """绘制心率曲线。

    Returns:
        保存的图片路径
    """
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df[time_col], df[hr_col], color="#e74c3c", linewidth=1)
    ax.set_xlabel("时间")
    ax.set_ylabel("心率 (bpm)")
    ax.set_title("心率曲线")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    out_path = FIGURES_DIR / "heart_rate_curve.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"已保存心率曲线图到 {out_path}")
    return out_path


def plot_daily_steps(daily_steps: pd.Series) -> Path:
    """绘制每日步数柱状图。"""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    daily_steps.plot(kind="bar", ax=ax, color="#3498db")
    ax.set_xlabel("日期")
    ax.set_ylabel("步数")
    ax.set_title("每日步数")
    ax.grid(True, axis="y", alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()

    out_path = FIGURES_DIR / "daily_steps.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"已保存每日步数图到 {out_path}")
    return out_path


def plot_daily_exercise_time(daily_time: pd.Series) -> Path:
    """绘制每日运动时长柱状图。"""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    daily_time.plot(kind="bar", ax=ax, color="#2ecc71")
    ax.set_xlabel("日期")
    ax.set_ylabel("运动时长 (分钟)")
    ax.set_title("每日运动时长")
    ax.grid(True, axis="y", alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()

    out_path = FIGURES_DIR / "daily_exercise_time.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"已保存每日运动时长图到 {out_path}")
    return out_path
