# 常見實用小技巧

本章整理 Prompt 撰寫的基礎技巧，適合剛接觸 PixAI 的新手快速上手。

---

## PixAI 基本功能說明

### 提示詞相關

| 功能        | 說明                                                   |
|-----------|------------------------------------------------------|
| **提示詞助手** | PixAI 內建的小 LLM，開啟後算圖前會把提示詞重新改寫成能算出東西的內容。打開就可以用中文寫提示。 |
| **自動補全**  | 輸入任一字元，自動帶出可能的提示詞。                                   |
| **負面提示詞** | 不希望畫面出現的東西放在這裡。負面的優先權高於正面。                           |
| **品質標籤**  | 可以當作常用的提示詞存放簿。                                       |

### 生成參數

| 參數            | 說明                                               |
|---------------|--------------------------------------------------|
| **取樣步數**      | 越多步越精細，也越貴（消耗更多點數）。                              |
| **CFG Scale** | 越高越聽話（嚴格遵守提示詞），但太高會崩圖。一般建議 5~7。                  |
| **Seed**      | 決定算圖的初始雜訊。Seed 一樣時，提示詞接近的情況下，會出現幾乎一致的結果。很適合用來微調。 |
| **尺寸**        | 成品的長寬比例。不同比例適合不同構圖。                              |
| **生成數量**      | 一次生幾張圖。多張可以挑選最滿意的。                               |

### 進階功能

| 功能             | 說明                       | 備註                 |
|----------------|--------------------------|--------------------|
| **面部修復**       | 針對人臉做修復，可以避免臉糊掉。         | 舊模型可能出現奇怪方框        |
| **HiRes**      | 修復畫質和擴圖用。                | 詳見 HiRes 放大        |
| **參考圖片**       | 讓 AI 參考整體畫面構圖。數值越低越接近原圖。 | 0 = 完全一致，1 = 完全不參考 |
| **角色參考**       | 讓 AI 參考角色外觀。             | 實測效果因模型而異          |
| **ControlNet** | 控制構圖畫面用（姿勢、線稿等）。         | 進階功能               |

---

## 提示詞撰寫的重要觀念

### Tag 必須存在於資料庫

PixAI上目前大多數受歡迎的 SDXL 模型是用 Danbooru / e621 的圖片訓練的，
所以用這兩個圖片分享網站 **資料庫裡有的 tag 效果最穩定可靠**。

💡 不在資料庫的詞有時也能用（如 `red chess piece`），因為模型的 text encoder（CLIP）有基礎的英文理解能力，會嘗試組合近似概念。但效果不如正式 tag 穩定，建議優先使用資料庫內的 tag。

📚 延伸閱讀：為什麼 CLIP 能理解自然語言？

**中文資源：**

