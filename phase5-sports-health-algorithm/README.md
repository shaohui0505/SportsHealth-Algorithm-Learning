# 第五阶段：运动健康算法

> 目标：真正进入行业，掌握运动健康领域的核心算法

## 为什么学

这是运动健康算法工程师的核心竞争力——将运动科学与算法结合。

## 学习内容

### 生理信号（`physiological-signals/`）
- ECG（心电）、PPG（光电容积）
- EMG（肌电）、EEG（脑电）
- EDA（皮肤电）、Respiration（呼吸）

### 可穿戴设备（`wearable-devices/`）
- Apple Watch、Garmin、华为、Polar、Whoop、Oura
- 数据格式与采集方式

### 核心算法方向
| 方向 | 内容 | 目录 |
|---|---|---|
| HAR | 人体活动识别 | `har/` |
| 能量消耗 | MET、卡路里估计 | `energy-expenditure/` |
| VO₂max | 最大摄氧量估计 | `vo2max/` |
| HRV | 心率变异性分析 | `hrv/` |
| 疲劳检测 | 恢复状态评估 | `fatigue-detection/` |
| 睡眠识别 | 睡眠分期 | `sleep/` |
| 跌倒检测 | 异常事件检测 | `fall-detection/` |

## 阶段项目

**Apple Watch 运动识别算法**：基于真实可穿戴数据实现端到端的运动识别。

## 目录结构

```
phase5-sports-health-algorithm/
├── physiological-signals/   # 生理信号处理
├── wearable-devices/        # 可穿戴设备
├── har/                     # 人体活动识别
├── energy-expenditure/      # 能量消耗估计
├── vo2max/                  # VO₂max 估计
├── hrv/                     # HRV 分析
├── fatigue-detection/       # 疲劳检测
├── sleep/                   # 睡眠识别
└── fall-detection/          # 跌倒检测
```
