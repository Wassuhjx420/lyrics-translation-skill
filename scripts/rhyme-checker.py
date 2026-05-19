#!/usr/bin/env python3
"""
中文押韵检测器
基于十三辙韵母分类，检测歌词的押韵情况
"""

import re

# 十三辙韵母分类
THIRTEEN_RHYMES = {
    "发花": ["a", "ia", "ua"],
    "梭波": ["o", "e", "uo"],
    "乜斜": ["ie", "üe"],
    "姑苏": ["u"],
    "衣期": ["i", "ü"],
    "怀来": ["ai", "uai"],
    "灰堆": ["ei", "ui"],
    "遥条": ["ao", "iao"],
    "由求": ["ou", "iu"],
    "言前": ["an", "ian", "uan", "üan"],
    "人辰": ["en", "in", "un", "ün"],
    "江阳": ["ang", "iang", "uang"],
    "中东": ["eng", "ing", "ong", "iong"],
}

# 构建韵母到辙名的反向映射
RHYME_TO_TYPE = {}
for rhyme_type, finals in THIRTEEN_RHYMES.items():
    for final in finals:
        RHYME_TO_TYPE[final] = rhyme_type

# 中文拼音韵母提取映射（简化版）
PINYIN_FINALS = {
    'a': 'a', 'o': 'o', 'e': 'e', 'i': 'i', 'u': 'u', 'ü': 'ü',
    'ai': 'ai', 'ei': 'ei', 'ui': 'ui', 'ao': 'ao', 'ou': 'ou',
    'iu': 'iu', 'ie': 'ie', 'üe': 'üe', 'er': 'er',
    'an': 'an', 'en': 'en', 'in': 'in', 'un': 'un', 'ün': 'ün',
    'ang': 'ang', 'eng': 'eng', 'ing': 'ing', 'ong': 'ong',
    'ia': 'ia', 'ua': 'ua', 'uo': 'uo', 'iao': 'iao', 'ian': 'ian',
    'uan': 'uan', 'iang': 'iang', 'uang': 'uang', 'iong': 'iong',
    'uai': 'uai', 'ue': 'üe',
}


def get_final(pinyin):
    """
    从拼音中提取韵母
    简化实现：取拼音中第一个元音之后的部分
    """
    pinyin = pinyin.lower().replace('v', 'ü')

    # 尝试完整匹配
    if pinyin in PINYIN_FINALS:
        return PINYIN_FINALS[pinyin]

    # 从最长到最短尝试匹配韵母
    for length in range(min(4, len(pinyin)), 0, -1):
        candidate = pinyin[-length:]
        if candidate in PINYIN_FINALS:
            return PINYIN_FINALS[candidate]

    return None


def get_rhyme_type(pinyin):
    """获取拼音所属的十三辙类型"""
    final = get_final(pinyin)
    if final:
        return RHYME_TO_TYPE.get(final)
    return None


def check_rhyme(pinyin_a, pinyin_b):
    """检查两个拼音是否押韵"""
    type_a = get_rhyme_type(pinyin_a)
    type_b = get_rhyme_type(pinyin_b)
    return type_a == type_b and type_a is not None


# 常见汉字的拼音映射（示例数据，实际应用应使用完整拼音库）
COMMON_CHAR_PINYIN = {
    '爱': 'ai4', '你': 'ni3', '我': 'wo3', '心': 'xin1', '永': 'yong3',
    '远': 'yuan3', '不': 'bu4', '变': 'bian4', '天': 'tian1', '空': 'kong1',
    '想': 'xiang3', '念': 'nian4', '风': 'feng1', '中': 'zhong1', '行': 'xing2',
    '梦': 'meng4', '痛': 'tong4', '送': 'song4', '懂': 'dong3', '龙': 'long2',
    '红': 'hong2', '光': 'guang1', '长': 'chang2', '江': 'jiang1', '阳': 'yang2',
    '香': 'xiang1', '亮': 'liang4', '浪': 'lang4', '方': 'fang1', '上': 'shang4',
    '人': 'ren2', '春': 'chun1', '云': 'yun2', '心': 'xin1', '深': 'shen1',
    '真': 'zhen1', '问': 'wen4', '分': 'fen1', '尘': 'chen2', '门': 'men2',
    '花': 'hua1', '家': 'jia1', '下': 'xia4', '画': 'hua4', '话': 'hua4',
    '大': 'da4', '马': 'ma3', '达': 'da2', '华': 'hua2', '发': 'fa1',
    '了': 'le5', '好': 'hao3', '小': 'xiao3', '到': 'dao4', '要': 'yao4',
    '笑': 'xiao4', '叫': 'jiao4', '跳': 'tiao4', '鸟': 'niao3', '妙': 'miao4',
    '走': 'zou3', '有': 'you3', '久': 'jiu3', '手': 'shou3', '头': 'tou2',
    '流': 'liu2', '秋': 'qiu1', '右': 'you4', '旧': 'jiu4', '口': 'kou3',
    '来': 'lai2', '开': 'kai1', '海': 'hai3', '外': 'wai4', '白': 'bai2',
    '回': 'hui2', '为': 'wei4', '会': 'hui4', '泪': 'lei4', '美': 'mei3',
    '月': 'yue4', '夜': 'ye4', '写': 'xie3', '别': 'bie2', '切': 'qie4',
    '山': 'shan1', '见': 'jian4', '年': 'nian2', '前': 'qian2', '全': 'quan2',
    '难': 'nan2', '完': 'wan2', '半': 'ban4', '感': 'gan3', '间': 'jian1',
}


