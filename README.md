# SportsHealth-Algorithm-Learning

> 运动健康算法工程师学习路线 —— 从 Python 基础到运动健康算法（HAR、HRV、VO₂max、疲劳检测等）的完整项目集

本仓库是一份**企业级算法工程师培养路线**的实战记录。目标不是上完课，而是通过真实项目积累，具备进入运动健康算法岗位（华为运动健康、Garmin、Apple Health、Keep、小米运动健康等）的核心能力。

---

## 这个岗位到底做什么

运动健康算法工程师不是算法竞赛工程师，绝大多数工作不是研究 Transformer 或发 CVPR，而是：

> **运动科学知识 + 数据分析 + 机器学习 + 信号处理 + 软件工程**
>
> 去解决运动健康中的实际问题。

一年后应能独立完成：

```
手环 PPG + IMU 数据
      ↓
自动识别：跑步 / 骑车 / 深蹲 / 卧推 / HIIT / 久坐
      ↓
计算：心率 / 卡路里 / VO₂max / 疲劳程度 / 恢复建议 / 训练负荷(TRIMP)
      ↓
Apple Watch → 手机 App → 算法模型 → 运动健康建议
```

---

## 六阶段学习路线

| 阶段 | 主题 | 周期 | 核心目标 | 目录 |
|:---:|---|:---:|---|---|
| 1 | 编程基础 + 数据分析 | 2 月 | 从不会写代码到能独立分析数据 | [phase1](phase1-python-data-analysis/) |
| 2 | 数学基础 | 2 月 | 掌握算法所需的统计/线代/概率/优化 | [phase2](phase2-math/) |
| 3 | 机器学习 | 2 月 | 用监督/无监督学习解决运动健康问题 | [phase3](phase3-machine-learning/) |
| 4 | 深度学习 | 2 月 | PyTorch + CNN/RNN/LSTM/Transformer | [phase4](phase4-deep-learning/) |
| 5 | 运动健康算法 | 2 月 | 生理信号、HAR、HRV、VO₂max、疲劳检测 | [phase5](phase5-sports-health-algorithm/) |
| 6 | 企业级项目 | 长期 | 完整系统：运动分类/心率预测/疲劳检测/运动处方 | [phase6](phase6-enterprise-projects/) |

补充技能（贯穿全程）：[信号处理](extras/signal-processing/) · [SQL](extras/sql/) · [Linux/Docker](extras/linux-docker/)

---

## 项目作品集

按难度递进，每个项目都应包含真实数据、可复现代码、实验记录与结果报告。

| 序号 | 项目 | 阶段 | 状态 |
|:---:|---|:---:|:---:|
| SportsHealth-001 | [运动数据分析器](projects/SportsHealth-001-运动数据分析器/) | 1 | 🚧 进行中 |
| SportsHealth-002 | 步数分析 | 2 | ⏳ 待开始 |
| SportsHealth-003 | 卡路里预测 | 3 | ⏳ 待开始 |
| SportsHealth-004 | 运动分类 (HAR) | 4 | ⏳ 待开始 |
| SportsHealth-005 | VO₂max 预测 | 3/5 | ⏳ 待开始 |
| SportsHealth-006 | HRV 分析 | 5 | ⏳ 待开始 |
| SportsHealth-007 | 疲劳检测 | 5 | ⏳ 待开始 |
| SportsHealth-008 | 睡眠识别 | 5 | ⏳ 待开始 |
| SportsHealth-009 | AI 运动教练 | 6 | ⏳ 待开始 |
| SportsHealth-010 | 完整运动健康平台 | 6 | ⏳ 待开始 |

---

## 学习方法（导师 + 企业实战）

每个知识点遵循固定流程：

1. **为什么学** —— 先讲它在运动健康算法中的作用，而非先讲理论
2. **理论讲解** —— 只学真正会用到的知识，避免无关内容
3. **代码实战** —— 从零开始一步步实现
4. **项目应用** —— 把知识放到真实运动健康问题中
5. **代码评审** —— 像企业导师一样找问题、优化代码和思路
6. **项目总结** —— 整理成可放进简历和 GitHub 作品集的项目

---

## 仓库结构

```
SportsHealth-Algorithm-Learning/
├── README.md                           # 本文件：学习路线总览
├── phase1-python-data-analysis/        # 第一阶段：Python + 数据分析
├── phase2-math/                        # 第二阶段：统计/线代/概率/优化
├── phase3-machine-learning/            # 第三阶段：机器学习
├── phase4-deep-learning/               # 第四阶段：PyTorch 深度学习
├── phase5-sports-health-algorithm/     # 第五阶段：运动健康算法
├── phase6-enterprise-projects/         # 第六阶段：企业级项目
├── extras/                             # 补充技能（信号处理/SQL/Linux）
└── projects/                           # 作品集项目
    └── SportsHealth-001-运动数据分析器/
```

---

## 环境准备

- Python 3.10+
- Anaconda / Miniconda
- VS Code
- Git
- Jupyter Notebook

```bash
# 安装基础依赖
pip install -r requirements.txt
```

---

## 关于数据与结果的原则

本仓库所有项目遵循**真实、可追溯、可复现**原则：

- 实验数据必须来自真实采集或公开数据集，不使用随机生成的假数据
- 评估指标、图表必须由模型真实输出计算得到，禁止硬编码或伪造
- 每次实验记录超参数、随机种子、数据划分，确保可复现
- 绘图脚本只读取已落盘的结果文件，不在绘图层生成数值

---

## License

MIT
