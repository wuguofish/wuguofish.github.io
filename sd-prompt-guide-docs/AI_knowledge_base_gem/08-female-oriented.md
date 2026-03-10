# BL / 耽美圖完整指南

> ### SDXL 多角色構圖的限制與替代方案
>
> 「多角色構圖」並非SDXL模型的強項。
>
> 當生成兩個或更多角色時，SDXL 可能會出現**「特徵混淆」**的問題——角色的視覺特徵（如臉部、髮型、服裝）會在彼此之間混雜，而且在生成三人或更多人時會變得更加明顯。
>
> 如果你想要更穩定的多角色效果，也可以考慮使用**基於 DiT 架構的模型** （如 Tsubaki、Serin 等）。
>
> 詳見 推薦 DiT 模型。
>
> 更多的多角色構圖的技巧，可以參考 多角色構圖控制指南。

---

## 常見問題

### 問題：想畫 BL，結果變成 BG（男女）或 GL（女女）

**原因**： 1\. 模型預設傾向畫女性 2\. `2boys` 的權重不夠強 3\. 互動描述詞（如 `kiss`）在訓練集中常與異性戀配對

**解法**：使用區塊分離語法

✅ Positive（使用 right:/left: 區塊分離）：
```
2boys, yaoi, 角色A at right, 角色B at left, 互動, 場景

right: 角色A, 詳細特徵與動作
left: 角色B, 詳細特徵與動作

```

❌ Negative（完全排除女性）：
```
1girl, female, hetero, yuri, breasts,
feminine, woman, girl

```

---

## ⭐ BL 圖黃金公式

> **⚠️ 重要提醒：SDXL模型沒有理解提示詞內構圖配置的能力**
>
>
> 本章節提供的建議寫法是目前中文區社群的大量測試後發現能提高機率的方式之一。
>
> 目前**推測**此方法能提高成功率是靠CLIP的基礎理解能力，但prompt越長效果越差。
>
> 增加 CFG 或許能提升效果，但並不保證能成功。

這是經過實測最有效的寫法，模型能清楚區分兩個角色：
```
2boys, yaoi, 角色1名字 at right, 角色2名字 at left, 互動, 場景描述, 畫風, 品質標籤, LoRA觸發詞

right: 角色1名字, 右邊角色詳細特徵與動作
left: 角色2名字, 左邊角色詳細特徵與動作

```

### 公式解說

| 區塊       | 功能                  |
|----------|---------------------|
| 第一行      | 整體設定：人數、關係、位置、互動、場景 |
| `right:` | 右邊角色的所有細節           |
| `left:`  | 左邊角色的所有細節           |

**重點**：

- 用 `at right` / `at left` 預先宣告角色位置
- 用 `right:` / `left:` 區塊詳細描述各角色
- 這樣寫模型不會把兩人的特徵混在一起

### 互動類型 tag 對照

| 中文    | 英文 tag                            | 備註 |
|-------|-----------------------------------|----|
| 接吻    | `kiss, kissing, french kiss`      |    |
| 擁抱    | `hug, hugging`                    |    |
| 牽手    | `holding hands`                   |    |
| 對視    | `eye contact, looking at another` |    |
| 從背後抱  | `hug from behind`                 |    |
| 壁咚    | `kabedon`                         |    |
| 公主抱   | `princess carry, carrying`        |    |
| 額頭貼額頭 | `forehead-to-forehead`            |    |
| 靠在肩上  | `head on another's shoulder`      |    |
| 膝枕    | `lap pillow`                      |    |

### 身高差/體格差表現

✅ 身高差：
```
height difference, tall male

```

✅ 體格差：
```
muscular male, large male

```

💡 `taller male`、`shorter male`、`slim male` 不是有效的 Danbooru tag。用 `tall male` 搭配具體描述來表達差異。

---

## 範例 prompt

### 範例 1：清純系 BL（校園）

Positive:
```
2boys, yaoi, Hikaru at right, Sora at left, kiss, eye contact, blush, classroom, school uniform, soft lighting

right: Hikaru, short black hair, blue eyes, gentle smile, slightly taller, hand on cheek
left: Sora, messy brown hair, green eyes, surprised expression, blushing

```

