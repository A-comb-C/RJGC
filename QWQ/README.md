# 个人项目作业 - 论文查重

## 项目简介

本项目是一个论文查重工具，基于 Python 实现。通过对比原文和抄袭版论文的文本内容，计算两者的相似度，并将结果输出到指定文件中。项目使用了 Python 内置的 `difflib` 库来实现文本相似度计算，并结合文件读写和性能分析功能。

## 项目结构

```
project/
├── test/                   # 测试文件夹
│   ├── orig.txt            # 原文文件
│   ├── plagiarized.txt     # 抄袭版论文文件
│   ├── output.txt          # 查重结果输出文件
│   ├── profile_output.txt  # 性能分析结果文件
│   └── test_file.txt       # 单元测试临时文件
├── dataset/                # 数据集文件夹
│   ├── orig.txt            # 原文文件
│   ├── orig_0.8_add.txt    # 添加内容的抄袭版
│   ├── orig_0.8_del.txt    # 删除内容的抄袭版
│   ├── orig_0.8_dis_1.txt  # 修改内容的抄袭版（1处修改）
│   ├── orig_0.8_dis_10.txt # 修改内容的抄袭版（10处修改）
│   └── orig_0.8_dis_15.txt # 修改内容的抄袭版（15处修改）
├── main.py                 # 主程序文件
└── README.md               # 项目说明文件
```

## 论文查重原理

### 1. 文本相似度计算

本项目使用 Python 内置的 `difflib.SequenceMatcher` 类来计算文本相似度。`SequenceMatcher` 基于最长公共子序列（Longest Common Subsequence, LCS）算法，能够高效地比较两个文本的相似性。

#### 算法核心
- **最长公共子序列**：找到两个文本中最长的相同子序列。
- **相似度计算**：通过公式 `similarity = (2 * LCS长度) / (文本1长度 + 文本2长度)` 计算相似度。

#### 示例
- 原文：`今天是星期天，天气晴，今天晚上我要去看电影。`
- 抄袭版：`今天是周天，天气晴朗，我晚上要去看电影。`
- 相似度计算结果：`0.81`

### 2. 文件读写

项目通过 Python 的文件读写功能，从指定路径读取原文和抄袭版论文，并将查重结果写入输出文件。

### 3. 性能分析

使用 Python 内置的 `cProfile` 模块对程序进行性能分析，找出性能瓶颈并优化代码。

---

## 使用方法

### 1. 运行程序

使用以下命令运行论文查重程序：

```bash
python main.py <原文文件路径> <抄袭版文件路径> <输出答案文件路径> [--profile <性能分析输出文件路径>]
```

#### 示例

```bash
python main.py test/orig.txt test/plagiarized.txt test/output.txt --profile test/profile_output.txt
```

### 2. 参数说明

- `<原文文件路径>`：原文文件的路径（如 `test/orig.txt`）。
- `<抄袭版文件路径>`：抄袭版论文文件的路径（如 `test/plagiarized.txt`）。
- `<输出答案文件路径>`：查重结果输出文件的路径（如 `test/output.txt`）。
- `--profile <性能分析输出文件路径>`：可选参数，启用性能分析并将结果保存到指定文件（如 `test/profile_output.txt`）。

### 3. 输出结果

- 查重结果会保存到 `<输出答案文件路径>` 中，格式为浮点数，精确到小数点后两位。
- 如果启用了性能分析，性能分析结果会保存到 `<性能分析输出文件路径>` 中。

---

## 测试说明

### 1. 单元测试

项目中包含单元测试，确保代码的正确性。运行以下命令执行单元测试：

```bash
python main.py
```

#### 测试用例

- `test_calculate_similarity`：测试相似度计算功能。
- `test_read_file`：测试文件读取功能。
- `test_run_plagiarism_check`：测试查重逻辑。

### 2. 数据集测试

使用 `dataset/` 文件夹中的文件进行测试：

```bash
python main.py dataset/orig.txt dataset/orig_0.8_add.txt test/output.txt
python main.py dataset/orig.txt dataset/orig_0.8_del.txt test/output.txt
python main.py dataset/orig.txt dataset/orig_0.8_dis_1.txt test/output.txt
python main.py dataset/orig.txt dataset/orig_0.8_dis_10.txt test/output.txt
python main.py dataset/orig.txt dataset/orig_0.8_dis_15.txt test/output.txt
```

---

## 评分规则

### 1. 博客评分规则（总分 60 分）

- **Gitcode 链接**：在博客正文首行给出作业 Gitcode 链接。（3 分）
- **PSP 表格**：记录预估和实际开发时间。（6 分）
- **接口设计与实现**：描述代码组织、算法关键点。（18 分）
- **性能改进**：记录性能改进过程，展示性能分析图。（12 分）
- **单元测试**：展示单元测试代码和覆盖率截图。（12 分）
- **异常处理**：介绍异常设计目标和测试样例。（6 分）
- **实际开发时间记录**：在 PSP 表格中记录实际开发时间。（3 分）

### 2. 程序评分规则（总分 40 分）

- **算法性能**：时间、资源占用、准确度等。（20 分）
- **代码可读性**：注释清晰，代码结构合理。（10 分）
- **命名规范**：变量、函数、类命名规范。（10 分）

---

## 附录

### 1. PSP 表格

| PSP2.1 | 任务阶段 | 预估耗时（分钟） | 实际耗时（分钟） |
|--------|----------|------------------|------------------|
| Planning | 计划 | 10 | 10 |
| · Estimate | 估计任务时间 | 10 | 10 |
| Development | 开发 | 120 | 150 |
| · Analysis | 需求分析 | 20 | 30 |
| · Design Spec | 设计文档 | 10 | 15 |
| · Design Review | 设计复审 | 10 | 10 |
| · Coding Standard | 代码规范 | 10 | 10 |
| · Design | 具体设计 | 20 | 25 |
| · Coding | 具体编码 | 30 | 40 |
| · Code Review | 代码复审 | 10 | 10 |
| · Test | 测试 | 10 | 10 |
| Reporting | 报告 | 30 | 40 |
| · Test Report | 测试报告 | 10 | 15 |
| · Size Measurement | 计算工作量 | 10 | 10 |
| · Postmortem | 事后总结 | 10 | 15 |
| 合计 |  | 160 | 200 |

### 2. Gitcode 使用

- 代码签入要求：每完成一个功能后至少提交一次。
- Commit 规范：遵循功能划分提交代码。

### 3. 单元测试

- 至少设计 10 个测试用例。
- 使用白盒测试方法，确保程序正确处理各种情况。
