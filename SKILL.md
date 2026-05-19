---
name: lyrics-translation
description: "歌词翻译技能。当用户提供外语歌词要求翻译成中文时触发。触发关键词：翻译歌词 / lyrics translation / 歌词の中訳 / 가사 번역 / 翻唱 / 双语歌词 / 译配 / translate this song to Chinese。不触发：普通文本翻译、文学翻译、脱离音乐语境的诗歌翻译。覆盖20+音乐流派，提供流派差异化翻译策略、韵律匹配、文化适应和可唱性优化指导。"
license: MIT
compatibility: 支持任何现代AI助手，建议具备中文语言能力
metadata:
  author: lyrics-translation-team
  version: "2.0"
  category: translation, music, localization, creative-writing
  languages: en->zh, ja->zh, ko->zh, fr->zh, es->zh, de->zh
  genres-covered: pop, rock, hip-hop, rnb, electronic, jazz, blues, country, folk, metal, punk, reggae, latin, musical, anime, jpop, kpop, ancient-chinese, indie, gospel, children, experimental
  difficulty: intermediate-advanced
  estimated-time: 15-60 minutes per song
  trigger-keywords:
    - 翻译歌词 / lyrics translation / 歌詞翻訳 / 가사 번역
    - 歌词中文翻译 / translate lyrics to Chinese
    - 翻唱中文版 / Chinese cover
    - 双语歌词 / bilingual lyrics
    - 译配 / lyric adaptation for singing
    - 歌词本地化 / lyric localization
    - song lyrics Chinese version
---

# 歌词翻译专业技能

## 触发条件

以下情况应激活本技能：

### 必定触发
- 用户提供了一段外语歌词，要求翻译成中文
- 用户要求制作某首歌的中文翻唱版
- 用户提供歌词原文，要求输出双语对照（原文+译文）
- 用户要求对现有中文歌词进行润色或重新翻译
- 用户要求"译配"歌词（即适配旋律的可唱翻译）

### 可能触发
- 用户询问某首歌的歌词含义、逐句解释
- 用户提到"帮我看一下这段歌词什么意思"，提供的是整段歌词而非个别单词
- 用户要求将中文歌词翻译成其他语言（反向翻译，策略需调整）
- 用户在做音乐相关的学术研究，需要歌词翻译作为参考

### 不应触发
- 用户要求翻译普通文本、文章、邮件（非歌词内容）
- 用户仅询问个别单词的含义而未提供歌词段落
- 用户要求文学翻译（小说、诗歌），除非明确提及音乐/演唱语境

### 关键词检测

| 语言 | 触发关键词 |
|------|-----------|
| 中文 | 歌词翻译、译配、翻唱、中文歌词、双语歌词、歌词本地化、歌词意思、逐句翻译 |
| English | lyrics translation, translate this song, Chinese cover, bilingual lyrics, lyric adaptation, song translation |
| 日本語 | 歌詞翻訳、中国語訳、カバー曲、歌詞の意味、和訳 |
| 한국어 | 가사 번역, 한글 가사, 번역 가사, 노래 가사 번역 |

## 概述
本技能为AI助手提供专业的歌词翻译指导，涵盖从流行到小众的20+音乐流派，帮助用户将外语歌词高质量地翻译成中文，同时保持原作的韵律、情感和艺术性。

## 适用场景
- 原创歌曲的中文化翻译
- 外语歌曲的中文翻唱版本制作
- 歌词字幕的本地化
- 音乐作品的学术研究与分析
- 双语歌词对照本的制作
- 现有中文歌词的润色和优化
- 为KTV或字幕组制作时间轴匹配的翻译

## 输出格式要求

**重要：所有翻译输出必须采用以下简洁的双语对照格式**

### 标准输出格式

```
[原歌词第1行]
[译文第1行]

[原歌词第2行]
[译文第2行]

[原歌词第3行]
[译文第3行]
...
```