Negative:
```
1girl, female, hetero, yuri, breasts, feminine

```

### 範例 2：年上攻 × 年下受

Positive:
```
2boys, yaoi, Ren at right, Yuki at left, hug from behind, height difference, bedroom, night

right: Ren, short hair, black hair, narrowed eyes, tall male, suit, smirk
left: Yuki, messy hair, brown hair, slim, casual clothes, blush

```

Negative:
```
1girl, female, hetero, yuri, breasts, feminine

```

### 範例 3：對等系

Positive:
```
2boys, yaoi, Kuro at right, Shiro at left, holding hands, walking, looking at another, city, sunset

right: Kuro, black hair, red eyes, black jacket, smile
left: Shiro, white hair, blue eyes, white coat, smile

```

Negative:
```
1girl, female, hetero, yuri, breasts, feminine

```

---

## 進階技巧

### 為什麼 `right:` / `left:` 語法有效？

這種區塊語法利用了模型訓練時學到的「條件式描述」結構。 當模型看到 `right:` 開頭的區塊，會把後面的描述只套用到右邊的角色。

### 其他有效的區塊寫法

除了 `right:` / `left:`，以下寫法也有效：

✅ 用數字：
```
1: 角色A特徵
2: 角色B特徵

```

✅ 用名字：
```
Hikaru: 角色A特徵
Sora: 角色B特徵

```

### 避免特徵混在一起的關鍵

1. **先用`at right` / `at left` 宣告位置**
2. **再用`right:` / `left:` 區塊詳述**
3. **讓兩人的髮色、髮型差異明顯** （如黑髮 vs 金髮）
4. **使用對比色眼睛** （如藍眼 vs 紅眼）

### R18 相關 tag

（僅列出常用 tag，請依平台規範使用）
```
裸體：nude, naked
上半身裸：topless male, bare chest
性暗示：suggestive
接吻舌頭：tongue kiss, tongue out

```

---

## 常見錯誤排除

| 問題     | 可能原因              | 解法                                |
|--------|-------------------|-----------------------------------|
| 出現女性   | negative 沒排除乾淨    | 加強 negative prompt                |
| 兩人長得一樣 | 描述不夠具體            | 加大外觀差異                            |
| 變成三人以上 | 沒寫 `2boys`        | 明確寫數量                             |
| 互動不自然  | 構圖太複雜             | 先從簡單構圖開始                          |
| 一人變女性化 | `uke` 等詞有時會觸發女性特徵 | 用具體外觀特徵描述（如 `short hair`、`blush`） |


---

# 夢圖攻略：OC × 角色同框指南

## 什麼是夢圖？

「夢圖」是指將自己的二次元人設（OC, Original Character）和喜歡的角色畫在同一張圖裡的同人創作。

> ### SDXL 多角色構圖的限制與替代方案
>
> 「多角色構圖」並非SDXL模型的強項。
>
> 當生成兩個或更多角色時，SDXL 可能會出現**「特徵混淆」**的問題——角色的視覺特徵（如臉部、髮型、服裝）會在彼此之間混雜，而且在生成三人或更多人時會變得更加明顯。
>
> 如果你想要更穩定的多角色效果，也可以考慮使用**基於 DiT 架構的模型** （如 Tsubaki、Serin 等）。
>
> 詳見 推薦 DiT 模型。
>
> 更多的多角色構圖的技巧，可以參考 多角色構圖控制指南。

---

## 常見問題

### 問題 1：兩個角色的特徵混在一起

**現象**：

- 我的 OC 是紅髮，角色是藍髮，結果兩個都變成紅髮
- 我的 OC 穿便服，角色穿制服，結果兩個都穿制服或是服裝交換

**原因**：AI 傾向「平均化」描述，把所有特徵混在一起分配。

**解法**：使用區塊分離語法（見下方公式）

### 問題 2：我喜歡的角色也變成女生了

**原因**：只寫角色名不夠，模型可能不認識或認錯。

**解法**：在區塊中完整描述角色外觀，不只依賴名字。

### 問題 3：角色認不出來

**原因**：該角色在訓練集中出現次數太少，模型不認得。

**解法**：

