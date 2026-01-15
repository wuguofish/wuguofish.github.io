# 畫男生的正確姿勢

## 常見問題與解法

### 問題 1：寫了 `1boy` 還是出現女生

**原因**：`1boy` 的權重不夠強，被其他隱含女性特徵的詞蓋過去了。

**解法**：

```
✅ 正確寫法：
1boy, solo, male focus, manly, short hair, flat chest

❌ Negative prompt 必加：
1girl, female, breasts, long hair, feminine, girl
```

### 問題 2：想畫成熟男性，結果變阿伯

**原因**：`mature male` 這個詞在訓練集裡常和老年人連結。

**解法**：用外觀特徵來暗示年齡，而非直接描述年齡

| 想要的效果 | 建議用詞（都是有效的 Danbooru tag） |
|------------|-----------------------------------|
| 少年感 | `bishounen` + `slim` + `short hair` |
| 青年感 | `tall male` + `toned male` + `narrowed eyes` |
| 輕熟感 | `tall male` + `stubble` + `muscular male` |
| 大叔感 | `mature male` + `beard` + `muscular` |
| 老人 | `old man` + `grey hair` + `wrinkles` |

**⚠️ 避免使用這些「模型不認識」的詞**：
- `adult male`、`young man`、`young adult` — 不是 Danbooru tag
- `middle-aged`、`teen`、`teenage` — 不是 Danbooru tag  
- `handsome`、`ikemen` — 不是 Danbooru tag

**關鍵**：用具體的外觀特徵（髮型、體格、鬍子）來表達年齡感，而非抽象的年齡詞彙。

### 問題 3：想要美型，結果太陽剛

**解法**：加入「美型」相關的 Danbooru tag

```
✅ 美型少年風格（都是有效 tag）：
1boy, bishounen, slim, slender, androgynous
```

⚠️ 注意：`pretty boy`、`delicate features`、`soft features` 不是有效 tag。

### 問題 4：臉型不好看

**解法**：用有效的 Danbooru tag 描述五官

```
✅ 有效的五官 tag：
narrowed eyes（細長眼）
half-closed eyes（半閉眼）
empty eyes（空洞眼神）
thick eyebrows（粗眉）
```

⚠️ 注意：`sharp jawline`、`high nose`、`gentle eyes` 不是有效 tag。

---

## 男性角色萬用模板

### 基礎模板

```
1boy, solo, male focus, [氣質], [髮型], [髮色], 
[眼色], [體型], [服裝], [場景]
```

### 範例：清秀少年

```
Positive:
1boy, solo, male focus, bishounen,
short hair, black hair, blue eyes, smile,
slim, school uniform, classroom

Negative:
1girl, female, breasts, feminine
```

### 範例：帥氣青年

```
Positive:
1boy, solo, male focus,
short hair, black hair, narrowed eyes,
tall male, toned male, suit, office

Negative:
1girl, female, breasts, feminine
```

### 範例：陰鬱系美少年

```
Positive:
1boy, solo, male focus, bishounen,
pale skin, white hair, red eyes, 
expressionless, slim,
dark clothes, simple background

Negative:
1girl, female, breasts, smile
```

---

## 進階技巧

### 視角問題：為什麼男生也被俯視？

由於 Danbooru 大多數圖片是「可愛的女性角色」，為了反映女性的嬌小可愛以滿足男性觀眾，很多圖的視角是**從上往下看（俯視）**。

這導致有些模型即使畫男生，也會習慣性地使用俯視角度，讓男性角色看起來不夠高大。

**解法**：明確指定視角

| 想要的效果 | 使用的 tag |
|------------|-----------|
| 正面平視（平等感） | `straight-on` |
| 仰視（高大感） | `from below` |
| 俯視（如果你要的話） | `from above` |

**範例**：想畫出高䠷帥氣的男性

```
1boy, solo, male focus, tall male,
from below, looking at viewer,
...
```

### 權重調整

如果某個特徵一直出不來，可以加強權重：

```
(male focus:1.3), (1boy:1.2), (flat chest:1.2)
```

數值建議範圍：1.1 ~ 1.4，太高容易破圖。

### `manly` 的使用技巧

`manly` 是讓男性角色看起來更陽剛的好用 tag，但**效果因模型而異**：

| 模型反應 | 建議寫法 |
|----------|----------|
| 模型對 manly 反應弱 | `(manly:1.5)` ~ `(manly:1.8)` |
| 模型對 manly 反應適中 | `manly` 或 `(manly:1.2)` |
| 模型對 manly 反應過強（變老） | `(manly:0.6)` ~ `(manly:0.8)` |

**建議做法**：
1. 先用預設權重 `manly` 測試
2. 如果不夠陽剛 → 加高權重
3. 如果變太老 → 降低權重或移除

**補充**：`masculine` 這個 tag 在 Danbooru 不存在，但在 e621 存在。如果使用 NoobAI 等同時訓練於兩個資料庫的模型，`masculine` 可能也有效果，可以嘗試 `manly, masculine` 組合使用。

### 負面 prompt 的重要性

畫男生時，negative prompt 的重要性比畫女生高很多。建議必加：

```
1girl, female, breasts, feminine, girl, woman,
long hair, skirt, dress, makeup, lipstick
```
