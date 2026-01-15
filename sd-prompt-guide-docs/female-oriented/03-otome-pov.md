# 第一人稱乙女 CG 風格指南

## 什麼是乙女 CG 風格？

乙女遊戲（女性向戀愛遊戲）中常見的 CG 構圖：
- 從女主角（玩家）的視角看著男性角色
- 男性角色看著「鏡頭」＝看著你
- 可能有互動：牽手、摸頭、比愛心等

這種構圖讓玩家有「他在看著我」的沉浸感。

---

## 核心 Tag

| Tag | 功能 |
|-----|------|
| `female pov` | 第一人稱女性視角 |
| `1girl out of frame` | 暗示「我」在畫面外但存在 |
| `hetero` | 強調異性戀互動 |
| `looking at viewer` | 角色看著鏡頭（看著你）|
| `pov hands` | 畫面中出現「自己的手」|

---

## ⚠️ 重要提醒

由於訓練資料的關係，`female pov` 有時會觸發 NSFW 內容。

**如果想要單純夢幻唯美的畫面，務必在 negative prompt 加上 `nsfw`。**

---

## 萬用公式

```
Positive:
1boy, solo, male focus, female pov, 
1girl out of frame, hetero, looking at viewer,
[互動], [角色描述], [場景]

Negative:
nsfw, nude
```

---

## 範例

### 範例 1：比愛心（實測成功）

使用模型：ChocoMint Mix

```
Positive:
solo focus, male focus, 1boy, 
bangs, black hair, short hair, brown eyes, glasses,
manly, masculine, smile, 
business casual, looking at viewer,
角色LoRA觸發詞,
half-heart hands, cowboy shot,
simple background, white background,
1girl out of frame, hetero, female pov

Negative:
nsfw, nude
```

**重點**：
- `manly` (Danbooru) 和 `masculine` (e621) 可以組合使用，增強陽剛感
- `half-heart hands` — 比一半愛心（和畫面外的「我」合成完整愛心）
- `1girl out of frame` + `hetero` — 暗示有女生在場但不入鏡

### 範例 2：牽手

```
Positive:
1boy, solo, male focus, female pov,
holding hands, pov hands,
looking at viewer, smile, blush,
bishounen, black hair, blue eyes,
outdoors, sunset

Negative:
nsfw, nude, 1girl, breasts
```

### 範例 3：撫摸臉頰

```
Positive:
1boy, solo, male focus, female pov,
hand on another's cheek, pov hands,
looking at viewer, blush,
bishounen, white hair, red eyes,
bedroom, night

Negative:
nsfw, nude, 1girl, breasts
```

### 範例 4：被摸頭

```
Positive:
1boy, solo, male focus, female pov,
hand on another's head, pov hands,
looking at viewer, closed eyes, smile,
black hair, school uniform,
simple background

Negative:
nsfw, nude, 1girl, breasts
```

---

## 常用互動 Tag

| 中文 | Tag |
|------|-----|
| 牽手 | `holding hands`, `pov hands` |
| 比一半愛心 | `half-heart hands` |
| 摸對方的頭 | `hand on another's head` |
| 摸對方的臉 | `hand on another's cheek` |
| 餵食 | `feeding`, `pov hands` |
| 擦眼淚 | `wiping tears` |

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
- 再慢慢加入 `pov hands` 等複雜互動