1. **用 LoRA**：找該角色專用的 LoRA
2. **詳細描述**：不依賴名字，完整描述角色外觀
3. **參考官方設定**：把角色的髮型、髮色、服裝、配件都寫出來

---

## ⭐ 夢圖黃金公式

> **⚠️ 重要提醒：SDXL模型沒有理解提示詞內構圖配置的能力**
>
>
> 本章節提供的建議寫法是目前中文區社群的大量測試後發現能提高機率的方式之一。
>
> 目前**推測**此方法能提高成功率是靠CLIP的基礎理解能力，但prompt越長效果越差。
>
> 增加 CFG 或許能提升效果，但並不保證能成功。

### BG 向夢圖公式（女 OC × 男角色 / 男 OC × 女角色）
```
(couple), 1boy, 1girl, 互動, 場景描述, 男生大略特徵描述, 女生大略特徵描述, 畫風, 品質標籤, LoRA觸發詞

boy: 男生詳細特徵與動作
girl: 女生詳細特徵與動作

```

### BL 向夢圖公式（男 OC × 男角色）
```
2boys, yaoi, OC名字 at right, 角色名字 at left, 互動, 場景描述, 畫風, 品質標籤, LoRA觸發詞

right: OC名字, OC詳細特徵與動作
left: 角色名字, 角色詳細特徵與動作

```

### 公式解說

| 區塊                 | 功能                     |
|--------------------|------------------------|
| 第一行                | 整體設定：人數、關係、位置、互動、場景、畫風 |
| `boy:` / `girl:`   | BG 向：分別描述男女角色          |
| `right:` / `left:` | BL 向：分別描述左右角色          |

**重點**：

- 這種寫法讓模型能清楚區分兩個角色
- 不會把特徵混在一起
- 搭配 LoRA 效果更好

---

## 範例 prompt

### 範例 1：BG 向夢圖（女 OC × 男角色）

Positive:
```
(couple), 1boy, 1girl, holding hands, looking at another, cafe, brown hair, red hair

boy: short hair, brown hair, golden eyes, smile, tall male, white shirt, sitting
girl: my OC Sakura, long hair, red hair, hair ribbon, green eyes, blush, sundress

```

Negative:
```
yaoi, yuri, multiple boys, multiple girls

```

### 範例 2：BL 向夢圖（男 OC × 男角色）

Positive:
```
2boys, yaoi, my OC Rei at right, Protagonist at left, hug from behind, bedroom, night

right: Rei, long hair, ponytail, silver hair, red eyes, pale skin, black coat
left: Protagonist, short hair, black hair, blue eyes, casual clothes, blush

```

Negative:
```
1girl, female, breasts, feminine, hetero

```

### 範例 3：乙女向夢圖（使用角色 LoRA）

Positive:
```
(couple), 1boy, 1girl, kiss, night sky, starry sky, 角色LoRA觸發詞

boy: 角色名, 角色外觀描述
girl: my OC, long hair, pink hair, purple eyes, white dress, closed eyes, blush

```

Negative:
```
yaoi, yuri, multiple boys, multiple girls

```

※ 在 PixAI 介面上選擇對應的 LoRA 並調整權重即可，不需手動輸入 `<lora:xxx:0.7>` 語法。

---

## 進階技巧

### 第一人稱視角（乙女 CG 風格）

如果你想畫「從自己的視角看著他」的乙女遊戲 CG 風格圖片，請參考：

👉 **第一人稱乙女 CG 指南**

### 為什麼區塊語法有效？

`boy:` / `girl:` 和 `right:` / `left:` 這種寫法利用了模型訓練時學到的「條件式描述」結構。 模型會把該區塊後的描述只套用到對應的角色，不會混在一起。

### 使用 LoRA 強化角色辨識度

如果目標角色有專用 LoRA：

1. 在 PixAI 介面上選擇該 LoRA
2. 在 prompt 中加入 **LoRA 觸發詞**
3. 在介面的 LoRA 控制板調整權重（建議 0.6-0.8）

**寫法範例**：
```
(couple), 1boy, 1girl, 互動, 角色LoRA觸發詞

boy: 角色名, 角色特徵
girl: my OC, OC特徵

```

※ 不需手動輸入 `<lora:xxx:0.7>` 語法，PixAI 會自動處理。

