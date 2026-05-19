[README.md](https://github.com/user-attachments/files/28010280/README.md)
# lyrics-translation

多语种歌词中文化翻译技能包。基于 Agent Skills 规范，为 AI 提供系统的歌词翻译指导。

## 功能

- 支持英文、日文、韩文、法文、西班牙文等语言到中文的歌词翻译
- 覆盖流行、摇滚、嘻哈、R&B、电子、爵士、蓝调、乡村、民谣、金属、朋克、雷鬼、拉丁、古典跨界、音乐剧、动漫、K-Pop、古风、独立、福音、儿童、实验等 20 余种音乐流派
- 各流派有独立的翻译策略，涉及韵律匹配、押韵处理、文化适应和可唱性评估
- 附带音节计数、押韵检测、可唱性评分等辅助脚本

## 使用方法

1. 向 AI 提供待翻译的歌词原文
2. 指定歌曲流派（不确定时可让 AI 自行分析）
3. 选择翻译风格（直译 / 意译 / 编译）
4. AI 根据流派策略和语言技巧进行翻译
5. 输出采用双语对照格式：原文在上，译文在下，空行分隔

## 目录结构

```
SKILL.md                    # 主技能文件
references/
  01-translation-principles.md      # 翻译核心原则
  02-rhythm-and-meter.md            # 节奏与韵律指南
  03-rhyme-schemes.md               # 中文十三辙押韵技巧
  04-cultural-adaptation.md         # 文化适应策略
  05-vocal-considerations.md        # 演唱适配性指南
  06-common-pitfalls.md             # 常见错误与解决方案
  genres/                           # 22 个音乐流派专项指南
  languages/                        # 4 种源语言翻译技巧
assets/
  templates/                        # 输出格式模板
  examples/                         # 各流派翻译示例
scripts/
  syllable-counter.py               # 音节计数器
  rhyme-checker.py                  # 押韵检测器
  singability-scorer.py             # 可唱性评分器
```

## 翻译要点

- 不同流派对语言风格和韵律的要求差异较大，参考对应流派指南
- 副歌部分应优先保证押韵，主歌可适当放宽
- 文化专有项的处理策略视歌曲类型和受众而定
- 翻译完成后建议朗读或试唱，检查可唱性