### 格式说明
1. **原歌词在上，译文在下**：每行原文后紧跟对应译文
2. **空行分隔**：每组原文+译文之间用空行分隔
3. **保持原结构**：保留原歌词的段落结构（verse、chorus、bridge等）
4. **段落标记**：如需要，可用括号标注段落名称，如 `[Verse 1]`、`[Chorus]`
5. **不添加额外注释**：输出时不需要翻译说明、分析或注释，仅输出双语对照

### 完整输出示例

```
[Verse 1]
Yesterday, all my troubles seemed so far away
昨日，我所有的烦恼仿佛远在天边

Now it looks as though they're here to stay
如今它们却似乎赖着不走

Oh, I believe in yesterday
哦，我怀念昨日

[Chorus]
Suddenly, I'm not half the man I used to be
刹那间，我已不再是从前的自己

There's a shadow hanging over me
阴影笼罩着我

Oh, yesterday came suddenly
哦，昨日来得太突然
```

## 使用方法
1. 提供待翻译的歌词原文
2. 指定歌曲流派（如不确定，AI将进行分析）
3. 确定翻译风格偏好（直译/意译/编译）
4. AI按照流派专项策略进行翻译
5. **输出时严格按照上述双语对照格式**

## 核心原则
详细内容请参考 [翻译核心原则](references/01-translation-principles.md)

### 信达雅三原则
- **信**：忠实传达原作含义，不随意增删
- **达**：中文表达通顺自然，符合语言习惯
- **雅**：保持文学性和艺术美感

### 流派适配原则
不同音乐流派有不同的语言风格要求：
| 流派类型 | 语言风格 | 韵律要求 | 口语化程度 |
|---------|---------|---------|-----------|
| 流行 | 优美流畅 | 中等 | 中等 |
| 摇滚 | 直接有力 | 灵活 | 较高 |
| 嘻哈 | 街头俚语 | 高韵律 | 极高 |
| 爵士 | 诗意朦胧 | 灵活 | 较低 |
| 古风 | 文言典雅 | 严格 | 极低 |
| 儿歌 | 简单易懂 | 严格 | 中等 |

## 流派专项策略

### 常见流派速查表
详细指南请参考 `references/genres/` 目录

| 流派 | 关键词 | 翻译要点 | 常见陷阱 |
|-----|-------|---------|---------|
| 流行 (Pop) | 朗朗上口、情感共鸣 | 保持简洁、注重副歌记忆点 | 过度直译破坏流畅性 |
| 摇滚 (Rock) | 反叛、力量、态度 | 保留原始冲击力、使用短句 | 过于文雅丧失摇滚精神 |
| 嘻哈 (Hip-Hop) | 节奏感、街头文化 | 重视韵脚、保留俚语特色 | 忽略flow和节奏适配 |
| R&B/Soul | 情感细腻、柔美 | 注重情感表达、使用叠词 | 过于生硬破坏柔美感 |
| 电子 (EDM) | 能量、重复、氛围 | 简化语言、强化节奏单元 | 忽略重复段落的微妙变化 |
| 爵士 (Jazz) | 即兴、慵懒、优雅 | 保持诗意、允许模糊性 | 过于直白破坏意境 |
| 蓝调 (Blues) | 忧郁、叙事、重复 | 保留重复结构、情感深度 | 忽略蓝调特有的忧郁感 |
| 乡村 (Country) | 叙事、朴实、生活化 | 使用生活化语言、讲好故事 | 过于城市化失去乡土气息 |
| 民谣 (Folk) | 真诚、简单、诗意 | 保持朴素、注重意境 | 过度修饰失去真诚感 |
| 金属 (Metal) | 暴力、黑暗、力量 | 保留冲击力、可使用古语 | 过于温和失去攻击性 |
| 朋克 (Punk) | 叛逆、直接、粗粝 | 短促有力、保留愤怒感 | 过于精致失去朋克本色 |
| 雷鬼 (Reggae) | 和平、放松、节奏 | 保持轻松感、注意节奏 | 忽略雷鬼特有的节奏韵律 |
| 拉丁 (Latin) | 热情、浪漫、舞蹈 | 保持热情、可保留部分原文 | 忽略拉丁音乐的节奏特色 |
| 古典跨界 (Classical Crossover) | 宏大、优美、典雅 | 用词典雅、句式规整 | 过于通俗丧失古典气质 |
| 音乐剧 (Musical) | 戏剧性、叙事性 | 保持戏剧张力、便于演唱 | 忽略角色性格和剧情背景 |
| 动漫/J-Pop | 热血、中二、情感 | 可保留日式表达、注重情感 | 过于西化失去日式美感 |
| K-Pop | 时尚、青春、能量 | 现代感、可保留韩语词 | 忽略K-Pop特有的语言风格 |
| 古风 | 文言、意境、典雅 | 使用古诗词表达、注重意境 | 现代词汇破坏古典美感 |
| 独立/另类 (Indie) | 独特、实验、个性 | 尊重原创性、不拘泥常规 | 过度标准化失去个性 |
| 福音 (Gospel) | 信仰、希望、力量 | 保留宗教色彩、庄重感 | 世俗化过度失去神圣感 |
| 儿童歌曲 | 简单、趣味、教育 | 用词简单、注重韵律 | 用词复杂超出儿童理解 |
| 实验/前卫 (Experimental) | 抽象、突破、创新 | 灵活处理、允许创造 | 过于保守失去实验精神 |

