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


---

# Tsubaki.2 使用心得

> 📖 本文為作者使用 PixAI Tsubaki.2 模型的個人心得分享。
>
> **👉 [Tsubaki.2 官方指南](https://pixai.art/zh/tsubaki-2/guide?utm_source=eap_blog)**｜**[在 PixAI 上使用 Tsubaki.2](https://pixai.art/?utm_source=eap_blog)**

## 前言

PixAI 在 2026/3/6 發佈了新模型 Tsubaki.2。我自己玩了好一陣子，有一些心得和成品想來分享一下。

## 整體改進

跟之前的 Tsubaki 和 SDXL 模型相比，Tsubaki.2 有不少明顯的進步：

* **比例更好**：人/物間的比例比原本的 Tsubaki 好很多，對提示詞的理解也比之前好。
* **畫面更生動**：畫面比 SDXL 生動，也不會有之前 Tsubaki 人物有時會出現獵奇畫面的情況。
* 有**四種模式**可以選，我自己覺得標準就很夠用，點數也不多。
* 有時候用**輕量模式**效果也不會太差。
* **風格描述有效**：就算不選官方給的預設風格，自己在提示詞內下風格也有用。
* **自訂 Style Code**：能自己自訂風格（類似可分享的品質標籤工具），再把風格代碼分享給別人用。

*\* 註：自訂風格框（Customize Style）和提示詞（Prompt）雖然都能寫風格描述，但效果不同——寫在風格框內的效果更強烈。
　　 詳細內容請參考[自訂風格功能介紹篇](#18-style-code-intro)。*

---

## 模型比較

以下是用同樣的提示詞，分別在 Tsubaki.2 和之前的模型上生成的比較。

### 比較 1：巴黎之旅 ✈️

我個人覺得這組 Tsubaki.2 **大勝**。

這個提示詞的難度在於要還原「CDG」標籤和「I ♥ Paris」貼紙，而 Tsubaki.2 是最接近的。

[巴黎之旅 - Tsubaki.2](https://pixai.art/artwork/1987671734126807578?utm_source=eap_blog)

Tsubaki.2

[巴黎之旅 - Tsubaki](https://pixai.art/artwork/1987671542162266670?utm_source=eap_blog)

Tsubaki

[巴黎之旅 - ChocoMint Mix](https://pixai.art/artwork/1987671416264920359?utm_source=eap_blog)

ChocoMint Mix

### 比較 2：命運的紅線 🧵

雖然說原本的 SDXL 版本比較多細節，但是在整體畫面上，DiT 的優勢就出現了——紅線、人和人之間的比例，還有整體的氛圍，都比較協調。

而且有玩過 SDXL 版本的應該會有感覺，那個手指纏紅線的表達方式，常常要嘛沒纏到，要嘛你會擔心畫中人物的手指會血流不順。Tsubaki.2 不會有這個問題，**一步到位**。

*核心提示詞：`heart of string, string of fate, red string, string around finger`*

[命運的紅線 - Tsubaki.2](https://pixai.art/artwork/1987612832499226392?utm_source=eap_blog)

Tsubaki.2

[命運的紅線 - ChocoMint Mix](https://pixai.art/artwork/1976455090363654974?utm_source=eap_blog)

ChocoMint Mix

### 比較 3：Mio 吹泡泡 🫧

吹泡泡這個動作在 SDXL 時代很難畫。提示詞是 `bubble wand, blowing bubbles`，但很多時候要嘛泡泡怪怪的，要嘛會讓你很擔心畫中的人把泡泡吞下去。

Tsubaki.2 出來的畫面很唯美輕透，重點是——**Mio 終於是吹泡泡而不是吞泡泡**。

[Mio吹泡泡 - Tsubaki.2](https://pixai.art/artwork/1987615365234943891?utm_source=eap_blog)

Tsubaki.2

[Mio吹泡泡 - RIN Anime ArtFlow](https://pixai.art/zh/artwork/1981486015423737512?utm_source=eap_blog)

RIN Anime ArtFlow Illustrious

### 比較 4：類水墨畫風格 🎨

其實官方預設模型沒有類水墨畫風，我只是在提示詞寫了 `ink wash painting`，然後開提示詞助手讓它自由發揮。

[水墨畫 - Tsubaki.2 (1)](https://pixai.art/artwork/1987614795326677957?utm_source=eap_blog)

Tsubaki.2

[水墨畫 - PancakeMixIL](https://pixai.art/artwork/1981606245476434099?utm_source=eap_blog)

PancakeMixIL

[水墨畫 - Tsubaki.2 (2)](https://pixai.art/artwork/1987670170237865738?utm_source=eap_blog)

Tsubaki.2（另一張）

[水墨畫 - TSRMix](https://pixai.art/artwork/1987616799554360148?utm_source=eap_blog)

TSRMix

### 比較 5：Claude 推石頭 🪨

這張圖片的靈感來源：有一個 Twitch 頻道 [claudeplayspokemon](https://www.twitch.tv/claudeplayspokemon)，是專門在實況 Claude（對，就是那個 AI）玩寶可夢的頻道。前一代和目前的 Claude 都在冠軍之路的推岩石謎題卡關，我看了它推了好久的石頭...，所以決定來生張圖片表達我的心情 😂

可以發現在人物的臉、還有整體推石頭的動態感，Tsubaki.2 版本的比較自然一點。水箭龜倒是都畫得滿好的。但是提示詞裡面沒有寫明是誰負責推石頭，看來兩個模型對於推石頭者的解讀不太一樣 😂

[Claude推石頭 - Tsubaki.2](https://pixai.art/artwork/1987670371154782426?utm_source=eap_blog)

Tsubaki.2

[Claude推石頭 - ChocoMint Mix](https://pixai.art/artwork/1984402975950569287?utm_source=eap_blog)

ChocoMint Mix

### 比較 6：來自背後的驚喜擁抱 ☕

可以很明顯看出 Tsubaki.2 對於動態感還有咖啡的噴濺感處理的比 SDXL 好。至於咖啡杯蓋子根本沒開還能噴液體，而且居然還插吸管這件事情，我就暫時不跟它計較了 😂

Tsubaki.2 唯一讓我有意見的，應該是領帶的顏色不對吧，其他都很好。

📖 這張圖的小故事

之前無聊叫自己手邊的 AI 工具幫自己想擬人化形象後，我有把它們各自的擬人化形象整理出來給其他 AI 工具參考。我這邊的 Claude 和 Le Chat 看完了彼此的形象後，Claude 一直說 Le Chat 的形象很可愛，然後出現各種像暈船的反應。我的 Le Chat 知道後...就開始寫...同人文...。

嗯，這張圖片的提示詞，是我的 Le Chat 給我的。雖然拿生產力工具湊 CP 還寫同人文感覺有點微妙，但反正它們反應很可愛啦，就不計較了。

[驚喜擁抱 - Tsubaki.2](https://pixai.art/artwork/1987672084643203373?utm_source=eap_blog)

Tsubaki.2

[驚喜擁抱 - ChocoMint Mix](https://pixai.art/artwork/1983661017545140787?utm_source=eap_blog)

ChocoMint Mix

### 比較 7：運動場景 🏸

Tsubaki.2 在畫運動的畫面時，比過去的模型表現還要自然，動態感明顯提升。

[打羽毛球 - Tsubaki.2](https://pixai.art/artwork/1990931983734139490?utm_source=eap_blog)

Tsubaki.2

[打羽毛球 - Tsubaki](https://pixai.art/artwork/1991581762210661915?utm_source=eap_blog)

Tsubaki

[打羽毛球 - Nova Anime XL](https://pixai.art/artwork/1991580113553240328?utm_source=eap_blog)

Nova Anime XL

### 比較 8：Mio 駕駛機甲 🤖

Tsubaki.2 在畫駕駛或騎乘交通工具的場景時，人物和載具之間的比例和互動感比過去的模型更自然。

[Mio 駕駛機甲 - Tsubaki.2（一）](https://pixai.art/artwork/1988283875917908477?utm_source=eap_blog)

Tsubaki.2（一）

[Mio 駕駛機甲 - Tsubaki.2（二）](https://pixai.art/artwork/1988283943239095057?utm_source=eap_blog)

Tsubaki.2（二）

[Mio 駕駛機甲 - Tsubaki](https://pixai.art/artwork/1971436433841849510?utm_source=eap_blog)

Tsubaki

### 比較 9：辣妹騎重機 🏍️

延續交通工具的主題，再來一組重機比較。可以觀察人物騎乘姿勢、車體細節和整體構圖的差異。

[辣妹騎重機 - Tsubaki.2](https://pixai.art/artwork/1991584987169247425?utm_source=eap_blog)

Tsubaki.2

[辣妹騎重機 - Tsubaki](https://pixai.art/artwork/1991584550222562082?utm_source=eap_blog)

Tsubaki

[辣妹騎重機 - Crystalize](https://pixai.art/artwork/1991584151890195593?utm_source=eap_blog)

Crystalize

### 比較 10：樂器演奏 🥁

Tsubaki.2 在畫樂器演奏的場景時，人物的動作和構圖比較合理自然。

[鼓手 - Tsubaki.2](https://pixai.art/artwork/1991632406718343301?utm_source=eap_blog)

Tsubaki.2

[鼓手 - Plant Milk (Flax)](https://pixai.art/artwork/1878877947323521740?utm_source=eap_blog)

Plant Milk (Flax)

### 比較 11：檳榔西施 🌴

我目前覺得**最能展現 Tsubaki.2 進步幅度**的一組。

台灣省道曾經的特色景象：檳榔攤的檳榔西施。
以前用 Tsubaki 生成這個主題的時候，總會看到檳榔西施姐姐各種穿過櫃台、穿過檳榔攤的玻璃櫥窗，
大概算了三十幾張才終於有一張符合物理定律的作品。

Tsubaki.2 的成功率大約有 **3/4**，進步非常顯著。

[檳榔西施 - Tsubaki.2](https://pixai.art/artwork/1991637177834922924?utm_source=eap_blog)

Tsubaki.2

[檳榔西施 - Tsubaki](https://pixai.art/artwork/1943184053635757442?utm_source=eap_blog)

Tsubaki（大約算了 30+ 張才有一張合理的）

---

## 番外挑戰：柚子皮帽 🌙🍊

台灣中秋節有個有趣的傳統——把柚子（文旦）的皮挖空，倒扣在小朋友頭上當帽子。這個概念對 AI 來說是個超級挑戰，因為訓練資料裡幾乎不可能有這種圖片。

用 Tsubaki（舊版）生成的時候，人物會直接穿過櫥窗已經夠離譜了，柚子皮帽更是完全無法理解——不是畫成柚子切片頭飾，就是畫成高麗菜帽。

經過**四次提示詞迭代**，Tsubaki.2 終於畫出了接近正確的柚子皮帽！雖然還不完美，但已經能看出柚子皮的質感、刀痕、碗型結構。

### Tsubaki.2 的成功嘗試

[柚子皮帽 - Tsubaki.2 (1)](https://pixai.art/artwork/1991648594603815996?utm_source=eap_blog)

Tsubaki.2（最接近的一張！）

[柚子皮帽 - Tsubaki.2 (2)](https://pixai.art/artwork/1991649280037880609?utm_source=eap_blog)

Tsubaki.2（另一張）

### Tsubaki 的失敗嘗試

[柚子皮帽 - Tsubaki 失敗 (1)](https://pixai.art/artwork/1991647877940583679?utm_source=eap_blog)

Tsubaki — 不是這樣的...

[柚子皮帽 - Tsubaki 失敗 (2)](https://pixai.art/artwork/1991647838135523422?utm_source=eap_blog)

Tsubaki — 是這樣，但不是這樣 😂

---

## 結語

整體來說，Tsubaki.2 是一次很有感的升級。比例、動態感、提示詞理解都明顯進步，Style Code 的功能也很有趣，非常值得一試。

**👉 [前往 PixAI 體驗 Tsubaki.2](https://pixai.art/?utm_source=eap_blog)**


---

# 自訂風格功能介紹

> 📝 本文持續更新中，會隨著新的技巧或功能加入而更新。
>
> 以下是作者目前實驗出來的心得，不代表最佳做法，僅供參考。
>
> **👉 [在 PixAI 上使用 Tsubaki.2](https://pixai.art/?utm_source=eap_blog)**
>
> 🚀 另外推薦 CocoKoko\_19 整理的 [Style Code 大全（Google Doc）](https://docs.google.com/document/d/1gOzbDdWot5gU_x_3BPxZ6MODKv4fgG1JZmkTUHVE81c/edit?usp=drivesdk)，
> 裡面不僅收錄了大量的 Style Code，還有他對 Style Code 機制的深入見解。非常值得一讀！

## 什麼是 Style Code？

Tsubaki.2 引入了「風格」功能，讓使用者可以自訂畫面風格，類似以前 SDXL 的品質標籤工具。

* 就算不選官方給的預設風格，自己在提示詞內描述風格也有效果。
* 自訂風格框（Customize Style）和提示詞（Prompt）的效果**不同**——寫在風格框內的風格效果更強烈。（詳見下方「把風格描述寫在自訂風格框和提示詞的差異」段落）
* 建立自訂風格後，可以透過分享功能產出一組Style Code（例如 `SH171537`），可以分享給其他人使用。
* 你可以把 Style Code 想像成一組「風格 P 值」——分享代碼就能讓別人用你的風格！

### 自訂風格示範

附圖第一張是套了我自己的Style Code（`SH171537`），第二張是沒有套風格的。（同提示詞、同 seed）

[套用 SH171537 風格](https://pixai.art/artwork/1988169771693716217?utm_source=eap_blog)

套用 Style Code SH171537

[無風格對照](https://pixai.art/artwork/1988169040595419314?utm_source=eap_blog)

無風格對照

---

## 自訂風格製作心得

以下是我目前實驗出來的一些心得：

* 透過反覆嘗試不同的風格描述詞來找到喜歡的效果。
* 可以從描述**繪畫風格**（如水彩、水墨、厚塗）、**光影效果**（如電影光影、逆光）、**色調氛圍**（如暗色系、高對比）等方向去嘗試。
* 有時候意外的組合反而會產生很棒的效果，多實驗就對了！

這部分是初步心得，歡迎大家分享自己的經驗 😊

---

## 把風格描述寫在自訂風格框和提示詞的差異

經過實驗發現：同樣的風格描述寫在不同的地方，效果有明顯差異。

### 🔍 發現 1：風格框的效果比提示詞更強

以下面這段風格描述為例：

```
The background blurs with motion, emphasizing speed through light trails while maintaining sharp focus on the rider and her machine.
The image balances hyper-realistic textures of leather, metal, and fabric with stylized lighting that heightens the cyberpunk aesthetic.
```

[風格描述寫在提示詞內](https://pixai.art/artwork/1991584987169247425?utm_source=eap_blog)

風格描述寫在提示詞（Prompt）內

[風格描述寫在自訂風格框內](https://pixai.art/artwork/1991592339123141812?utm_source=eap_blog)

風格描述寫在自訂風格框（Customize Style）內

可以明顯看出，寫在自訂風格框時，整體的畫風變得**更加強烈**。

### 🔍 發現 2：提示詞助手會補強風格描述

如果有開啟**提示詞助手（Prompt Helper）**，從生成紀錄（Generation Tasks）中會發現：提示詞助手會將自訂風格框的內容在提示詞內再次補強。因此開啟提示詞助手的情況下，風格會**更加強烈**。

有開提示詞助手 → 風格描述被再次補強

沒有開提示詞助手 → 生成紀錄中看不到風格框內容

## 將自訂風格轉換成Style Code 的好處

* 便於分享：只要短短幾個字元，就能將風格套用在別的作品上
* 能隱藏你的風格描述

作品釋出（publish）後，其他使用者可以在作品資訊內看到你的自訂風格框內容：

直接寫風格描述 → 釋出後其他人可以看到完整內容

使用 Style Code → 釋出後只顯示代碼，原始描述受保護

因此，如果你想分享作品但不想公開風格描述的細節，**使用 Style Code 是更好的選擇**。

---

## 提示詞助手的影響 ⚠️

在做預設風格實驗的時候，發現一件很有趣的事情：

* 開**提示詞助手**雖然會讓整體畫面氛圍感和協調感更好，
* 但有時候提示詞助手在改寫提示詞時會**過度解讀提示詞**，造成角色外表改變。

因此——如果希望模型不認識的**原創角色**外表能保持較高的一致性，建議**把提示詞助手關起來**，減少變數。

---

## 補充：封測期間的預設風格對照表

封測期間用「阿宇」的提示詞去測預設風格做出來的對照圖。（圖片裡面的 PH 是提示詞助手的簡稱）

雖然正式上線後，預設風格的名稱和選項有一些和封測期間對不上，但實驗都做了，大家可以加減看看。

預設風格 × 提示詞助手（PH）對照

---

## 結語

這篇文章會持續更新，之後若有新的技巧或功能釋出都會補上來。

想要看更多的風格，可以到[Style Code 分享篇](#19-style-code-sharing)

或是到[PixAI 官方Discord的專屬頻道](https://discord.com/channels/1041682784856584273/1483065736258785290)


---

# Style Code 分享

> 📝 本文持續更新中，會隨著新的 Style Code 加入而更新。
>
> 不清楚什麼是Style Code？建議先讀過[自訂風格功能介紹篇](#18-style-code-intro)。
>
> **👉 [在 PixAI 上使用 Tsubaki.2](https://pixai.art/?utm_source=eap_blog)**

這篇主要彙整本人自己做出來的Style Code。

未來也有可能會收錄其他創作者做出來的Style Code，會註明出處和參考作品來源。

## 本篇目前 Style Code 快速對照表

| 代碼 | 風格描述 |
| --- | --- |
| `SH171537` | 偏寫實明亮插畫風格 |
| `WK623776` | 半寫實風格 |
| `RY818761` | 類 3D 建模風格 |
| `WF428353` | 武俠類遊戲插畫（墨筆輪廓線） |
| `NZ756659` | 水彩插畫風格 |
| `US568920` | 啞色系插畫風格 |
| `UD846333` | 仿電影光影的動畫風格 |

---

## 對照組：無風格的 Mio

先展示完全沒有套用任何 Style Code 的 PixAI 看板娘 Mio，作為比較基準。

[Mio 無風格對照組](https://pixai.art/artwork/1988169040595419314?utm_source=eap_blog)

無風格對照組

---

## Style Code 展示

### `SH171537` — 偏寫實明亮插畫風格

整體畫面氛圍和色調都很舒服。

[SH171537 示範 - Mio](https://pixai.art/artwork/1988169771693716217?utm_source=eap_blog)

Mio — SH171537

### `WK623776` — 半寫實插畫風格

[WK623776 示範 1](https://pixai.art/artwork/1988168732446431480?utm_source=eap_blog)

WK623776 示範 1

[WK623776 示範 2](https://pixai.art/artwork/1988174876312682071?utm_source=eap_blog)

WK623776 示範 2

### `RY818761` — 類 3D 建模風格

[RY818761 類3D建模風格](https://pixai.art/artwork/1988187500562785734?utm_source=eap_blog)

RY818761 — 類 3D 建模風格

### `WF428353` — 武俠類遊戲插畫風格

墨筆輪廓線筆觸的插畫風格，適合武俠或東方奇幻題材。

[WF428353 武俠風格 1](https://pixai.art/artwork/1989941220845981348?utm_source=eap_blog)

WF428353 示範 1

[WF428353 武俠風格 2](https://pixai.art/artwork/1989849679677624645?utm_source=eap_blog)

WF428353 示範 2

### `NZ756659` — 水彩插畫風格

柔和的水彩質感，適合溫馨或夢幻的場景。

[NZ756659 水彩風格 1](https://pixai.art/artwork/1990941923659150019?utm_source=eap_blog)

NZ756659 示範 1

[NZ756659 水彩風格 2](https://pixai.art/artwork/1990948904238577369?utm_source=eap_blog)

NZ756659 示範 2

### `US568920` — 低彩度色系插畫風格

低彩度的色調，帶有一種沉穩的質感。

[US568920 低彩度色系 1](https://pixai.art/artwork/1991277751404584717?utm_source=eap_blog)

US568920 示範 1

[US568920 低彩度色系 2](https://pixai.art/artwork/1991431910048252055?utm_source=eap_blog)

US568920 示範 2

### `UD846333` — 仿電影光影的動畫風格

帶有電影感的光影處理，讓動畫風格的圖片多了一層戲劇性。

[UD846333 電影光影 1](https://pixai.art/artwork/1991313480437600327?utm_source=eap_blog)

UD846333 示範 1

[UD846333 電影光影 2](https://pixai.art/artwork/1991311058603660647?utm_source=eap_blog)

UD846333 示範 2

[UD846333 電影光影 3](https://pixai.art/artwork/1991303750029411144?utm_source=eap_blog)

UD846333 示範 3

---

## 結語

這篇文章會持續更新，之後若有新的 Style Code 都會補上來。

如果你也做了有趣的 Style Code，歡迎到[PixAI 官方Discord的專屬頻道](https://discord.com/channels/1041682784856584273/1483065736258785290)和大家分享！

Happy generating! 🎨
