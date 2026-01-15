# 男性角色 Tag 大全

本文件整理所有與男性角色相關的 tag，按使用情境分類。

---

## 基礎必備 Tag

畫男性角色時，這些 tag 幾乎每次都要用：

```
1boy                 # 一個男生（必備）
solo                 # 單人（避免多人）
male focus           # 男性為焦點（強化用）
```

**Negative prompt 必加**：
```
1girl, female, breasts, feminine, woman, girl
```

---

## 年齡與氣質分類

### ⚠️ 重要觀念

Danbooru **沒有**「青年」「中年」這類年齡 tag。
模型不認識 `young man`、`adult male`、`middle-aged` 這些詞。

**正確做法**：用外觀特徵來暗示年齡感。

### 有效的 Danbooru Tag

| Tag | 使用次數 | 效果 |
|-----|----------|------|
| `bishounen` | 19,463 | 美型少年，纖細優雅 |
| `manly` | 9,969 | 陽剛感，⚠️ 效果因模型而異 |
| `mature male` | 37,456 | 成熟男性，但容易偏老 |
| `old man` | 10,318 | 明確的老人 |
| `muscular male` | 99,142 | 肌肉男 |
| `toned male` | 15,182 | 精瘦有線條 |

### ⚠️ `manly` 使用須知

`manly` 是讓角色更陽剛的好用 tag，但效果因模型差異很大：

```
模型反應弱 → (manly:1.5) ~ (manly:1.8)
模型反應適中 → manly 或 (manly:1.2)
模型反應過強（變老）→ (manly:0.6) ~ (manly:0.8)
```

**建議**：每換一個模型都要重新測試 `manly` 的最佳權重。

### 用外觀組合表達年齡感

**少年感（清秀、年輕）**
```
bishounen, slim, short hair, soft features
```

**青年感（帥氣、有精神）**
```
tall male, toned male, narrowed eyes, short hair
```

**輕熟感（性感、可靠）**
```
tall male, muscular male, stubble, narrowed eyes
```

**大叔感（穩重、成熟）**
```
mature male, beard, muscular, facial hair
```

### ❌ 不要用這些詞（模型不認識）

```
young man, young adult, adult male
middle-aged, teen, teenage
handsome, ikemen
```
這些不是 Danbooru tag，寫了模型也看不懂。

---

## 體型分類

### 纖細型

```
slim, slender, thin, skinny,
narrow waist, delicate frame
```

### 普通型

```
average build, medium build
（通常不需特別標註）
```

### 精瘦型（有肌肉線條）

```
toned male, athletic,
lean muscle, fit
```

### 肌肉型

```
muscular male, muscular,
abs, pectorals, biceps,
broad shoulders
```

### 壯漢型（Bara）

```
bara, very muscular,
large male, bulky,
hairy, chest hair (可選)
```

---

## 五官特徵

### 眼睛形狀

| 效果 | tag |
|------|-----|
| 細長眼 | `narrowed eyes` |
| 銳利眼神 | `sharp eyes` |
| 溫柔眼神 | `gentle eyes`, `soft eyes` |
| 下垂眼 | `droopy eyes` |
| 半閉眼 | `half-closed eyes` |
| 空洞眼神 | `empty eyes` |

### 眉毛

| 效果 | tag |
|------|-----|
| 粗眉 | `thick eyebrows` |
| 細眉 | `thin eyebrows` |

### 臉部特徵

| 效果 | tag |
|------|-----|
| 銳利下顎 | `sharp jawline` |
| 高挺鼻子 | `high nose` |
| 鬍渣 | `stubble` |
| 鬍子 | `beard` |
| 落腮鬍 | `facial hair` |
| 傷疤 | `scar`, `scar on face` |
| 痣 | `mole`, `facial mole` |

---

## 獸耳/幻想種族

| 效果 | tag |
|------|-----|
| 貓耳男 | `cat boy`, `cat ears` |
| 狗耳男 | `dog boy`, `dog ears` |
| 狐耳男 | `fox boy`, `fox ears` |
| 狼耳男 | `wolf boy`, `wolf ears` |
| 龍角男 | `dragon boy`, `horns` |
| 惡魔男 | `demon boy`, `demon horns` |
| 怪物男 | `monster boy` |
| 精靈 | `elf`, `pointy ears` |
| 吸血鬼 | `vampire`, `fangs` |

---

## 服裝快速參考

### 日常服裝

```
casual clothes, shirt, t-shirt, 
jeans, pants, shorts,
hoodie, jacket, sweater
```

### 正式服裝

```
suit, formal, dress shirt,
necktie, vest, blazer
```

### 制服類

```
school uniform, military uniform,
police uniform, butler
```

### 和風

```
kimono, yukata, japanese clothes,
hakama, haori
```

### 運動/休閒

```
sportswear, jersey, tank top,
shorts, sneakers
```

### 性感/裸露

```
topless male, shirtless,
bare chest, open shirt,
unbuttoned, wet clothes
```

---

## 萬用模板庫

### 模板 A：清秀美少年

```
Positive:
1boy, solo, male focus, bishounen,
[髮色] hair, [髮型], [眼色] eyes,
slim, 
[服裝], [場景]

Negative:
1girl, female, breasts, feminine, 
muscular, old man, wrinkles
```

### 模板 B：帥氣青年

```
Positive:
1boy, solo, male focus,
[髮色] hair, short hair, [眼色] eyes,
narrowed eyes, tall male, toned male,
[服裝], [場景]

Negative:
1girl, female, breasts, feminine,
bishounen, old man
```

### 模板 C：陽剛型男

```
Positive:
1boy, solo, male focus, manly,
[髮色] hair, short hair, [眼色] eyes,
muscular male, stubble,
[服裝], [場景]

Negative:
1girl, female, breasts, feminine,
bishounen, slim
```

### 模板 D：陰鬱美少年

```
Positive:
1boy, solo, male focus, bishounen,
pale skin, [髮色] hair, [眼色] eyes,
slim, empty eyes, expressionless,
dark clothes, simple background

Negative:
1girl, female, breasts, feminine,
smile, muscular
```

### 模板 E：Bara 系

```
Positive:
1boy, solo, male focus, bara,
muscular, large male,
[髮色] hair, short hair, [眼色] eyes,
facial hair,
[服裝], [場景]

Negative:
1girl, female, slim,
bishounen, feminine
```

---

## 常見問題 Q&A

**Q: 為什麼加了 `1boy` 還是出女生？**

A: `1boy` 權重不夠，需要加上 `male focus`, `solo`，並在 negative 加入 `1girl, female, breasts`。

**Q: `mature male` 為什麼變阿伯？**

A: 這個詞在訓練集常與老年人連結。想要輕熟男請用 `tall male` + `stubble` + 具體外觀描述，不要用年齡相關的詞。

**Q: 怎麼畫出美型但不女性化的男生？**

A: 用 `bishounen` + `male focus`，並加入一些男性特徵如 `flat chest`, `narrow waist` 但避免 `feminine`。

**Q: `muscular` 和 `muscular male` 有什麼差別？**

A: `muscular male` 更明確指向男性，建議優先使用。`muscular` 可能會讓模型聯想到肌肉女。

**Q: 怎麼畫出「攻」和「受」的差異？**

A: 
- 攻：`taller male`, `muscular`, `sharp eyes`, `smirk`
- 受：`shorter male`, `slim`, `soft features`, `blush`
- 避免用 `uke`, `seme` 等詞，效果不穩定