### 流派详细指南位置
- 流行音乐：[references/genres/pop.md](references/genres/pop.md)
- 摇滚音乐：[references/genres/rock.md](references/genres/rock.md)
- 嘻哈说唱：[references/genres/hip-hop-rap.md](references/genres/hip-hop-rap.md)
- R&B/灵魂乐：[references/genres/rnb-soul.md](references/genres/rnb-soul.md)
- 电子音乐：[references/genres/electronic.md](references/genres/electronic.md)
- 爵士音乐：[references/genres/jazz.md](references/genres/jazz.md)
- 蓝调音乐：[references/genres/blues.md](references/genres/blues.md)
- 乡村音乐：[references/genres/country.md](references/genres/country.md)
- 民谣音乐：[references/genres/folk.md](references/genres/folk.md)
- 金属音乐：[references/genres/metal.md](references/genres/metal.md)
- 朋克音乐：[references/genres/punk.md](references/genres/punk.md)
- 雷鬼音乐：[references/genres/reggae.md](references/genres/reggae.md)
- 拉丁音乐：[references/genres/latin.md](references/genres/latin.md)
- 古典跨界：[references/genres/classical-crossover.md](references/genres/classical-crossover.md)
- 音乐剧：[references/genres/musical-theater.md](references/genres/musical-theater.md)
- 日本动漫/J-Pop：[references/genres/anime-jpop.md](references/genres/anime-jpop.md)
- K-Pop：[references/genres/kpop.md](references/genres/kpop.md)
- 中国古风：[references/genres/chinese-ancient.md](references/genres/chinese-ancient.md)
- 独立/另类：[references/genres/indie-alternative.md](references/genres/indie-alternative.md)
- 福音音乐：[references/genres/gospel.md](references/genres/gospel.md)
- 儿童歌曲：[references/genres/children.md](references/genres/children.md)
- 实验/前卫：[references/genres/experimental.md](references/genres/experimental.md)

## 标准翻译工作流程

### 阶段一：分析与准备
1. **歌词分析**
   - 识别歌曲主题、情感基调、叙事视角
   - 分析韵律结构（节拍、音节数、重音位置）
   - 识别押韵模式（AABB、ABAB、自由韵等）
   - 确定歌曲流派和风格特征

2. **文化背景调研**
   - 查找歌词中的文化引用、典故、俚语
   - 确认专有名词（人名、地名、品牌）的翻译惯例
   - 了解歌曲的创作背景和意图

3. **制定翻译策略**
   - 确定直译/意译/编译的比例
   - 选择押韵方案
   - 确定语言风格（口语化/书面化/文言化）

