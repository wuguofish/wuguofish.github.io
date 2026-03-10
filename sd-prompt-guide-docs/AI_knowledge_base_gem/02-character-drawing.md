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

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969510792091976598?utm_source=eap_blog>)

### 問題 2：想畫成熟男性，結果變阿伯

**原因**：`mature male` 這個詞在訓練集裡常和老年人連結。

**解法**：用外觀特徵來暗示年齡，而非直接描述年齡

| 想要的效果  | 建議用詞（都是有效的 Danbooru tag）                   | 範例圖（PixAI）                                                   |
|--------|--------------------------------------------|--------------------------------------------------------------|
| 少年感    | `bishounen`                                | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969540234820798124?utm_source=eap_blog>) |
| 青年感(1) | `manly`                                    | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969511546958035792?utm_source=eap_blog>) |
| 青年感(2) | `tall male`, `toned male`, `narrowed eyes` | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969512043666331691?utm_source=eap_blog>) |
| 輕熟感    | `tall male`, `stubble`, `muscular male`    | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969539218394127846?utm_source=eap_blog>) |
| 大叔感    | `mature male`, `beard`, `muscular male`    | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969539360340877425?utm_source=eap_blog>) |
| 老人     | `old man`, `grey hair`, `wrinkles`         | [🖼️ 實際生成效果](<https://pixai.art/artwork/1969539540603234330?utm_source=eap_blog>) |

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

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969504032097544233?utm_source=eap_blog>)

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
| [![narrowed eyes](https://images-ng.pixai.art/gi/orig/c54a6078-153e-4e94-ab62-0bc271b19365)](<https://pixai.art/artwork/1969542505303551693?utm_source=eap_blog>) | [![half-closed eyes](https://images-ng.pixai.art/gi/orig/9c2ecb30-37c0-44c9-83e2-bb02ddd660bc)](<https://pixai.art/artwork/1969542583299331470?utm_source=eap_blog>) | [![empty eyes](https://images-ng.pixai.art/gi/orig/25f4a1a2-3535-476e-856c-fde2ba074366)](<https://pixai.art/artwork/1969542719345245388?utm_source=eap_blog>) | [![thick eyebrows](https://images-ng.pixai.art/gi/orig/f9820670-a2c1-46b5-bfad-4fc9b904662c)](<https://pixai.art/artwork/1969542850996724704?utm_source=eap_blog>) |

---

## 男性角色萬用模板

### 基礎模板
```
1boy, solo, male focus, [氣質], [髮型], [髮色],
[眼色], [體型], [服裝], [場景]

```

### 範例：清秀少年

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969546758144778701?utm_source=eap_blog>)

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

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969546938723573302?utm_source=eap_blog>)

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

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969548058845340243?utm_source=eap_blog>)

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


---

# 純風景 / 純物件生成指南

## 問題：為什麼一直出現人物？

AI 繪圖模型的訓練資料以「角色圖」為主，即使你只想畫風景或物件，模型也會習慣性地加入人物。

## 核心解法：明確告訴 AI「不要人」

### 萬用公式

Positive:
```
no humans, [主題描述]

```

Negative:
```
1girl, 1boy, person, people, human, face,
figure, character, portrait, body

```

---

## 純風景範例

### 自然風景

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969565824758421469?utm_source=eap_blog>)

Positive:
```
scenery, landscape, no humans,
mountain, lake, forest,
sunrise, sunbeam, sky, nature

```

Negative:
```
1girl, 1boy, person, human, figure,
character, face, portrait

```

### 都市風景

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969566087377127882?utm_source=eap_blog>)

Positive:
```
scenery, cityscape, no humans,
city lights, night sky, buildings,
neon lights, rain, reflection, cyberpunk

```

Negative:
```
1girl, 1boy, person, human, figure,
character, face, portrait, crowd

```

### 室內場景

🖼️ 實際生成效果：

