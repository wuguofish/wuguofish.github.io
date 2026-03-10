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