### 阶段二：初译
1. **逐句直译**
   - 忠实传达原文含义
   - 标记难以直译的部分
   - 记录可能的文化替代方案

2. **韵律调整**
   - 调整词序以匹配节奏
   - 增减衬词以适配音节数
   - 选择同音节数的替代词

### 阶段三：润色优化
1. **押韵处理**
   - 应用押韵技巧（详见 [押韵技巧大全](references/03-rhyme-schemes.md)）
   - 确保韵脚自然不生硬

2. **情感强化**
   - 检查情感传达是否准确
   - 调整用词力度

3. **可唱性测试**
   - 检查是否便于演唱（详见 [演唱适配性指南](references/05-vocal-considerations.md)）
   - 避免拗口的声母组合
   - 确保元音开口度适合旋律

### 阶段四：输出
1. **格式化输出**
   - 严格按照双语对照格式输出
   - 原歌词在上，译文在下
   - 保持原歌词的段落结构
   - 不添加额外注释或分析

2. **最终检查**
   - [ ] 含义准确性
   - [ ] 韵律匹配度
   - [ ] 押韵自然度
   - [ ] 情感传达度
   - [ ] 可唱性评分
   - [ ] 文化适应性
   - [ ] 输出格式正确

## 源语言专项技巧

### 英译中技巧
详细内容：[references/languages/english-to-chinese.md](references/languages/english-to-chinese.md)

**要点速览**：
- 英语多被动句，中文应转为主动
- 英语长句需拆分为中文短句
- 英语时态变化需用时间副词表达
- 英语缩略语需展开翻译

### 日译中技巧
详细内容：[references/languages/japanese-to-chinese.md](references/languages/japanese-to-chinese.md)

**要点速览**：
- 日语敬语体系需简化或转换
- 日语拟声拟态词需寻找中文对应
- 日语特有的暧昧表达需适度保留
- 汉字词汇可直接使用但需考虑语感差异

### 韩译中技巧
详细内容：[references/languages/korean-to-chinese.md](references/languages/korean-to-chinese.md)

**要点速览**：
- 韩语敬语需根据歌曲语境处理
- 韩语特有语气词需寻找替代
- K-Pop中常见的英语混用需统一处理
- 韩语拟声词需创造性翻译

## 常见问题与解决方案 (Gotchas)

### 韵律相关
- **问题**：原文音节数与中文差异大
  - **解决**：使用衬词（啊、呀、哦）、叠词、扩充或压缩表达
  - **示例**："I love you" (3音节) → "我爱着你" (4音节) / "我爱你" (3音节)

- **问题**：原韵脚在中文中无对应
  - **解决**：改变押韵模式或采用近韵
  - **参考**：[押韵技巧大全](references/03-rhyme-schemes.md)

### 文化相关
- **问题**：文化专有名词无对应
  - **解决**：音译+注释 / 意译 / 替换为中文对应文化元素
  - **示例**："Thanksgiving" → "感恩节" / "团圆节"(如需中国化)

- **问题**：不可译的双关语
  - **解决**：保留原文+注释 / 创造新的双关 / 放弃双关改用直译
  - **参考**：[文化适应策略](references/04-cultural-adaptation.md)

### 流派相关
- **问题**：嘻哈中的脏话和俚语
  - **解决**：根据语境选择保留、弱化或替换
  - **参考**：[嘻哈/说唱专项指南](references/genres/hip-hop-rap.md)

- **问题**：古风歌曲中的文言表达
  - **解决**：参考古诗词用语，保持一致性
  - **参考**：[中国古风专项指南](references/genres/chinese-ancient.md)

### 技术相关
- **问题**：快速歌曲音节过多
  - **解决**：精简表达、使用单音节词、删除衬词
  - **参考**：[快歌处理指南](assets/examples/19-special/fast-tempo.md)

- **问题**：极简风格歌词过于简单
  - **解决**：保持简洁、注重留白、强化意境
  - **参考**：[极简风格处理](assets/examples/19-special/minimalist.md)