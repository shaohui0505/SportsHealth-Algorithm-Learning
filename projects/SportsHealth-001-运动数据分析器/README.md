# SportsHealth-001：运动数据分析器

> 第一阶段结业项目 —— 读取运动数据，分析心率 / 步数 / 运动时间，输出自动分析报告

## 项目目标

完成从「不会写代码」到「能独立分析数据」的跨越。

## 功能清单

- [ ] 读取一份运动数据（CSV 格式）
- [ ] 分析心率（最大值、最小值、平均值、趋势）
- [ ] 分析步数（每日总步数、步速）
- [ ] 统计每日运动时间
- [ ] 绘制折线图（心率曲线、步数曲线）
- [ ] 绘制统计图（每日运动时长柱状图）
- [ ] 输出一份自动分析报告（Markdown）

## 数据来源

**必须使用真实数据**，禁止使用随机生成的假数据。可选来源：

1. **自有设备数据**：Apple Watch / 华为 / Garmin 导出的 CSV
2. **公开数据集**：
   - [PAMAP2 Physical Activity Monitoring](https://archive.ics.uci.edu/dataset/231/pamap2+physical+activity+monitoring)
   - [UCI Human Activity Recognition](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones)

将数据文件放入 `data/raw/` 目录（该目录已被 `.gitignore` 排除，不会提交大文件）。

## 项目结构

```
SportsHealth-001-运动数据分析器/
├── README.md                  # 本文件
├── data/
│   ├── raw/                   # 原始 CSV 数据（不提交）
│   └── processed/             # 清洗后的数据
├── src/
│   ├── data_loader.py         # 数据读取与清洗
│   ├── analysis.py            # 统计分析
│   └── visualization.py       # 可视化绘图
├── notebooks/                 # 探索性分析 Notebook
└── reports/
    ├── figures/               # 生成的图表
    └── experiment_log.md      # 分析记录
```

## 快速开始

```bash
# 1. 安装依赖（在仓库根目录执行）
pip install -r requirements.txt

# 2. 将运动数据 CSV 放入 data/raw/

# 3. 运行分析
python src/analysis.py
```

## 学习要点

通过本项目掌握：
- Python 文件读写
- Pandas 数据清洗与聚合
- Matplotlib 折线图 / 柱状图
- 时间序列数据处理
- 报告自动生成

## 状态

🚧 进行中 —— 代码模板已就绪，等待填入真实数据和实现分析逻辑。
