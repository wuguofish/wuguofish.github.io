# 夢圖攻略：OC × 角色同框指南

## 什麼是夢圖？

「夢圖」是指將自己的二次元人設（OC, Original Character）和喜歡的角色畫在同一張圖裡的同人創作。

## 常見問題

### 問題 1：兩個角色的特徵混在一起

**現象**：
- 我的 OC 是紅髮，角色是藍髮，結果兩個都變成紫髮
- 我的 OC 穿便服，角色穿制服，結果兩個都穿奇怪的混合服裝

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

| 區塊 | 功能 |
|------|------|
| 第一行 | 整體設定：人數、關係、位置、互動、場景、畫風 |
| `boy:` / `girl:` | BG 向：分別描述男女角色 |
| `right:` / `left:` | BL 向：分別描述左右角色 |

**重點**：
- 這種寫法讓模型能清楚區分兩個角色
- 不會把特徵混在一起
- 搭配 LoRA 效果更好

---

## 範例 prompt

### 範例 1：BG 向夢圖（女 OC × 男角色）

```
Positive:
(couple), 1boy, 1girl, holding hands, looking at another, cafe, brown hair, red hair

boy: short hair, brown hair, golden eyes, smile, tall male, white shirt, sitting
girl: my OC Sakura, long hair, red hair, hair ribbon, green eyes, blush, sundress

Negative:
yaoi, yuri, multiple boys, multiple girls
```

### 範例 2：BL 向夢圖（男 OC × 男角色）

```
Positive:
2boys, yaoi, my OC Rei at right, Protagonist at left, hug from behind, bedroom, night

right: Rei, long hair, ponytail, silver hair, red eyes, pale skin, black coat
left: Protagonist, short hair, black hair, blue eyes, casual clothes, blush

Negative:
1girl, female, breasts, feminine, hetero
```

### 範例 3：乙女向夢圖（使用角色 LoRA）

```
Positive:
(couple), 1boy, 1girl, kiss, night sky, starry sky, 角色LoRA觸發詞

boy: 角色名, 角色外觀描述
girl: my OC, long hair, pink hair, purple eyes, white dress, closed eyes, blush

Negative:
yaoi, yuri, multiple boys, multiple girls
```

※ 在 PixAI 介面上選擇對應的 LoRA 並調整權重即可，不需手動輸入 `<lora:xxx:0.7>` 語法。

---

## 進階技巧

### 第一人稱視角（乙女 CG 風格）

如果你想畫「從自己的視角看著他」的乙女遊戲 CG 風格圖片，請參考：

👉 **`references/female-oriented/03-otome-pov.md`**

### 為什麼區塊語法有效？

`boy:` / `girl:` 和 `right:` / `left:` 這種寫法利用了模型訓練時學到的「條件式描述」結構。
模型會把該區塊後的描述只套用到對應的角色，不會混在一起。

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

| 問題 | 解法 |
|------|------|
| 髮色混在一起 | 加大色差（如 `dark hair` vs `white hair`） |
| 服裝混在一起 | 用位置詞分離，加強描述具體度 |
| 變成同一個人 | 加入 `different appearance`, `distinct features` |
| 角色消失只剩一人 | 確認有寫 `2boys` 或 `1boy 1girl` |
| 莫名出現第三人 | negative 加 `multiple boys` 或 `crowd` |
