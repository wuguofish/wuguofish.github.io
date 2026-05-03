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
