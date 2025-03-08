import sys
import difflib
import cProfile
import pstats

def read_file(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"文件读取错误: {e}")
        sys.exit(1)

def calculate_similarity(text1, text2):
    """计算两个文本的相似度"""
    seq = difflib.SequenceMatcher(None, text1, text2)
    return round(seq.ratio(), 2)

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

def main():
    if len(sys.argv) < 4:
        print("用法: python main.py <原文文件路径> <抄袭版文件路径> <输出答案文件路径> [--profile <性能分析输出文件路径>]")
        sys.exit(1)

    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]

    # 检查是否启用性能分析
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
    else:
        # 正常运行查重逻辑
        run_plagiarism_check(original_file, plagiarized_file, output_file)

if __name__ == "__main__":
    main()