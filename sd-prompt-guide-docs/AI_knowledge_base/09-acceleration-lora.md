# 加速 LoRA 介紹

## 什麼是加速 LoRA？

一般的圖像生成需要 20-50 步才能完成，**加速 LoRA**透過「蒸餾」能讓你用 **4-8 步**就得到差不多的結果。

### 白話解釋「蒸餾」

你可能會看到「知識蒸餾（Knowledge Distillation）」這個詞，聽起來很像化學實驗，但其實概念很簡單：

> **讓小模型「抄捷徑」學會大模型的生成技巧**

想像一下：

- **老師模型**：很厲害但跑很慢，需要 50 步才能畫出好圖
- **學生模型**：小而快的模型

傳統訓練是讓學生從零開始學（看大量原始圖片），但「蒸餾」的做法是：

> 讓學生**直接模仿老師的作答過程和答案**，而不是重新學習所有原理

就像學生不用把整本微積分課本讀完，只要老師說「遇到這種題型，答案長這樣」，學生就能用捷徑得到差不多的結果。

### 為什麼需要加速 LoRA？

- **節省時間**：快 3-10 倍
- **節省點數/算力**：步數少 = 消耗少
- **快速預覽**：構圖、配色滿意再用正常步數精修
- **批量生成**：大量出圖時效率更高

---

## 延伸閱讀

想深入了解加速 LoRA 背後的原理和技術比較，推薦閱讀這篇文章：