- [bedroom](<https://pixai.art/artwork/1969566490290644548?utm_source=eap_blog>)
- [library](<https://pixai.art/artwork/1969566674894930484?utm_source=eap_blog>)
- [cafe](<https://pixai.art/artwork/1969566763949038280?utm_source=eap_blog>)

Positive:
```
scenery, indoors, no humans,
[房間類型如 bedroom, library, cafe],
window, chair, lamp, backlighting

```

Negative:
```
1girl, 1boy, person, human, figure,
character, face, portrait

```

---

## 純物件範例

### 食物

🖼️ 實際生成效果：

- [月餅（mooncake）](<https://pixai.art/artwork/1969567576165286765?utm_source=eap_blog>)
- [粽子(zongzi)](<https://pixai.art/artwork/1969567905358623113?utm_source=eap_blog>)
- [湯圓（tangyuan）](<https://pixai.art/artwork/1969567987213912395?utm_source=eap_blog>)
- [珍珠奶茶（bubble tea）](<https://pixai.art/artwork/1969569105725169399?utm_source=eap_blog>)
- [紅茶（black tea）](<https://pixai.art/artwork/1969569384282115582?utm_source=eap_blog>)

Positive:
```
food focus, still life, no humans,
[食物名稱], plate, table, simple background

```

Negative:
```
1girl, 1boy, person, human, hand, hands,
figure, character, face

```

### 花卉

🖼️ 實際生成效果：

- [向日葵（sunflower）](<https://pixai.art/artwork/1969568543605829094?utm_source=eap_blog>)
- [茶花（camellia）](<https://pixai.art/artwork/1969568635850475981?utm_source=eap_blog>)
- [菊花（chrysanthemum）](<https://pixai.art/artwork/1969568713701478423?utm_source=eap_blog>)

Positive:
```
flower, still life, no humans,
[花的種類如 rose, cherry blossoms, sunflower],
vase, petals, leaf, simple background

```

Negative:
```
1girl, 1boy, person, human, figure,
character, face, portrait

```

### 物品/道具

🖼️ 實際生成效果：

- [咖啡豆](<https://pixai.art/artwork/1969569961430983834?utm_source=eap_blog>)
- [文具組合](<https://pixai.art/artwork/1969571477945137988?utm_source=eap_blog>)

Positive:
```
object focus, still life, no humans,
[物品名稱], simple background

```

Negative:
```
1girl, 1boy, person, human, hand, hands,
figure, character, face

```

---

## 無人穿戴的服裝/配件

想畫「沒有人穿的鞋子」「放在桌上的帽子」等物品？使用 `unworn_*` 系列 tag：

| 中文         | Tag               | 使用次數   |
|------------|-------------------|--------|
| 沒人穿的鞋子     | `unworn shoes`    | 11,406 |
| 沒人戴的帽子     | `unworn hat`      | 25,260 |
| 沒人戴的頭飾     | `unworn headwear` | 33,236 |
| 沒人戴的眼鏡     | `unworn eyewear`  | 14,699 |
| 沒人穿的外套     | `unworn jacket`   | 6,594  |
| 沒人穿的裙子     | `unworn skirt`    | 8,475  |
| 沒人戴的面具     | `unworn mask`     | 6,413  |
| 沒人穿的衣服（通用） | `unworn clothes`  | 7,235  |

### 範例：放在地上的鞋子

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969571790031817169?utm_source=eap_blog>) Positive:
```
still life, no humans,
unworn shoes, sneakers,
wooden floor, sunbeam, simple background

```

Negative:
```
1girl, 1boy, person, human, feet, legs,
figure, character

```

---

## 概念圖專用模板

（適合設計師快速生成示意圖）

### Logo 概念

🖼️ 實際生成效果：

- [範例圖 1](<https://pixai.art/artwork/1969573219872526406?utm_source=eap_blog>)
- [範例圖 2](<https://pixai.art/artwork/1969573532817268837?utm_source=eap_blog>)

Positive:
```
logo, simple background, no humans,
[主題], [顏色], monochrome, white background

```

Negative:
```
person, human, character, photo

```

### 海報/Banner 背景

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969575243312079766?utm_source=eap_blog>)

Positive:
```
simple background, no humans,
[風格], [顏色], gradient background, negative space

```

Negative:
```
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

| Tag            | 使用次數   | 說明   |
|----------------|--------|------|
| `scenery`      | 52,470 | 風景   |
| `landscape`    | 6,078  | 地景   |
| `still life`   | 6,813  | 靜物   |
| `food focus`   | 11,098 | 食物特寫 |
| `object focus` | 1,301  | 物件特寫 |

### 避免觸發人物的詞

有些詞容易讓 AI 聯想到人物：

| ❌ 容易出現人   | ✅ 改用                           |
|-----------|--------------------------------|
| `cafe`    | `cafe, indoors, no humans`     |
| `bedroom` | `bedroom, indoors, no humans`  |
| `street`  | `scenery, outdoors, no humans` |

---

## 常見問題排除

| 問題          | 解法                                |
|-------------|-----------------------------------|
| 還是出現人       | 加重 `(no humans:1.4)` 權重           |
| 出現人的影子/剪影   | negative 加 `shadow, silhouette`   |
| 出現手（例如拿著物件） | negative 加 `hand, hands, holding` |
| 畫面太空        | 加入更多場景細節描述                        |


---

# 男性角色 Tag 速查表

本頁整理男性角色相關的 Danbooru tag，方便快速查詢。基礎觀念請參考 畫男性角色。

---

## 體型分類

| 效果    | Tag             | 備註              |
|-------|-----------------|-----------------|
| 精瘦有線條 | `toned male`    | 15,182 筆        |
| 肌肉男   | `muscular male` | 99,142 筆        |
| 壯漢型   | `bara`          | 搭配 `large male` |
| 高個子   | `tall male`     | 常用於青年感          |

💡 `slim`、`slender` 在 Danbooru 已棄用。NoobAI 等 e621 系模型可嘗試 `slim_male`。

---

## 五官特徵

### 眼睛

| 效果   | Tag                |
|------|--------------------|
| 細長眼  | `narrowed eyes`    |
| 半閉眼  | `half-closed eyes` |
| 空洞眼神 | `empty eyes`       |
| 下垂眼  | `droopy eyes`      |

### 眉毛

| 效果  | Tag              |
|-----|------------------|
| 粗眉  | `thick eyebrows` |
| 細眉  | `thin eyebrows`  |

### 臉部毛髮

| 效果  | Tag           |
|-----|---------------|
| 鬍渣  | `stubble`     |
| 鬍子  | `beard`       |
| 落腮鬍 | `facial hair` |

### 其他臉部特徵

| 效果  | Tag                    |
|-----|------------------------|
| 傷疤  | `scar`, `scar on face` |
| 痣   | `mole`, `facial mole`  |

**⚠️ 這些不是有效的 Danbooru tag：**
`sharp eyes`、`gentle eyes`、`soft eyes`、`sharp jawline`、`high nose`

---

## 獸耳 / 幻想種族

| 效果  | Tag                        |
|-----|----------------------------|
| 貓耳男 | `cat boy`, `cat ears`      |
| 狗耳男 | `dog boy`, `dog ears`      |
| 狐耳男 | `fox boy`, `fox ears`      |
| 狼耳男 | `wolf boy`, `wolf ears`    |
| 龍角男 | `dragon boy`, `horns`      |
| 惡魔男 | `demon boy`, `demon horns` |
| 怪物男 | `monster boy`              |
| 精靈  | `elf`, `pointy ears`       |
| 吸血鬼 | `vampire`, `fangs`         |

---

## 服裝速查

### 日常
```
casual clothes, shirt, t-shirt,
jeans, pants, shorts,
hoodie, jacket, sweater

```

### 正式
```
suit, formal, dress shirt,
necktie, vest, blazer

```

### 制服
```
school uniform, military uniform,
police uniform, butler

```

### 和風
```
kimono, yukata, japanese clothes,
hakama, haori

```

### 運動 / 休閒
```
sportswear, jersey, tank top,
shorts, sneakers

```

### 裸露 / 性感
```
topless male, shirtless,
bare chest, open shirt,
unbuttoned, wet clothes

```

---

## 萬用模板

以下模板可直接複製修改使用。詳細說明請參考 畫男性角色。

### 清秀美少年
```
Positive:
1boy, solo, male focus, bishounen,
[髮色] hair, [髮型], [眼色] eyes,
[服裝], [場景]

Negative:
1girl, female, breasts, muscular

```

### 帥氣青年
```
Positive:
1boy, solo, male focus,
[髮色] hair, short hair, [眼色] eyes,
narrowed eyes, tall male, toned male,
[服裝], [場景]

Negative:
1girl, female, breasts

```

### 陽剛型男
```
Positive:
1boy, solo, male focus, manly,
[髮色] hair, short hair, [眼色] eyes,
muscular male, stubble,
[服裝], [場景]

Negative:
1girl, female, breasts, bishounen

```

### 陰鬱美少年
```
Positive:
1boy, solo, male focus, bishounen,
pale skin, [髮色] hair, [眼色] eyes,
empty eyes, expressionless,
dark clothes, simple background

Negative:
1girl, female, breasts, smile

```

### Bara 系
```
Positive:
1boy, solo, male focus, bara,
muscular, large male,
[髮色] hair, short hair, [眼色] eyes,
facial hair,
[服裝], [場景]

Negative:
1girl, female, bishounen

```
