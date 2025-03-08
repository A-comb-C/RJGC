| 这个作业属于哪个课程 | [软件工程2023](https://edu.cnblogs.com/campus/gdgy/SoftwareEngineeringClassof2023/) |
| ------------ | ------------ |
| 这个作业要求在哪里 | [作业要求](https://edu.cnblogs.com/campus/gdgy/SoftwareEngineeringClassof2023/homework/13324) |
| 这个作业的目标 | 实现一个论文查重系统，计算两篇文本的相似度，并输出结果。通过此项目学习代码管理、性能分析、单元测试等软件开发实践。 |

- 作者：蔡梓欣
- 学号：`3223004209`
- GitHub仓库：[RJGC](https://github.com/A-comb-C/RJGC)

# 论文查重系统

## 项目简介
本项目实现了一个简单的论文查重系统，能够计算两篇文本的相似度，并将结果输出到指定文件中。系统基于Python开发，使用了Python标准库`difflib`来计算文本相似度。

## 数据集
在 `dataset` 文件夹中，提供了多组测试文本，包括：
- `orig.txt`：原文文件。
- `orig_0.8_add.txt`：添加了部分内容的抄袭版。
- `orig_0.8_del.txt`：删除了部分内容的抄袭版。
- `orig_0.8_dis_1.txt`：打乱了部分内容的抄袭版。
- `orig_0.8_dis_10.txt`：打乱了部分内容的抄袭版。
- `orig_0.8_dis_15.txt`：打乱了部分内容的抄袭版。

这些文件可以用于测试程序的查重功能。

## 使用方法
1. 确保已安装 Python 3.x。
2. 无需安装依赖 `difflib`，因为它是 Python 的标准库模块，已经随 Python 安装包一起安装好了。你只需要确保你的 Python 环境正常即可。

### 正常运行程序
```bash
python main.py <原文文件路径> <抄袭版文件路径> <输出答案文件路径>
```

#### 示例（以 `test` 文件夹中的数据为例）
```bash
python main.py test/orig.txt test/plagiarized.txt test/output.txt
```

### 启用性能分析
要启用性能分析，请在运行程序时添加 `--profile` 参数：
```bash
python main.py <原文文件路径> <抄袭版文件路径> <输出答案文件路径> --profile <性能分析输出文件路径>
```

#### 示例（以 `dataset` 文件夹中的数据为例）
```bash
python main.py test/orig.txt test/plagiarized.txt test/output.txt --profile test/profile_results.txt
```

性能分析结果将保存到指定的文件中，文件内容为 UTF-8 编码的文本格式。

### 运行单元测试
```bash
python test_main.py
```

## 项目结构

```
your_github_repo/          # GitHub仓库根目录
│
├── 3223004209/            # 以学号命名的文件夹
│   ├── text/              # 示例文件夹
│   │   ├── orig.txt       # 示例中的原文文件
│   │   ├── output.txt     # 示例中的输出结果文件
│   │   ├── plagiarized.txt # 示例中的抄袭版文件
│   │   └── profile_results.txt # 示例中的性能分析结果文件
│   ├── main.py            # 主程序文件
│   ├── test_main.py       # 单元测试文件
│   ├── requirements.txt   # Python依赖文件（本项目无需额外依赖）
│   └── README.md          # 项目说明文件
│
├── dataset/               # 数据集文件夹
│   ├── orig.txt           # 原文文件
│   ├── orig_0.8_add.txt   # 添加内容的抄袭版
│   ├── orig_0.8_del.txt   # 删除内容的抄袭版
│   ├── orig_0.8_dis_1.txt # 打乱内容的抄袭版
│   ├── orig_0.8_dis_10.txt # 打乱内容的抄袭版
│   └── orig_0.8_dis_15.txt # 打乱内容的抄袭版
│
└── .gitignore             # Git忽略文件
```

---

## PSP表格

| PSP2.1 | Personal Software Process Stages | 预估耗时（分钟） | 实际耗时（分钟） |
| ------------ | ------------ |----------|----------|
| **Planning** | **计划** | 30       | 30       |
| · Estimate | · 估计这个任务需要多少时间 | 30       | 30       |
| **Development** | **开发** | 120      | 160      |
| · Analysis | · 需求分析 (包括学习新技术) | 60       | 60       |
| · Design Spec | · 生成设计文档 | 30       | 30       |
| · Design Review | · 设计复审 | 30       | 30       |
| · Coding Standard | · 代码规范 (为目前的开发制定合适的规范) | 30       | 30       |
| · Design | · 具体设计 | 60       | 60       |
| · Coding | · 具体编码 | 120      | 150      |
| · Code Review | · 代码复审 | 30       | 30       |
| · Test | · 测试（自我测试，修改代码，提交修改） | 60       | 60       |
| **Reporting** | **报告** | 90       | 90       |
| · Test Report | · 测试报告 | 30       | 30       |
| · Size Measurement | · 计算工作量 | 30       | 30       |
| · Postmortem & Process Improvement Plan | · 事后总结, 并提出过程改进计划 | 30       | 30       |
| **合计** |  | 420      | 480      |

---




### 项目概述

该项目是一个简单的论文查重系统，旨在通过计算两篇文本的相似度来检测抄袭行为。系统基于Python开发，使用了Python标准库`difflib`来计算文本相似度。项目的主要功能包括：

1. **读取文件内容**：从指定的文件路径读取原文和抄袭版文本。
2. **计算相似度**：使用`difflib.SequenceMatcher`计算两篇文本的相似度。
3. **输出结果**：将相似度结果写入指定的输出文件。
4. **性能分析**：可选地启用性能分析，生成性能分析报告。

### 项目结构

项目的文件结构如下：

```
your_github_repo/          # GitHub仓库根目录
│
├── 3223004209/            # 以学号命名的文件夹
│   ├── text/              # 示例文件夹
│   │   ├── orig.txt       # 示例中的原文文件
│   │   ├── output.txt     # 示例中的输出结果文件
│   │   ├── plagiarized.txt # 示例中的抄袭版文件
│   │   └── profile_results.txt # 示例中的性能分析结果文件
│   ├── main.py            # 主程序文件
│   ├── test_main.py       # 单元测试文件
│   ├── requirements.txt   # Python依赖文件（本项目无需额外依赖）
│   └── README.md          # 项目说明文件
│
├── dataset/               # 数据集文件夹
│   ├── orig.txt           # 原文文件
│   ├── orig_0.8_add.txt   # 添加内容的抄袭版
│   ├── orig_0.8_del.txt   # 删除内容的抄袭版
│   ├── orig_0.8_dis_1.txt # 打乱内容的抄袭版
│   ├── orig_0.8_dis_10.txt # 打乱内容的抄袭版
│   └── orig_0.8_dis_15.txt # 打乱内容的抄袭版
│
└── .gitignore             # Git忽略文件
```

### 主要功能实现

#### 1. 读取文件内容

```python
def read_file(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"文件读取错误: {e}")
        sys.exit(1)
```

该函数用于从指定路径读取文件内容，并返回文件内容字符串。如果文件读取失败，程序会输出错误信息并退出。

#### 2. 计算相似度

```python
def calculate_similarity(text1, text2):
    """计算两个文本的相似度"""
    seq = difflib.SequenceMatcher(None, text1, text2)
    return round(seq.ratio(), 2)
```

该函数使用`difflib.SequenceMatcher`计算两篇文本的相似度，并返回一个保留两位小数的浮点数。

#### 3. 运行查重逻辑

```python
def run_plagiarism_check(original_file, plagiarized_file, output_file):
    """运行查重逻辑"""
    # 读取文件内容
    original_text = read_file(original_file)
    plagiarized_text = read_file(plagiarized_file)

    # 计算重复率
    similarity = calculate_similarity(original_text, plagiarized_text)

    # 输出结果
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"{similarity:.2f}\n")
        print(f"查重结果已保存到: {output_file}")
    except Exception as e:
        print(f"写入答案文件失败: {e}")
        sys.exit(1)
```

该函数负责整个查重流程，包括读取文件、计算相似度以及将结果写入输出文件。

#### 4. 性能分析

```python
if "--profile" in sys.argv:
    try:
        profile_output_file = sys.argv[sys.argv.index("--profile") + 1]
    except IndexError:
        print("错误：未指定性能分析输出文件路径")
        sys.exit(1)

    print(f"性能分析已启用，结果将保存到: {profile_output_file}")

    # 运行性能分析
    profiler = cProfile.Profile()
    profiler.enable()  # 开始性能分析
    run_plagiarism_check(original_file, plagiarized_file, output_file)  # 运行查重逻辑
    profiler.disable()  # 结束性能分析

    # 将性能分析结果保存为 UTF-8 编码的文本文件
    with open(profile_output_file, 'w', encoding='utf-8') as profile_file:
        stats = pstats.Stats(profiler, stream=profile_file)
        stats.sort_stats(pstats.SortKey.TIME)  # 按耗时排序
        stats.print_stats()  # 写入性能分析结果

    print(f"性能分析结果已保存到: {profile_output_file}")
```

该部分代码用于启用性能分析，生成性能分析报告并保存到指定文件中。

### 项目总结

通过本次项目，我学习了如何使用Python进行文本处理、性能分析和单元测试。未来可以进一步优化算法，提升系统的性能和准确度。

---

### 未来改进方向

1. **算法优化**：可以尝试使用更复杂的文本相似度算法，如基于词向量的相似度计算，以提高查重的准确性。
2. **性能优化**：进一步优化代码性能，减少内存占用和运行时间。
3. **扩展功能**：增加对多文件批处理的支持，允许用户一次性输入多个文件进行查重。