- [[Stable Diffusion雜談] Stable Diffusion 與 CLIP 的基本原理](<https://youtu.be/oLSpkO619FM>)（工gin師）
- [一次掌握CLIP：AI跨模態理解的關鍵技術](<https://vocus.cc/article/69084b3efd89780001af5fa7>)（Josh的沙龍）
- [[Day29] SD XL：SD的限界突破](<https://ithelp.ithome.com.tw/articles/10339667>)（Nick・iT邦鐵人賽）

**英文資源：**

- [CLIP: Connecting text and images](<https://openai.com/index/clip/>)（OpenAI 官方）
- [OpenAI CLIP Model Explained](<https://www.lightly.ai/blog/clip-openai>)（Lightly）
- [Two Text Encoders in SDXL 1.0](<https://mybyways.com/blog/two-text-prompts-text-encoders-in-sdxl-1-0>)（myByways）
- [SDXL 官方文檔](<https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0>)（Hugging Face）

**常見錯誤：**
❌ `young man` → 不存在（改用 `1boy` \+ 具體特徵）
❌ `handsome` → 不存在（改用 `bishounen` 或 `manly`）
❌ `narrow eyes` → 不存在（正確是 `narrowed eyes`）

### 底線要換成空白

Danbooru、e621的Tag 資料庫在某些介面下會用底線（`black_hair`），但實際輸入時用空白（`black hair`）。

### 實用工具：PixAI Tagger

不知道一張圖該用什麼 tag？可以用 PixAI 官方的 Tagger 工具來分析：

[![PixAI Tagger](https://cdn-avatars.huggingface.co/v1/production/uploads/63047b40bad6ce7fc0249261/q_wXWEc5Fatvd9hQI56yN.jpeg) PixAI Tagger Demo ➚](<https://huggingface.co/spaces/pixai-labs/pixai-tagger-demo>)

上傳圖片後，工具會自動辨識圖片中的元素並列出對應的 tag。很適合用來學習「這種畫面要用什麼 tag 描述」。

---

## 提示詞排序建議

提示詞的順序會影響生成結果。建議依照以下順序撰寫：
```
畫面主元素, 畫面細節元素, 鏡頭, 畫風, 品質標籤
```

**範例**：
```
1boy, black hair, short hair, blue eyes,
upper body,
anime style,
masterpiece, best quality
```

| 順序  | 類型     | 範例                                         |
|-----|--------|--------------------------------------------|
| 1   | 畫面主元素  | `1boy`, `1girl`, `scenery`                 |
| 2   | 畫面細節元素 | `black hair`, `blue eyes`, `smile`         |
| 3   | 鏡頭     | `upper body`, `close-up`, `from below`     |
| 4   | 畫風     | `anime style`, `illustration`, `realistic` |
| 5   | 品質標籤   | `masterpiece`, `best quality`              |

💡 **小提醒**：每個元素用逗號分隔，提示詞可分行，但運算時分行會被忽略。

---

## 權重符號

權重符號可以控制 AI 對某個詞彙的重視程度。

### 直接指定權重（推薦）

使用 `(關鍵字:權重)` 的格式，數值範圍約 0.1 ~ 2.0：

- **小於 1**：減弱效果
- **大於 1**：增強效果

```
(black hair:1.2)    # 稍微加強
(blue eyes:1.4)     # 明顯加強
(smile:0.8)         # 稍微減弱
```

⚠️ **注意**：權重建議不要超過 1.5，太高容易導致畫面崩壞。

### 括號權重（進階）

⚠️ **建議在 PixAI 上只使用小括號`()`**，大括號 `{}` 和方括號 `[]` 的行為在不同平台上不一致，容易造成混淆。

| 寫法      | 範例               | 效果                  |
|---------|------------------|---------------------|
| `(關鍵字)` | `((black hair))` | 每層括號 ×1.1，雙層 = 1.21 |

💡 **建議**：直接用 `(關鍵字:權重)` 的寫法最直觀好控制，也最不容易出錯。

### 跳脫字元

如果你的提示詞本身就需要括號（例如角色名稱），使用反斜線跳脫：
```
\(特殊符號\)
```

但一般情況下很少需要這樣做。

---

## 運算符號（⚠️ PixAI 不適用）

⚠️ **重要提醒**：以下符號經社群驗證，**在 PixAI 上無效**。這些是 A1111（Automatic1111 WebUI）等本地端工具的功能，PixAI 並不支援。

📖 想深入了解 PixAI 上哪些語法有效、哪些無效，可以參考 PixAI 官方 Discord 中 Maki 整理的實驗文章：[Using Emphasis on PixAI](<https://discord.com/channels/1041682784856584273/1462309387564744869>)。

| 符號    | 範例                | 原本預期的效果  | 在 PixAI 上的狀況             |
|-------|-------------------|----------|--------------------------|
| `AND` | `a cat AND a dog` | 同時滿足兩個條件 | ❌ A1111 功能，PixAI 無效      |
| `+`   | `a cat + a dog`   | 同時滿足兩個條件 | ❌ 未確認有效果                 |
| `     |`                  | `red     |blue hair`                | 隨機選擇其中一個 | ❌ ComfyUI 的 OR 語法，PixAI 無效 |
| `_`   | `coffee_cake`     | 連接成單一概念  | ⚠️ 通常等同於空白，除非該 tag 本身含底線 |

💡 **結論**：在 PixAI 上請直接使用逗號分隔的標準寫法，不需要使用這些運算符號。

---

## 畫風 Tag 參考

常用的畫風標籤，可依照想要的風格選擇：

| 中文    | 英文 tag           | 效果          |
|-------|------------------|-------------|
| 插畫風   | `illustration`   | 精緻的插畫風格     |
| 繪畫風   | `painting`       | 傳統繪畫質感      |
| 動漫風   | `anime`          | 日式動漫風格      |
| 漫畫風   | `comic`          | 漫畫風格        |
| 數位繪   | `digital art`    | 數位繪圖風格      |
| 遊戲 CG | `game CG`        | 遊戲 CG 風格    |
| 半寫實   | `semi-realistic` | 介於動漫與寫實之間   |
| 2.5D  | `2.5D`           | 有立體感的 2D 風格 |
| 寫實風   | `realistic`      | 接近真實的風格     |
| 照片風   | `photograph`     | 如同照片的效果     |

---

## 畫質 Tag 參考

提升畫質的常用標籤：

### 通用畫質標籤
```
masterpiece, best quality, ultra-detailed, 8k
```

### 依風格選用

| 適用風格   | 建議標籤                                     |
|--------|------------------------------------------|
| 一般動漫   | `masterpiece, best quality`              |
| 精緻細節   | `ultra-detailed, extremely detailed`     |
| 寫實風格   | `photorealistic, extremely detailed, 8k` |
| 3D 建模風 | `unreal engine rendered, 3D rendered`    |

💡 **小提醒**：品質標籤不是越多越好，通常 2~3 個就夠了。過多可能反而讓畫面過度銳化。

---

## Negative Prompt 基礎

Negative prompt（負面提示詞）用來告訴 AI「不要畫什麼」。

### 常用負面提示詞
```
lowres, bad anatomy, bad hands, text, error,
missing fingers, extra digit, fewer digits,
cropped, worst quality, low quality,
normal quality, jpeg artifacts, signature,
watermark, username, blurry
```

### 畫男生時必加
```
1girl, female, breasts
```

### 畫風景時必加
```
1girl, 1boy, person, human, figure, character
```

更多細節請參考各主題的專門章節。

---

## 快速入門範例

### 範例 1：基本男性角色

Positive:
```
1boy, solo, male focus,
short hair, black hair, blue eyes, smile,
upper body, looking at viewer,
simple background,
masterpiece, best quality
```

Negative:
```
1girl, female, breasts, lowres, bad anatomy
```

### 範例 2：風景圖

Positive:
```
scenery, no humans,
mountain, lake, forest, sunrise,
landscape, nature,
masterpiece, best quality
```

Negative:
```
1girl, 1boy, person, human, figure, character
```

---

## 下一步

掌握這些基礎後，可以根據你想畫的內容，參考對應的章節：

- 想畫男生 → 畫男性角色
- 想畫風景/物件 → 純風景/純物件
- 想查 Tag 怎麼寫 → Tag 中英對照
