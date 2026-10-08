# 第四阶段：深度学习

> 目标：用 PyTorch 搭建神经网络，处理时序生理信号

## 为什么学

可穿戴设备产生的 IMU、PPG、ECG 数据是时序信号，深度学习（尤其是 RNN/LSTM/CNN）是处理这类数据的利器。

## 学习内容

### 框架：PyTorch
- Tensor 操作
- 自动求导
- Dataset / DataLoader
- 模型训练循环

### 核心网络
| 网络 | 适用场景 | 目录 |
|---|---|---|
| 全连接网络 (MLP) | 基础入门 | `pytorch-basics/` |
| CNN | 局部特征提取（信号片段） | `cnn/` |
| RNN / LSTM | 时序依赖建模 | `rnn-lstm/` |
| Transformer | 长序列建模（基础） | `transformer/` |

## 阶段项目

**运动识别（HAR）**：输入 IMU 数据（三轴加速度 + 三轴陀螺仪），识别走路 / 跑步 / 上下楼 / 骑车。

> 这是真实企业项目。

## 目录结构

```
phase4-deep-learning/
├── pytorch-basics/   # PyTorch 基础
├── cnn/              # 卷积神经网络
├── rnn-lstm/         # 循环神经网络
└── transformer/      # Transformer 基础
```
