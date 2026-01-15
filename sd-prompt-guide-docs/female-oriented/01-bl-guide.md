# BL / 耽美圖完整指南

## 常見問題

### 問題：想畫 BL，結果變成 BG（男女）或 GL（女女）

**原因**：
1. 模型預設傾向畫女性
2. `2boys` 的權重不夠強
3. 互動描述詞（如 `kiss`）在訓練集中常與異性戀配對

**解法**：使用區塊分離語法

```
✅ Positive（使用 right:/left: 區塊分離）：
2boys, yaoi, 角色A at right, 角色B at left, 互動, 場景

right: 角色A, 詳細特徵與動作
left: 角色B, 詳細特徵與動作

❌ Negative（完全排除女性）：
1girl, female, hetero, yuri, breasts, 
feminine, woman, girl
```

---

## ⭐ BL 圖黃金公式

這是經過實測最有效的寫法，模型能清楚區分兩個角色：

```
2boys, yaoi, 角色1名字 at right, 角色2名字 at left, 互動, 場景描述, 畫風, 品質標籤, LoRA觸發詞

right: 角色1名字, 右邊角色詳細特徵與動作
left: 角色2名字, 左邊角色詳細特徵與動作
```

### 公式解說

| 區塊 | 功能 |
|------|------|
| 第一行 | 整體設定：人數、關係、位置、互動、場景 |
| `right:` | 右邊角色的所有細節 |
| `left:` | 左邊角色的所有細節 |

**重點**：
- 用 `at right` / `at left` 預先宣告角色位置
- 用 `right:` / `left:` 區塊詳細描述各角色
- 這樣寫模型不會把兩人的特徵混在一起

### 互動類型 tag 對照

| 中文 | 英文 tag | 備註 |
|------|----------|------|
| 接吻 | `kiss, kissing, french kiss` | |
| 擁抱 | `hug, hugging, embrace` | |
| 牽手 | `holding hands, hand holding` | |
| 對視 | `eye contact, looking at another` | |
| 從背後抱 | `hug from behind` | |
| 壁咚 | `wall slam, kabedon` | |
| 公主抱 | `princess carry, carrying` | |
| 額頭貼額頭 | `forehead-to-forehead` | |
| 靠在肩上 | `head on another's shoulder, leaning on shoulder` | |
| 膝枕 | `lap pillow` | |

### 身高差/體格差表現

```
✅ 身高差：
height difference, taller male, shorter male

✅ 體格差：
muscular male, slim male, 
larger male, smaller male
```

---

## 範例 prompt

### 範例 1：清純系 BL（校園）

```
Positive:
2boys, yaoi, Hikaru at right, Sora at left, kiss, eye contact, blush, classroom, school uniform, soft lighting, romantic

right: Hikaru, short black hair, blue eyes, gentle smile, slightly taller, hand on cheek
left: Sora, messy brown hair, green eyes, surprised expression, blushing

Negative:
1girl, female, hetero, yuri, breasts, feminine
```

### 範例 2：年上攻 × 年下受

```
Positive:
2boys, yaoi, Ren at right, Yuki at left, hug from behind, height difference, bedroom, night

right: Ren, short hair, black hair, narrowed eyes, tall male, suit, smirk
left: Yuki, messy hair, brown hair, slim, casual clothes, blush

Negative:
1girl, female, hetero, yuri, breasts, feminine
```

### 範例 3：對等系

```
Positive:
2boys, yaoi, Kuro at right, Shiro at left, holding hands, walking, looking at another, city, sunset

right: Kuro, black hair, red eyes, black jacket, smile
left: Shiro, white hair, blue eyes, white coat, smile

Negative:
1girl, female, hetero, yuri, breasts, feminine
```

---

## 進階技巧

### 為什麼 `right:` / `left:` 語法有效？

這種區塊語法利用了模型訓練時學到的「條件式描述」結構。
當模型看到 `right:` 開頭的區塊，會把後面的描述只套用到右邊的角色。

### 其他有效的區塊寫法

除了 `right:` / `left:`，以下寫法也有效：

```
✅ 用數字：
1: 角色A特徵
2: 角色B特徵

✅ 用名字：
Hikaru: 角色A特徵
Sora: 角色B特徵
```

### 避免特徵混在一起的關鍵

1. **先用 `at right` / `at left` 宣告位置**
2. **再用 `right:` / `left:` 區塊詳述**
3. **讓兩人的髮色、髮型差異明顯**（如黑髮 vs 金髮）
4. **使用對比色眼睛**（如藍眼 vs 紅眼）

### R18 相關 tag

（僅列出常用 tag，請依平台規範使用）

```
裸體：nude, naked
上半身裸：topless, bare chest
性暗示：suggestive, implied yaoi
接吻舌頭：tongue kiss, tongue out
```

---

## 常見錯誤排除

| 問題 | 可能原因 | 解法 |
|------|----------|------|
| 出現女性 | negative 沒排除乾淨 | 加強 negative prompt |
| 兩人長得一樣 | 描述不夠具體 | 加大外觀差異 |
| 變成三人以上 | 沒寫 `2boys` | 明確寫數量 |
| 互動不自然 | 構圖太複雜 | 先從簡單構圖開始 |
| 一人變女性化 | `uke` 等詞有時會觸發女性特徵 | 用 `shorter male` 替代 |