權重太高可能會壓過 OC 的描述，建議從 0.6 開始調整。

### 構圖建議

**容易成功的構圖**：

- 並肩站立
- 一前一後（不重疊）
- 坐在一起（如咖啡廳對坐）
- 牽手（身體不重疊）

**難度較高的構圖**：

- 擁抱（身體重疊多）
- 接吻（臉部靠近）
- 公主抱（姿勢複雜）

建議從簡單構圖開始，熟練後再挑戰複雜構圖。

### 當特徵還是會混在一起時

如果用了公式還是會混，試試：

1. **加大外觀差異**：讓髮色完全相反（如黑 vs 白、紅 vs 藍）
2. **簡化描述**：每個角色只保留 3-4 個最重要的特徵
3. **分開生成**：先分別生成兩人的單人圖，確認特徵正確，再合圖

---

## 常見錯誤排除

| 問題       | 解法                                   |
|----------|--------------------------------------|
| 髮色混在一起   | 加大色差（如 `dark hair` vs `white hair`）  |
| 服裝混在一起   | 用位置詞分離，加強描述具體度                       |
| 變成同一個人   | 加大外觀差異（髮色、髮型、服裝完全不同）                 |
| 角色消失只剩一人 | 確認有寫 `2boys` 或 `1boy 1girl`          |
| 莫名出現第三人  | negative 加 `multiple boys` 或 `crowd` |


---

# 第一人稱乙女 CG 風格指南

## 什麼是乙女 CG 風格？

乙女遊戲（女性向戀愛遊戲）中常見的 CG 構圖：

- 從女主角（玩家）的視角看著男性角色
- 男性角色看著「鏡頭」＝看著你
- 可能有互動：牽手、摸頭、比愛心等

這種構圖讓玩家有「他在看著我」的沉浸感。

---

## 核心 Tag

| Tag                  | 功能           |
|----------------------|--------------|
| `female pov`         | 第一人稱女性視角     |
| `1girl out of frame` | 暗示「我」在畫面外但存在 |
| `hetero`             | 強調異性戀互動      |
| `looking at viewer`  | 角色看著鏡頭（看著你）  |
| `pov hands`          | 畫面中出現「自己的手」  |

---

## ⚠️ 重要提醒

由於訓練資料的關係，`female pov` 有時會觸發 NSFW 內容。

**如果想要單純夢幻唯美的畫面，務必在 negative prompt 加上`nsfw`。**

---

## 萬用公式

Positive:
```
1boy, solo, male focus, female pov,
1girl out of frame, hetero, looking at viewer,
[互動], [角色描述], [場景]

```

Negative:
```
nsfw, nude

```

---

## 範例

### 範例 1：比愛心

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1964289416839594394?utm_source=eap_blog>)

Positive:
```
solo focus, male focus, 1boy,
角色人設, looking at viewer,
half-heart hands, cowboy shot,
simple background, white background,
1girl out of frame, hetero, female pov

```

**重點**：

- `half-heart hands` — 比一半愛心（和畫面外的「我」合成完整愛心）
- `1girl out of frame` \+ `hetero` — 暗示有女生在場但不入鏡

### 範例 2：牽手

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969688080071440546?utm_source=eap_blog>)

Positive:
```
1boy, 角色人設, 地點,
holding hands, looking at viewer,
1girl out of frame, hetero, female pov

```

### 範例 3：吻手

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969688677469070019?utm_source=eap_blog>)

Positive:
```
1boy, 角色人設,
  kissing hand, holding hand, looking at viewer, close-up,
  female pov, 1girl out of frame, 地點

```

### 範例 4：被餵食

🖼️ 實際生成效果：[範例圖](<https://pixai.art/zh/artwork/1959502489562995800?utm_source=eap_blog>)

Positive:
```
1boy, 角色人設,
  holding spoon, incoming food,
  食物,
  sitting, table,
  地點, looking at viewer

```

### 範例 5：即將擁抱

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969684787295042765?utm_source=eap_blog>)

Positive:
```
1boy, incoming hug,
  角色人設, looking at viewer,
  地點

```

### 範例 6：摸臉

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969694437534097090?utm_source=eap_blog>)

