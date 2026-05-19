#!/usr/bin/env python3
"""
中文歌词可唱性评分器
评估翻译后的歌词是否便于演唱
"""

import re


def score_initial_consonant_fluency(text):
    """
    声母流畅度评分（权重30%）

    检查：
    - 连续相同声母的出现（扣分）
    - 连续难发音声母的组合（扣分）
    - 评分 0-100
    """
    # 难发音声母组合（中文）
    hard_clusters = [
        'ch', 'sh', 'zh',
    ]

    # 提取每个汉字的声母（简化版）
    chars = list(text)
    score = 100

    # 检查连续难发音
    hard_count = 0
    for i in range(len(chars) - 1):
        c1, c2 = chars[i], chars[i + 1]
        # 简单检测：连续两个都是某些声母开头的
        if re.match(r'[csz]', c1) and re.match(r'[csz]', c2):
            hard_count += 1

    score -= hard_count * 10

    # 检查连续相同辅音（绕口令效应）
    for i in range(len(chars) - 2):
        segment = text[i:i + 3]
        if len(set(segment)) == 1:
            score -= 15

    return max(score, 0)


def score_vowel_openness(text):
    """
    元音开口度评分（权重25%）

    评估歌词的元音是否适合旋律配合
    开口元音（a, o, e, ai, ao等）更适合长音高音
    闭口元音（i, u, ü等）更适合快速短音
    """
    open_vowels = set('aoe')
    close_vowels = set('iuv')  # v代表ü

    chars = list(text)
    open_count = sum(1 for c in chars if c in open_vowels)
    close_count = sum(1 for c in chars if c in close_vowels)
    total = open_count + close_count

    if total == 0:
        return 70  # 中性

    # 理想比例：适当混合，不过度集中
    ratio = open_count / total if total > 0 else 0.5
    if 0.3 <= ratio <= 0.7:
        return 90
    elif 0.2 <= ratio <= 0.8:
        return 70
    else:
        return 50


def score_syllable_density(text, target_syllables=None):
    """
    音节密度评分（权重25%）

    评估每秒钟的音节数是否适合演唱
    实际演唱中，歌词需要与旋律的音符数匹配
    """
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    actual_count = len(chinese_chars)

    if target_syllables is None:
        # 如果没有目标音节数，检查是否在合理范围
        # 一般每句4-12个汉字
        if 4 <= actual_count <= 12:
            return 90
        elif 2 <= actual_count <= 15:
            return 70
        else:
            return 50

    # 与目标音节数比较
    diff = abs(actual_count - target_syllables)
    if diff <= 1:
        return 100
    elif diff <= 3:
        return 80
    elif diff <= 5:
        return 60
    else:
        return 40


def score_naturalness(text):
    """
    自然流畅度评分（权重20%）

    评估翻译后的中文是否自然，是否像地道的歌词
    """
    score = 100

    # 检查是否包含不自然的词汇组合
    unnatural_patterns = [
        r'被.*被',      # 被动句式过度
        r'的.*的.*的',  # 的字堆砌
        r'了.*了.*了',  # 了字过多
        r'而且.*而且',  # 连词堆砌
        r'但是.*但是',  # 转折堆砌
    ]

    for pattern in unnatural_patterns:
        if re.search(pattern, text):
            score -= 15

    # 检查标点使用
    punctuation = re.findall(r'[，。！？；：、]', text)
    char_count = len(re.findall(r'[\u4e00-\u9fff]', text))
    if char_count > 0:
        punct_ratio = len(punctuation) / char_count
        if punct_ratio > 0.3:  # 标点过多
            score -= 10

    return max(score, 0)


def score_singability(lyrics, target_syllables_per_line=None):
    """
    评估歌词的可唱性综合评分

    评估维度：
    1. 声母流畅度（30%）
    2. 元音开口度（25%）
    3. 音节密度（25%）
    4. 自然流畅度（20%）

    参数：
        lyrics: 歌词文本
        target_syllables_per_line: 目标每行音节数（可选）

    返回：
        综合评分和各项分数
    """
    lines = [l.strip() for l in lyrics.split('\n') if l.strip()]
    lines = [l for l in lines if not re.match(r'^\[.*\]$', l)]

    if not lines:
        return {'error': '无歌词可分析'}

    total_scores = {
        'fluency': 0,
        'vowel': 0,
        'density': 0,
        'naturalness': 0,
    }

    for line in lines:
        total_scores['fluency'] += score_initial_consonant_fluency(line)
        total_scores['vowel'] += score_vowel_openness(line)
        total_scores['density'] += score_syllable_density(
            line, target_syllables_per_line
        )
        total_scores['naturalness'] += score_naturalness(line)

    n = len(lines)
    avg_scores = {k: v / n for k, v in total_scores.items()}

    # 加权综合评分
    overall = (
        avg_scores['fluency'] * 0.30 +
        avg_scores['vowel'] * 0.25 +
        avg_scores['density'] * 0.25 +
        avg_scores['naturalness'] * 0.20
    )

    # 评级
    if overall >= 85:
        rating = "优秀 - 非常适合演唱"
    elif overall >= 70:
        rating = "良好 - 稍作调整即可演唱"
    elif overall >= 55:
        rating = "一般 - 需要一定调整"
    else:
        rating = "需改进 - 建议重新翻译"

    return {
        'overall': round(overall, 1),
        'rating': rating,
        'dimensions': {
            '声母流畅度': round(avg_scores['fluency'], 1),
            '元音开口度': round(avg_scores['vowel'], 1),
            '音节密度': round(avg_scores['density'], 1),
            '自然流畅度': round(avg_scores['naturalness'], 1),
        }
    }


def format_score_report(result):
    """格式化评分报告"""
    if 'error' in result:
        return f"错误: {result['error']}"

    report = [
        "=== 歌词可唱性评分报告 ===",
        f"综合评分: {result['overall']}/100",
        f"评级: {result['rating']}",
        "",
        "各维度得分:",
    ]

    for dim, score in result['dimensions'].items():
        bar_length = int(score / 5)
        bar = '█' * bar_length + '░' * (20 - bar_length)
        report.append(f"  {dim}: {score:6.1f} {bar}")

    return '\n'.join(report)


if __name__ == "__main__":
    # 使用示例
    samples = [
        "我爱你中国亲爱的妈妈",
        "夜空中最亮的星 能否听清",
        "你突然的离开 让我不知所措地等待",
        "让我们荡起双桨 小船儿推开波浪",
    ]

    for sample in samples:
        result = score_singability(sample)
        print(f"歌词: {sample}")
        print(format_score_report(result))
        print()