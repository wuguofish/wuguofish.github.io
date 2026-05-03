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
