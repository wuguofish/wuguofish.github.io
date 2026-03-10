# 女性向友善模型推薦

## 核心觀念

> 沒有算不出美少年的 Model，只有不懂 Model 個性的使用者。

每個模型都有自己的「個性」——擅長的風格、預設的畫風、對特定 tag 的反應。選對模型，事半功倍。

---

## 推薦模型清單

以下模型皆可在 PixAI 上使用，且經女性向社群實測對男性角色表現良好。

### 1\. Plant Milk

**連結**：https://pixai.art/zh/model/1840638240479764095?utm_source=eap_blog

**特色**：

- 內建 8 個版本，對應不同畫風
- 出來的人物都偏美型
- 適合各種風格嘗試

**適合場景**：想要嘗試不同畫風、需要美型角色

---

### 2\. Aüngir

**連結**：https://pixai.art/zh/model/1825099018174912691?utm_source=eap_blog

**特色**：

- 動漫風首選
- 光影處理漂亮
- 男性角色偏陽剛帥氣，但不會老氣

**適合場景**：想要帥氣系男角、重視光影效果

**小提醒**：畫美型少年可能需要額外加 `bishounen` 等詞調整

---

### 3\. One obsession

**連結**：https://pixai.art/zh/model/1875126058825562303?utm_source=eap_blog

**特色**：

- 容易做出言情小說封面的粉彩風格
- 色調柔和浪漫

**適合場景**：乙女向、言情風、浪漫氛圍

---

### 4\. coco-Illustrious-NoobXL-Style

**連結**：https://pixai.art/zh/model/1819625090188724117?utm_source=eap_blog

**特色**：

- 中規中矩，畫什麼都不會太差
- 泛用性高

**適合場景**：新手入門、不確定要什麼風格時的安全選擇

---

### 5\. Nova Orange XL v10.0

**連結**：https://pixai.art/zh/model/1882805156367629767?utm_source=eap_blog

**特色**：

- 日系偏寫實動漫風格
- 人物偏美型
- 場景偏日式

**適合場景**：想要日系風格、校園/日常場景

---

### 6\. Diving-Illustrious Anime

**暗色系版本**：https://pixai.art/zh/model/1890273426555336148?utm_source=eap_blog
**亮色系版本**：https://pixai.art/zh/model/1932440954135769967?utm_source=eap_blog

**特色**：

- 可做出類似 Niji（MidJourney 動漫模式）的風格
- 兩個版本分別對應暗色系和亮色系畫風

**適合場景**：喜歡 Niji 風格、想要高品質動漫插畫感

---

## 模型選擇快速指南

| 我想要的風格     | 推薦模型                          |
|------------|-------------------------------|
| 不知道選什麼，先求穩 | coco-Illustrious-NoobXL-Style |
| 帥氣陽剛男角     | Aüngir                        |
| 美型少年       | Plant Milk                    |
| 言情小說封面     | One obsession                 |
| 日系校園風      | Nova Orange XL                |
| 類 Niji 高品質 | Diving-Illustrious Anime      |
| 陰鬱病嬌系      | Vete ┃ Dreamhex ILL（進階）       |
| LoRA 控制精準  | ChocoMint Mix（進階）             |

---

## 進階模型

以下模型功能強大，但需要一定經驗才能駕馭。

### 7\. Vete ┃ Dreamhex ILL

**連結**：https://pixai.art/zh/model/1958202009206907933?utm_source=eap_blog

**特色**：

- 陰鬱系美少年首選
- 適合病嬌、暗黑、頹廢風格

**注意事項**：

- 容易有眼睛破圖的問題
- 需要從 prompt 或 LoRA 補救
- **適合玩一陣子的高手**

**適合場景**：陰鬱系、病嬌風、暗黑美學

---

### 8\. ChocoMint Mix

**連結**：https://pixai.art/zh/model/1874095126418918009?utm_source=eap_blog

**特色**：

- 對 LoRA 反應非常良好
- 偏寫實的動漫風格
- 對畫風提示詞很敏感，可塑性高

**注意事項**：

- ⚠️ **不適合新手**：預設容易跑出萌妹子
- 需要明確的男性特徵描述 + 完整的 negative prompt
- 適合已經熟悉 prompt 調整的使用者

**適合場景**：想要精準控制 LoRA 效果、需要多變畫風的進階玩家

---

## 通用建議

1. **先用預設設定試跑**：了解模型的「原廠風格」
2. **記錄有效的 prompt**：每個模型對同樣的詞反應不同，找到適合的組合要記下來
3. **搭配 LoRA 微調**：模型決定大方向，LoRA 調整細節
4. **多生幾張挑選**：AI 有隨機性，同樣的 prompt 多跑幾次結果會不同


---

# 推薦 DiT 模型

> 📖 本頁的 DiT 模型資訊引用自 [**PixAI 官方部落格**](<https://pixai.art/articles/zh/otome-special-mastering-bl-yaoi-art-in-pixai-2/?utm_source=eap_blog>)，經官方授權引用。
>
> **👉[在PixAI上使用基於DiT架構的模型](<https://pixai.art/en/market#type=DIT7_MODEL?utm_source=eap_blog>)**

## 什麼是 DiT？

DiT（Diffusion Transformer）是新一代的圖像生成架構，與傳統 SDXL（基於 U-Net）相比，DiT 在以下方面有明顯優勢：

- **多角色構圖更穩定**：角色特徵不容易混在一起
- **支援自然語言**：大部分 DiT 模型可以用更接近自然語言的方式撰寫提示詞
- **整體品質提升**：面部、服裝、背景的細節渲染更精煉

---

## 推薦模型清單

| 模型                                                                | 特色                           |
|-------------------------------------------------------------------|------------------------------|
| [Tsubaki](<https://pixai.art/zh/model/1884107375027888751?utm_source=eap_blog>)       | 支援自然語言提示詞，多角色生成品質高（間距、互動、平衡） |
| [Tsubaki v1.1](<https://pixai.art/zh/model/1935090614966005945?utm_source=eap_blog>)  | 強化版，更精煉的面部、服裝與背景渲染           |
| [Tsubaki Flash](<https://pixai.art/zh/model/1934789863877919615?utm_source=eap_blog>) | 官方高速版本，大幅縮短生成時間，極高的 LoRA 相容性 |
| [Serin](<https://pixai.art/zh/model/1911477338694141481?utm_source=eap_blog>)         | 正統韓系藝術風格，視覺震撼的角色設計           |

---

## 注意事項

- DiT 模型的提示詞語法可能與 SDXL 不同（例如 `right:` / `left:` 區塊語法不一定適用），使用時請參考各模型的說明。
- DiT 模型目前在 PixAI 上的 LoRA 生態仍在發展中，可用的 LoRA 數量可能不如 SDXL 豐富。
