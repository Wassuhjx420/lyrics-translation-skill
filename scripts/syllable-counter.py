#!/usr/bin/env python3
"""
中文歌词音节计数器
用于计算中文歌词每行的音节数，辅助韵律匹配
"""

import re


def count_chinese_syllables(text):
    """
    计算中文歌词的音节数

    规则：
    - 每个汉字 = 1音节
    - 英文单词按标准音节数计算
    - 数字按实际读音音节计算
    - 标点符号不计入
    """
    text = text.strip()
    if not text:
        return 0

    count = 0

    # 中文字符：每个汉字1音节
    chinese_chars = re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf]', text)
    count += len(chinese_chars)

    # 英文字母/单词：粗略按每4个字母1音节
    english_words = re.findall(r'[a-zA-Z]+', text)
    for word in english_words:
        count += count_english_syllables(word)

    # 数字：按单个数字读音
    digits = re.findall(r'[0-9]', text)
    count += len(digits)

    return count


def count_english_syllables(word):
    """
    计算英文单词的音节数（近似）
    使用简单的元音群计数法
    """
    word = word.lower()
    vowels = 'aeiou'
    count = 0
    prev_is_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_is_vowel:
            count += 1
        prev_is_vowel = is_vowel

    # 处理结尾不发音e
    if word.endswith('e') and count > 1:
        count -= 1

    # 最少1个音节
    return max(count, 1)


def analyze_lyrics_structure(lyrics):
    """
    分析整首歌词的韵律结构

    参数：
        lyrics: 歌词文本，每行一句

    返回：
        每行音节数列表和统计分析
    """
    lines = [l.strip() for l in lyrics.split('\n') if l.strip()]
    # 过滤掉段落标记（如 [Verse 1]）
    lines = [l for l in lines if not re.match(r'^\[.*\]$', l)]

    syllable_counts = []
    for line in lines:
        count = count_chinese_syllables(line)
        syllable_counts.append((line, count))

    total = sum(c for _, c in syllable_counts)
    avg = total / len(syllable_counts) if syllable_counts else 0

    return {
        'lines': syllable_counts,
        'total_syllables': total,
        'avg_syllables_per_line': round(avg, 1),
        'max_syllables': max((c for _, c in syllable_counts), default=0),
        'min_syllables': min((c for _, c in syllable_counts), default=0),
    }


def format_analysis_report(analysis):
    """格式化输出分析报告"""
    report = [
        "=== 歌词音节分析报告 ===",
        f"总句数: {len(analysis['lines'])}",
        f"总音节数: {analysis['total_syllables']}",
        f"平均每句音节数: {analysis['avg_syllables_per_line']}",
        f"最多音节数: {analysis['max_syllables']}",
        f"最少音节数: {analysis['min_syllables']}",
        "",
        "逐句明细:",
    ]
    for line, count in analysis['lines']:
        report.append(f"  {count:3d} | {line}")

    return '\n'.join(report)


if __name__ == "__main__":
    # 使用示例
    samples = [
        "我爱你中国",
        "Yesterday all my troubles seemed so far away",
        "我愛你 心永遠不會變",
        "Let it be, let it be, let it be, let it be",
    ]

    for sample in samples:
        print(f"'{sample}'")
        print(f"  音节数: {count_chinese_syllables(sample)}")
        print()

    # 整首分析示例
    test_lyrics = """
[Verse 1]
Yesterday, all my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday

[Chorus]
Suddenly, I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly
"""
    analysis = analyze_lyrics_structure(test_lyrics)
    print(format_analysis_report(analysis))