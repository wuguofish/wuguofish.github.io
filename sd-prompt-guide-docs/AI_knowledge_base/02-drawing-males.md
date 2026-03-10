# 畫男生的正確姿勢

## 常見問題與解法

⚠️ 注意：本章節中的所有實際生成效果僅供參考，實際成果仍會因模型不同而略有差異。

### 問題 1：寫了 `1boy` 還是出現女生

**原因**：`1boy` 的權重不夠強，被其他隱含女性特徵的詞蓋過去了。

**解法**：

✅ 正確寫法：
```
1boy, solo, male focus, short hair
```

❌ Negative prompt 必加：
```
1girl, breasts

```

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969510792091976598>)

### 問題 2：想畫成熟男性，結果變阿伯

**原因**：`mature male` 這個詞在訓練集裡常和老年人連結。

**解法**：用外觀特徵來暗示年齡，而非直接描述年齡

| 想要的效果  | 建議用詞（都是有效的 Danbooru tag）                   | 範例圖（PixAI）                                                   |
|--------|--------------------------------------------|--------------------------------------------------------------|
| 少年感    | `bishounen`                                | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969540234820798124>) |
| 青年感(1) | `manly`                                    | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969511546958035792>) |
| 青年感(2) | `tall male`, `toned male`, `narrowed eyes` | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969512043666331691>) |
| 輕熟感    | `tall male`, `stubble`, `muscular male`    | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969539218394127846>) |
| 大叔感    | `mature male`, `beard`, `muscular male`    | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969539360340877425>) |
| 老人     | `old man`, `grey hair`, `wrinkles`         | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969539540603234330>) |

**⚠️ 避免使用這些「模型不認識」的詞**：

- `adult male`、`young man`、`young adult` — 不是 Danbooru tag
- `middle-aged`、`teen`、`teenage` — 不是 Danbooru tag
- `handsome`、`ikemen` — 不是 Danbooru tag

**關鍵**：用具體的外觀特徵（髮型、體格、鬍子）來表達年齡感，而非抽象的年齡詞彙。

### 問題 3：想要美型，結果太陽剛

**解法**：加入「美型」相關的 Danbooru tag

✅ 美型少年風格（都是有效 tag）：
```
1boy, bishounen, androgynous

```

⚠️ 注意：`pretty boy`、`delicate features`、`soft features` 不是有效 tag。

💡 補充：`slim`、`slender` 在 Danbooru 已棄用，但 e621 系模型（如 NoobAI-XL）可使用 `slim_male`。

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969504032097544233>)

### 問題 4：臉型不好看

**解法**：用有效的 Danbooru tag 描述五官

✅ 有效的五官 tag：
```
narrowed eyes（細長眼）
half-closed eyes（半閉眼）
empty eyes（空洞眼神）
thick eyebrows（粗眉）

```

⚠️ 注意：`sharp jawline`、`high nose`、`gentle eyes` 不是有效 tag。

🖼️ 實際生成效果：

| narrowed eyes                                                                                                                                 | half-closed eyes                                                                                                                                 | empty eyes                                                                                                                                 | thick eyebrows                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [![narrowed eyes](https://images-ng.pixai.art/gi/orig/c54a6078-153e-4e94-ab62-0bc271b19365)](<https://pixai.art/artwork/1969542505303551693>) | [![half-closed eyes](https://images-ng.pixai.art/gi/orig/9c2ecb30-37c0-44c9-83e2-bb02ddd660bc)](<https://pixai.art/artwork/1969542583299331470>) | [![empty eyes](https://images-ng.pixai.art/gi/orig/25f4a1a2-3535-476e-856c-fde2ba074366)](<https://pixai.art/artwork/1969542719345245388>) | [![thick eyebrows](https://images-ng.pixai.art/gi/orig/f9820670-a2c1-46b5-bfad-4fc9b904662c)](<https://pixai.art/artwork/1969542850996724704>) |

---

## 男性角色萬用模板

### 基礎模板
```
1boy, solo, male focus, [氣質], [髮型], [髮色],
[眼色], [體型], [服裝], [場景]

```

### 範例：清秀少年

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969546758144778701>)

Positive:
```
1boy, solo, male focus, bishounen,
short hair, black hair, blue eyes, smile,
school uniform, classroom

```

Negative:
```
1girl, female, breasts

```

### 範例：帥氣青年

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969546938723573302>)

Positive:
```
1boy, solo, male focus,
short hair, black hair, narrowed eyes,
tall male, toned male, suit, office

```

Negative:
```
1girl, female, breasts

```

### 範例：陰鬱系美少年

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969548058845340243>)

Positive:
```
1boy, solo, male focus, bishounen,
pale skin, white hair, red eyes,
expressionless, black shirt, simple background

```

Negative:
```
1girl, female, breasts, smile

```

---

## 進階技巧

### 視角問題：為什麼男生也被俯視？

由於 Danbooru 大多數圖片是「可愛的女性角色」，為了反映女性的嬌小可愛以滿足男性觀眾，很多圖的視角是**從上往下看（俯視）**。

這導致有些模型即使畫男生，也會習慣性地使用俯視角度，讓男性角色看起來不夠高大。

**解法**：明確指定視角

| 想要的效果           | 使用的 tag                                                                                  | 實際生成效果 |
|-----------------|------------------------------------------------------------------------------------------|--------|
| 正面平視（平等感）       |                                                                                          |
| [code]          |
|     straight-on |
| ```         |
|                 |
|                 | ![straight-on](https://images-ng.pixai.art/gi/orig/27c816a8-0075-4e28-b324-87d880b517a3) |
| 仰視（高大感）         |                                                                                          |
| [code]          |
|     from below  |
| ```         |
|                 |
|                 | ![from below](https://images-ng.pixai.art/gi/orig/892947e4-7add-441c-ba84-611c8267b913)  |
| 俯視（如果你要的話）      |                                                                                          |
| [code]          |
|     from above  |
| ```         |
|                 |
|                 | ![from above](https://images-ng.pixai.art/gi/orig/a9b81b82-8801-41cd-9325-6e18724072c7)  |

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

| 模型反應               | 建議寫法                          |
|--------------------|-------------------------------|
| 模型對 manly 反應弱      | `(manly:1.5)` ~ `(manly:1.8)` |
| 模型對 manly 反應適中     | `manly` 或 `(manly:1.2)`       |
| 模型對 manly 反應過強（變老） | `(manly:0.6)` ~ `(manly:0.8)` |

**建議做法**：

1. 先用預設權重 `manly` 測試
2. 如果不夠陽剛 → 加高權重
3. 如果變太老 → 降低權重或移除

**補充**：`masculine` 這個 tag 在 Danbooru 不存在，但在 e621 存在。如果使用 NoobAI 等同時訓練於兩個資料庫的模型，`masculine` 可能也有效果，可以嘗試 `manly, masculine` 組合使用。

### 負面 prompt 的重要性

畫男生時，negative prompt 的重要性比畫女生高很多。建議必加：
```
1girl, female, breasts, girl, woman, skirt, dress, makeup, lipstick

```

💡 補充：`feminine` 在 Danbooru 已棄用，放在 negative prompt 中效果可能不穩定，因此從建議中移除。