Positive:
```
solo focus, male focus, 1boy, 角色人設,
  head tilt, holding another's wrist, looking at viewer, close-up,
  1girl out of frame, hetero, female pov, hand on another's cheek,
  背景

```

### 範例 7：惡搞向－－捏臉頰

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969693954309235518?utm_source=eap_blog>)

Positive:
```
solo focus, male focus, 1boy, 角色人設,
  looking at viewer, close-up,
  1girl out of frame, hetero, female pov,
  hands on another's cheek, cheek squash,
  背景

```

---

## 常用互動 Tag

| 中文    | Tag                          |
|-------|------------------------------|
| 牽手    | `holding hands`, `pov hands` |
| 比一半愛心 | `half-heart hands`           |
| 摸對方的頭 | `hand on another's head`     |
| 摸對方的臉 | `hand on another's cheek`    |
| 被餵食   | `incoming food`              |

---

## 常見問題

**Q: 為什麼會出現女生的身體？**

A: `female pov` 有時會讓模型畫出女性身體部位。加強以下設定：

- Positive 加 `1boy, solo`
- Negative 加 `1girl, breasts, female`

**Q: 為什麼畫面變成 NSFW？**

A: 訓練資料中 `female pov` 常與成人內容連結。Negative 一定要加 `nsfw, nude`。

**Q: 手的位置不對？**

A: 互動類的構圖本來就難度較高。建議：

- 先從簡單的 `looking at viewer` 開始
- 再慢慢加入 `incoming hug` 等互動

---

## 推薦的修正 LoRA

由於許多模型對 `female pov` 的理解不夠好，社群中有許多創作者訓練了專門的修正 LoRA。以下是參考清單：

### 有標示基礎模型

這些 LoRA 有明確標示基礎模型，請選擇與你使用的模型相容的版本。

| 名稱                                                                               | 作者                | 基礎模型                | 觸發詞                                                         |
|----------------------------------------------------------------------------------|-------------------|---------------------|-------------------------------------------------------------|
| [[Hoshino] Female Fingers POV](<https://pixai.art/zh/model/1829204677156840472?utm_source=eap_blog>) | callagainsometime | Hoshino             | `pov`, `pov hands`, `female fingers`, `female pov`          |
| [Female Fingers POV](<https://pixai.art/zh/model/1810901088008722614?utm_source=eap_blog>)           | callagainsometime | Animagine XL V3.1   | `pov`, `finger pov`, `female finger pov`, `slender fingers` |
| [Female POV Hand And Finger](<https://pixai.art/zh/model/1969710978626188643?utm_source=eap_blog>)   | 阿童ATone           | Illustrious-XL-v2.0 | `fpov_hand_finger`                                          |
| [Female POV Kissing Hand](<https://pixai.art/zh/model/1942029360467149364?utm_source=eap_blog>)      | 阿童ATone           | Illustrious-XL-v2.0 | `fpov kissing hand`                                         |

### 未標示基礎模型

這些 LoRA 沒有標示基礎模型，作者資訊也不明確，使用前請自行測試相容性。如果你知道這些 LoRA 的原始來源，歡迎補充！

| 名稱                                                             | 觸發詞                                  | 備註                     |
|----------------------------------------------------------------|--------------------------------------|------------------------|
| [Female POV](<https://pixai.art/zh/model/1788705416870654701?utm_source=eap_blog>) | `female pov`, `fpov`, `pov`, `1girl` | 使用數 55.3k，評價 Excellent |

### 尋找更多 LoRA

這類修正 LoRA 一直有創作者持續提供。如果上述 LoRA 不符合你的需求，可以在 PixAI 的 LoRA Market 用以下關鍵字搜尋：

- `female pov`
- `woman perspective`
- `girl perspective`

**選擇 LoRA 時的注意事項：**

- 確認 LoRA 的 Base Model 是否與你使用的模型相容（Pony、Illustrious、Animagine 等）。關於模型相容性，可參考 [LoRA 基礎與疊加技巧](<08-lora-basics.html>)。
- 如果找不到滿意的 LoRA，也可以考慮自己訓練一個！詳見 [訓練自己的 LoRA](<08b-lora-training.html>)。
