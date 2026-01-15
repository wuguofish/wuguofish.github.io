# 純風景 / 純物件生成指南

## 問題：為什麼一直出現人物？

AI 繪圖模型的訓練資料以「角色圖」為主，即使你只想畫風景或物件，模型也會習慣性地加入人物。

## 核心解法：明確告訴 AI「不要人」

### 萬用公式

```
Positive:
no humans, [主題描述]

Negative:
1girl, 1boy, person, people, human, face, 
figure, character, portrait, body
```

---

## 純風景範例

### 自然風景

```
Positive:
scenery, landscape, no humans,
mountain, lake, forest, 
sunrise, sunbeam, sky,
nature

Negative:
1girl, 1boy, person, human, figure, 
character, face, portrait
```

### 都市風景

```
Positive:
scenery, cityscape, no humans,
city lights, night sky, buildings,
neon lights, rain, reflection,
cyberpunk

Negative:
1girl, 1boy, person, human, figure,
character, face, portrait, crowd
```

### 室內場景

```
Positive:
scenery, indoors, no humans,
[房間類型如 bedroom, library, cafe],
window, chair, lamp,
backlighting

Negative:
1girl, 1boy, person, human, figure,
character, face, portrait
```

---

## 純物件範例

### 食物

```
Positive:
food focus, still life, no humans,
[食物名稱], plate, table,
simple background

Negative:
1girl, 1boy, person, human, hand, hands,
figure, character, face
```

### 花卉

```
Positive:
flower, still life, no humans,
[花的種類如 rose, cherry blossoms, sunflower],
vase, petals, leaf,
simple background

Negative:
1girl, 1boy, person, human, figure,
character, face, portrait
```

### 物品/道具

```
Positive:
object focus, still life, no humans,
[物品名稱],
simple background

Negative:
1girl, 1boy, person, human, hand, hands,
figure, character, face
```

---

## 無人穿戴的服裝/配件

想畫「沒有人穿的鞋子」「放在桌上的帽子」等物品？使用 `unworn_*` 系列 tag：

| 中文 | Tag | 使用次數 |
|------|-----|----------|
| 沒人穿的鞋子 | `unworn shoes` | 11,406 |
| 沒人戴的帽子 | `unworn hat` | 25,260 |
| 沒人戴的頭飾 | `unworn headwear` | 33,236 |
| 沒人戴的眼鏡 | `unworn eyewear` | 14,699 |
| 沒人穿的外套 | `unworn jacket` | 6,594 |
| 沒人穿的裙子 | `unworn skirt` | 8,475 |
| 沒人戴的面具 | `unworn mask` | 6,413 |
| 沒人穿的衣服（通用） | `unworn clothes` | 7,235 |

### 範例：放在地上的鞋子

```
Positive:
still life, no humans,
unworn shoes, sneakers,
wooden floor, sunbeam,
simple background

Negative:
1girl, 1boy, person, human, feet, legs,
figure, character
```

---

## 概念圖專用模板

（適合設計師快速生成示意圖）

### Logo 概念

```
Positive:
logo, simple background, no humans,
[主題], [顏色],
monochrome, white background

Negative:
person, human, character, photo
```

### 海報/Banner 背景

```
Positive:
simple background, no humans,
[風格], [顏色],
gradient background, negative space

Negative:
1girl, 1boy, person, human, character,
figure, face
```

---

## 進階技巧

### 加強「無人」效果

如果還是一直出現人，試著加重權重：

```
(no humans:1.4), scenery
```

### 使用場景專用 tag

有些 tag 天生傾向無人構圖：

| Tag | 使用次數 | 說明 |
|-----|----------|------|
| `scenery` | 52,470 | 風景 |
| `landscape` | 6,078 | 地景 |
| `still life` | 6,813 | 靜物 |
| `food focus` | 11,098 | 食物特寫 |
| `object focus` | 1,301 | 物件特寫 |

### 避免觸發人物的詞

有些詞容易讓 AI 聯想到人物：

| ❌ 容易出現人 | ✅ 改用 |
|--------------|--------|
| `cafe` | `cafe, indoors, no humans` |
| `bedroom` | `bedroom, indoors, no humans` |
| `street` | `scenery, outdoors, no humans` |

---

## 常見問題排除

| 問題 | 解法 |
|------|------|
| 還是出現人 | 加重 `(no humans:1.4)` 權重 |
| 出現人的影子/剪影 | negative 加 `shadow, silhouette` |
| 出現手（例如拿著物件）| negative 加 `hand, hands, holding` |
| 畫面太空 | 加入更多場景細節描述 |