📖 [你還在用30步算圖？揭秘1步生成的性能奇蹟](<https://306007.xyz/zh/blog/2025_distillation_loras/>)

---

## 五種推薦的加速 LoRA

以下是在 PixAI 上推薦使用的加速 LoRA，點擊連結可直接前往使用：

### 1\. LCM（Latent Consistency Model）

🔗 **PixAI 連結**：https://pixai.art/model/1687631572599847061?utm_source=eap_blog

**原理**：將擴散模型蒸餾成「一致性模型」，讓模型學會「一步到位」生成圖像。

**特色**：

- ⭐ 最普及，社群資源最多
- 設定簡單，新手友善
- PixAI 上最常見

---

### 2\. DMD2（Distribution Matching Distillation 2）

🔗 **PixAI 連結**：https://pixai.art/zh/model/1897811443252033347?utm_source=eap_blog

**原理**：透過「分佈匹配蒸餾」，學生模型快速學會老師模型的輸出分佈。

**特色**：

- ⭐ 畫質比 LCM 更好
- 寫實風格表現特別出色
- 支援極低步數（1-4 步）

---

### 3\. PCM（Phased Consistency Model）- NormalCFG 版

🔗 **PixAI 連結**：https://pixai.art/zh/model/1810142527271081205?utm_source=eap_blog

**原理**：LCM 的改良版，將生成軌跡分段處理，減少誤差累積。

**特色**：

- ⭐ CFG 彈性最高（可用 2-9）
- 負面提示詞真的有效
- 有 NormalCFG 和 SmallCFG 兩種版本

---

### 4\. WAI-illustrious-Rectified-4Steps

🔗 **PixAI 連結**：https://pixai.art/zh/model/1857294002524835135?utm_source=eap_blog

**原理**：基於 Rectified Flow 技術，專為 Illustrious 系列模型優化的 4 步加速 LoRA。

**特色**：

- ⭐ 專為 Illustrious 系列優化
- 固定 4 步，設定簡單
- 與 Illustrious 系模型相容性最佳

---

### 5\. Hyper SDXL

🔗 **PixAI 連結**：https://pixai.art/zh/model/1783737893546128417?utm_source=eap_blog

**原理**：ByteDance 開發的 Hyper-SD 技術，結合 Trajectory Segmented Consistency Distillation（TSCD）與 Human Feedback Learning，實現極低步數生成。

💡 **小知識**：雖然名稱是「2steps-lora」，技術上確實支援 2 步生成，但 PixAI 上建議使用 8 步以獲得更穩定的畫質。

**特色**：

- ⭐ 建議 8 步，可更高
- CFG 需維持低值（1.1-2.0）
- 採樣器相容性佳（Euler a、DDIM）

---

## 建議參數表

在 PixAI 上使用這些加速 LoRA 時的推薦設定（實際設定值仍需以LoRA介紹頁的建議以及自己需求為主）：

| 項目          | LCM     | DMD2    | PCM (NormalCFG) | WAI-Rectified-4Steps | Hyper SDXL     |
|-------------|---------|---------|-----------------|----------------------|----------------|
| **建議步數**    | 3-8     | 4-8     | 4-16            | 4                    | 8+             |
| **CFG 範圍**  | 1.0-2.0 | 1.0-1.6 | 2-9             | 1.0-2.0              | 1.1-2.0        |
| **採樣器**     | LCM     | LCM     | DDIM / Euler    | Euler                | Euler a / DDIM |
| **LoRA 權重** | 1.0     | 0.7-1.0 | 1.0             | 1.0                  | 1.0            |

### PCM 版本說明

PCM 有兩種版本，差別在於 CFG 範圍：

| 版本            | CFG 範圍 | 適用情境         |
|---------------|--------|--------------|
| **NormalCFG** | 2-9    | 需要負面提示詞發揮作用時 |
| **SmallCFG**  | 1-2    | 類似 LCM 的使用方式 |

---

## 優缺點比較

### LCM

| 優點 ✓      | 缺點 ✗        |
|-----------|-------------|
| 最普及、社群資源多 | CFG 只能用 1-2 |
| 相容性好      | 負面提示詞效果差    |
| 設定簡單易上手   | 步數變化結果不一致   |

### DMD2

| 優點 ✓        | 缺點 ✗       |
|-------------|------------|
| 畫質比 LCM 更好  | 可能出現泛白/褪色  |
| 支援極低步數（1-4） | 需調整 CFG 補償 |
| 寫實風格表現佳     | 社群資源較少     |

### PCM

| 優點 ✓         | 缺點 ✗                |
|--------------|---------------------|
| CFG 彈性高（2-9） | 檔案較大                |
| 負面提示詞有效      | 需選對版本（Normal/Small） |
| 不同步數結果穩定     | 步數要匹配 LoRA 版本       |

### WAI-illustrious-Rectified-4Steps

| 優點 ✓              | 缺點 ✗               |
|-------------------|--------------------|
| 專為 Illustrious 優化 | 僅適用 Illustrious 系列 |
| 固定 4 步，設定簡單       | 步數固定，彈性較低          |
| 相容性佳              | 其他模型效果可能不佳         |

### Hyper SDXL

| 優點 ✓    | 缺點 ✗              |
|---------|-------------------|
| 採樣器相容性佳 | CFG 必須很低（1.1-2.0） |
| 設定簡單易上手 | 高 CFG 會出問題        |
| 畫質穩定    | 步數不算最少（8+）        |

---

## 快速選擇指南

| 你的需求                   | 推薦選擇                 | 理由                        |
|------------------------|----------------------|---------------------------|
| 🆕 **新手入門**             | LCM                  | 設定最簡單，CFG 1.5、步數 4-6 就能用  |
| 🎨 **追求畫質**             | DMD2                 | 4-8 步就有不錯效果，寫實風格特別出色      |
| 🚫 **需要負面提示詞**          | PCM (NormalCFG)      | 支援 CFG 2-9，負面提示詞真的有用      |
| 🎯 **用 Illustrious 模型** | WAI-Rectified-4Steps | 專為 Illustrious 系列優化，相容性最佳 |
| 🔧 **採樣器彈性**            | Hyper SDXL           | Euler a、DDIM 都能用，設定簡單     |

---

## PixAI 上的使用率參考

根據社群使用情況：

| 加速 LoRA       | 普及度   |
|---------------|-------|
| LCM           | ⭐⭐⭐⭐⭐ |
| DMD2          | ⭐⭐⭐⭐  |
| PCM           | ⭐⭐⭐   |
| WAI-Rectified | ⭐⭐⭐   |
| Hyper SDXL    | ⭐⭐⭐⭐  |

---

## 實用建議

### 1\. 先用加速 LoRA 預覽，再用正常步數精修

加速 LoRA 最適合用來快速確認構圖和配色，滿意後再關掉加速 LoRA，用 20-30 步精修細節。

### 2\. 加速 LoRA 可以和其他 LoRA 疊加

你可以同時使用：

- 加速 LoRA（如 LCM）
- 風格 LoRA
- 角色 LoRA

只要注意總權重不要太高，避免互相干擾。

### 3\. 不同加速 LoRA 不要混用

一次只用一種加速 LoRA，混用會導致結果混亂。

### 4\. 注意版本匹配

- **SDXL 模型**用 SDXL 版的加速 LoRA
- **SD 1.5 模型**用 SD 1.5 版的加速 LoRA
- **Illustrious 系列**優先考慮 WAI-Rectified-4Steps
- 版本不對會完全沒效果或出錯

---

## 快速連結總覽

| 加速 LoRA              | PixAI 連結                                       |
|----------------------|------------------------------------------------|
| LCM                  | https://pixai.art/model/1687631572599847061?utm_source=eap_blog    |
| DMD2                 | https://pixai.art/zh/model/1897811443252033347?utm_source=eap_blog |
| PCM (NormalCFG)      | https://pixai.art/zh/model/1810142527271081205?utm_source=eap_blog |
| WAI-Rectified-4Steps | https://pixai.art/zh/model/1857294002524835135?utm_source=eap_blog |
| Hyper SDXL           | https://pixai.art/zh/model/1783737893546128417?utm_source=eap_blog |