def get_line_last_char_pinyin(line):
    """获取中文句子最后一个汉字的拼音"""
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', line)
    if not chinese_chars:
        return None
    last_char = chinese_chars[-1]
    return COMMON_CHAR_PINYIN.get(last_char)


def check_rhyme_scheme(lyrics):
    """
    检测歌词的押韵模式

    参数：
        lyrics: 歌词文本，每行一句

    返回：
        押韵分析结果
    """
    lines = [l.strip() for l in lyrics.split('\n') if l.strip()]
    # 过滤段落标记
    lines = [l for l in lines if not re.match(r'^\[.*\]$', l)]

    results = []
    for i, line in enumerate(lines):
        pinyin = get_line_last_char_pinyin(line)
        if pinyin:
            rhyme_type = get_rhyme_type(pinyin)
            results.append((i + 1, line, pinyin, rhyme_type))
        else:
            results.append((i + 1, line, None, None))

    # 检测韵脚组
    rhyme_groups = {}
    for line_num, line, pinyin, rhyme_type in results:
        if rhyme_type:
            if rhyme_type not in rhyme_groups:
                rhyme_groups[rhyme_type] = []
            rhyme_groups[rhyme_type].append(line_num)

    # 判断押韵模式
    scheme = detect_scheme(results)

    return {
        'lines': results,
        'rhyme_groups': rhyme_groups,
        'scheme': scheme,
    }


def detect_scheme(results):
    """检测押韵模式（AABB, ABAB, ABCB, 自由韵等）"""
    rhyme_types = [r[3] for r in results if r[3] is not None]

    if len(rhyme_types) < 2:
        return "无押韵"

    # AABB模式
    if len(rhyme_types) >= 4:
        if (rhyme_types[0] == rhyme_types[1] and
                rhyme_types[2] == rhyme_types[3]):
            if rhyme_types[0] != rhyme_types[2]:
                return "AABB"

    # ABAB模式
    if len(rhyme_types) >= 4:
        if (rhyme_types[0] == rhyme_types[2] and
                rhyme_types[1] == rhyme_types[3]):
            if rhyme_types[0] != rhyme_types[1]:
                return "ABAB"

    # ABCB模式
    if len(rhyme_types) >= 4:
        if rhyme_types[1] == rhyme_types[3]:
            if rhyme_types[0] != rhyme_types[1] and rhyme_types[2] != rhyme_types[1]:
                return "ABCB"

    # 统计不同韵脚数
    unique_types = set(rhyme_types)
    total_lines = len(rhyme_types)

    if len(unique_types) == 1:
        return "AAAA（一韵到底）"
    elif len(unique_types) == total_lines:
        return "自由韵（无重复韵脚）"
    else:
        return "混合韵"


def format_rhyme_report(analysis):
    """格式化押韵分析报告"""
    report = [
        "=== 押韵分析报告 ===",
        f"押韵模式: {analysis['scheme']}",
        "",
        "逐句分析:",
    ]

    for line_num, line, pinyin, rhyme_type in analysis['lines']:
        rhyme_info = f"{pinyin} [{rhyme_type}]" if rhyme_type else "(无中文)"
        report.append(f"  {line_num:3d} | {rhyme_info:20s} | {line}")

    if analysis['rhyme_groups']:
        report.append("")
        report.append("韵脚分组:")
        for rhyme_type, line_nums in sorted(
                analysis['rhyme_groups'].items(),
                key=lambda x: -len(x[1])
        ):
            report.append(f"  [{rhyme_type}] 第{', '.join(map(str, line_nums))}行")

    return '\n'.join(report)


if __name__ == "__main__":
    # 使用示例
    sample_lines = [
        "我爱你",
        "想着你",
        "念着你",
        "不分离",
    ]

    print("单句押韵检测:")
    for line in sample_lines:
        pinyin = get_line_last_char_pinyin(line)
        if pinyin:
            rhyme_type = get_rhyme_type(pinyin)
            print(f"  '{line}' -> {pinyin} -> [{rhyme_type}]")
    print()

    # 整首分析示例
    test_lyrics = """
[Verse 1]
夜空中最亮的星
能否听清
那仰望的人
心底的孤独和叹息
"""
    analysis = check_rhyme_scheme(test_lyrics)
    print(format_rhyme_report(analysis))