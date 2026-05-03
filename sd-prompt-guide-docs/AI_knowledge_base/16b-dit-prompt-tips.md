# DiT 模型 Prompt 撰寫指南

PixAI 推出的 Tsubaki / Serin / Tsubaki Flash 等 DiT 模型，提示詞寫法跟 SDXL 系列差很多。本章針對「會用 SDXL、剛接觸 DiT」的使用者，整理一套寫 prompt 的基礎 SOP。

---

## 核心原則

DiT 模型 **只接受英文 prompt**，並且強烈建議用**自然英文**描述——越像跟一位專業畫家說故事，效果越好。

**為什麼不用 Danbooru tag？**

* SDXL 系列（Illustrious、NoobAI 等）的 text encoder 是 CLIP，CLIP 訓練時看到的就是 Danbooru / e621 的 tag 描述，所以吃 tag 寫法。
* DiT 模型用的是更接近 LLM 的 text encoder，理解自然語言敘述的能力強很多，反而對純 tag 串列適應沒那麼好。
* 結果：在 SDXL 必須查資料庫的限制（`young man` 不存在、要用 `1boy`），到 DiT 都不再是限制，可以放心用一般英文寫作的方式描述。

---

## 實證對比：模型 × prompt 風格

同一個 prompt 餵到不同模型、效果差很多。以下用 [PixAI 看板娘 Mio 的 LoRA](https://pixai.art/zh/model/2003569134213267874/2003619928619895094?utm_source=eap_blog)（DiT 版 + SDXL 版同一角色、Spring Echoes 翠色版本）做嚴格對照——**同主題、同場景、只換模型 / prompt 風格**：

|  | 自然語言 prompt | Tag 堆疊 prompt |
| --- | --- | --- |
| **Tsubaki.2 (DiT)** | [A: Tsubaki.2 + 自然語言](https://pixai.art/artwork/2007632257497851383?utm_source=eap_blog)   A：模型擅長 + prompt 適配 ✓ | [B: Tsubaki.2 + Tag 堆疊](https://pixai.art/artwork/2007632821115072747?utm_source=eap_blog)   B：DiT 對 tag 風格適應較弱 |
| **Illustrious-XL (SDXL)** | [C: Illustrious-XL + 自然語言](https://pixai.art/artwork/2007632700776527473?utm_source=eap_blog)   C：SDXL 對自然語言適應較弱 | [D: Illustrious-XL + Tag 堆疊](https://pixai.art/artwork/2007632410572594057?utm_source=eap_blog)   D：模型擅長 + prompt 適配 ✓ |

對角線（A、D）兩個都是「模型 + prompt 風格」匹配的組合、效果最自然；另一條對角線（B、C）則出現意外效果——不適當的配對會讓即使是同一個 LoRA、同一個場景主題、結果也跑掉。

---

## SDXL → DiT 遷移常見踩坑

從 SDXL 跳到 DiT 時，這些習慣要丟掉：

| ❌ SDXL 慣性寫法 | 在 DiT 為什麼不行 / 該改成 |
| --- | --- |
| `1boy, solo, masterpiece, best quality` | DiT 不靠品質 tag 提升畫質；改用自然句「A young man standing alone in a cinematic scene」 |
| 大量品質 tag（`8k, ultra-detailed, extremely detailed`） | DiT 模型本身畫質就穩、疊品質 tag 可能會跟預期效果不一致（不一定稀釋、也可能用力過猛）。最多放 1 個風格詞 |
| 底線串接（`black_hair`、`looking_at_viewer`） | DiT 直接看自然英文，不必處理底線 |
| 括號權重 `(black hair:1.2)` | DiT 不認這種權重語法；想強調某元素，重新組句、把它放前面 |
| `right: ... left: ...` 區塊或 `BREAK` 隔離多人 | 在 DiT 上仍有用、但效果不特別突出；改用自然語言敘述關係、整體畫面通常更生動（見後方多人圖段） |
| 角色 LoRA trigger 補丁式放最前（`tsunu, 1boy, ...`） | DiT 上建議改成把 trigger 嵌入敘述（如 `A young man named tsunu...`）；詳見後方 LoRA 段 |

---

## 生成參數差異

除了 prompt 寫法、DiT 模型（如 Tsubaki.2）的參數面板跟 SDXL 也不一樣：

* **CFG Scale 與步數設定不存在**——SDXL 上常調的這兩個參數、在 DiT 介面根本沒有。
* **改用「模式」(Mode) 控制品質 vs 速度**：選項是 `輕量 / 標準 / 專業 / 極致`（英文：`Lite / Standard / Pro / Ultra`），原理近似 SDXL 的「步數」——越高越精緻、也越花點數。
* 預設「標準」品質就很好；要極致細節時再用「專業」。

模式選單介面

---

## 情境 1：單人圖

**推薦撰寫順序**：

| 順序 | 內容 | 為什麼這樣排 |
| --- | --- | --- |
| 1 | 畫風 / 整體氛圍 / 鏡頭語言 | 先給模型整體基調，後面所有元素都會 align 這個基調 |
| 2 | 主角 + 動作 / 姿態 | 接著讓畫面焦點清楚 |
| 3 | 服裝與配件 | 角色定位後再描述細節 |
| 4 | 前景道具 | 補足視覺重點 |
| 5 | 背景環境 | 從前景到後景、由近到遠 |
| 6 | 光影與特效 | 最後一層收尾、定氛圍 |

**範例**：

```
A cinematic medium shot of a young Taiwanese girl with long silver hair and purple eyes, gently smiling, wearing an elegant white lolita dress with intricate lace, standing in a cherry blossom garden, soft pink petals floating in the air, warm golden hour sunlight filtering through the trees, highly detailed, beautiful anime style
```

> 💡 注意這裡寫了 `young Taiwanese girl`——這在 SDXL 是不存在的 tag、會被 CLIP 誤解，但在 DiT 是合法的自然描述。**DiT 不需要查 Danbooru 資料庫**。

---

## 情境 2：多人圖

DiT 對多人圖最大的不同——**不是用標籤隔離，而是用敘述關係**。

**推薦撰寫順序**：

| 順序 | 內容 | 為什麼這樣排 |
| --- | --- | --- |
| 1 | 整體構圖 / 鏡頭 / 氛圍 | 同單人圖、先設定基調 |
| 2 | **人物之間的關係與互動**（最重要！） | DiT 靠這層理解誰是誰、誰在跟誰互動 |
| 3 | 各角色的外觀、動作、表情(從主要到次要) | 一個一個介紹、依重要性排序 |
| 4 | 服裝與細節 | 角色介紹完再補細節 |
| 5 | 背景、光影、特效 | 同單人圖最後收尾 |

**範例**：

```
A romantic wide shot under cherry blossoms at sunset, a silver-haired catgirl with purple eyes is tiptoeing to kiss a tall black-haired boy, the boy gently holding her waist, they are looking at each other affectionately, detailed intricate clothing, soft pink petals floating around them, warm golden sunlight, cinematic lighting, emotional atmosphere, beautiful detailed anime style
```

> ⚠️ **不要套 SDXL 多人圖的隔離技巧**——`right: ... left: ...`、`BREAK`、重複 tag 等手法在 DiT 通常無效或反效果。改用「她正踮腳吻他、他輕輕扶著她的腰」這樣的敘述關係。

---

## 通用小提醒

### LoRA 觸發詞嵌入方式（建議寫法、未充分驗證）

社群一般**推測**：把 LoRA trigger 寫成敘述的一部分、**有可能**比 tag 式 prefix 穩定——理由是這樣寫讓模型更清楚 trigger 跟敘述中描述對象的對應關係。但目前還沒有充分驗證、不同 LoRA / 場景的實際效果可能不同、建議兩種都試試看。

值得一提：**部分 PixAI 官方 DiT 系 LoRA（例如看板娘 Mio LoRA）的 trigger 直接設計成一整段角色描述**、本來就要融進敘述使用。例如 [[PixAI Mio/ミオ] Spring Echoes LoRA](https://pixai.art/zh/model/2003569134213267874/2003696017189397264?utm_source=eap_blog) 的觸發詞：

```
A girl with white-to-pink gradient hair, heart ahoge, purple eyes, eyepatch, cat ears, fang, jirai kei style. Open dark grey glossy leather hoodie over a black bandeau, slight cleavage, cinched waist, pink drawstrings. Black distressed low-rise denim short
```

把這段直接接續場景動作、比另起一行當 prefix 更自然：

| 寫法 | 範例 |
| --- | --- |
| 整段 trigger 塞最前、再接場景 | `<觸發詞整段>. She is walking through neon-lit Shibuya at night.` |
| 自然合一(推薦) | `A girl with white-to-pink gradient hair, heart ahoge, purple eyes, eyepatch, cat ears, fang, jirai kei style, walking through neon-lit Shibuya at night, ...` |

實在無法自然嵌入時、再單獨放最前或最後一句。

### 負面提示詞（共用版）

```
blurry, low quality, deformed hands, extra fingers, bad anatomy, watermark, text, logo, ugly, deformed, mutated
```

DiT 跟 SDXL 一樣吃負面提示詞、這條基礎清單兩邊通用。

### 風格描述優先放 Customize Style

> ⚠️ **Customize Style 是 Tsubaki.2 模型獨有的欄位**——其他 DiT 模型（Tsubaki v1、Serin、Tsubaki Flash）沒有這個欄位。在 Tsubaki.2 上把風格詞拆到 Customize Style 可以讓主 prompt 更乾淨；其他 DiT 模型請直接整合進主 prompt 末尾。

#### Customize Style 範例

| 場景 | Customize Style 內容 |
| --- | --- |
| 單人立繪 | `delicate anime style, soft lighting, studio ghibli influence` |
| 多人浪漫 | `romantic anime style, cinematic, soft bokeh` |
