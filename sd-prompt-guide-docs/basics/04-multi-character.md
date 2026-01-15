# 多角色構圖控制指南

## 常見問題

當你想畫兩個以上的角色時，常會遇到：

1. **特徵混在一起** — A 角色的紅髮跑到 B 角色身上
2. **變成同一個人** — 兩個角色長得一模一樣
3. **人數錯誤** — 要兩個人卻出現三個，或只剩一個
4. **性別錯誤** — 要畫兩個男生卻出現女生

## 解決方案：區塊分離語法

經過實測，以下寫法最能讓模型清楚區分不同角色：

### 用位置區分（推薦）

```
2boys, 角色A at right, 角色B at left, 互動, 場景

right: 角色A名字, 右邊角色的詳細特徵
left: 角色B名字, 左邊角色的詳細特徵
```

### 用性別區分

```
1boy, 1girl, 互動, 場景

boy: 男生詳細特徵
girl: 女生詳細特徵
```

## 為什麼這樣寫有效？

`right:` / `left:` 和 `boy:` / `girl:` 這種區塊語法，利用了模型訓練時學到的「條件式描述」結構。模型會把該區塊後的描述只套用到對應的角色，不會混在一起。

---

## 範例

### 範例 1：兩個男性角色

```
Positive:
2boys, Kuro at right, Shiro at left, standing, talking, cafe

right: Kuro, short hair, black hair, red eyes, tall male, black jacket
left: Shiro, long hair, white hair, blue eyes, slim, white coat

Negative:
1girl, female, breasts
```

### 範例 2：一男一女

```
Positive:
1boy, 1girl, holding hands, walking, street, sunset

boy: short hair, brown hair, tall male, casual clothes
girl: long hair, blonde hair, sundress, smile

Negative:
yaoi, yuri
```

### 範例 3：三人以上

人數越多越難控制，建議：
- 明確寫出人數（`3boys`, `2boys 1girl`）
- 每個角色的特徵差異要大（髮色完全不同）
- 構圖保持簡單（並排站立比複雜互動容易成功）

```
Positive:
3boys, standing, group picture, simple background

leftmost: short hair, black hair, glasses
center: medium hair, red hair, tall male  
rightmost: long hair, blonde hair, slim

Negative:
1girl, female
```

---

## 進階技巧

### 加大特徵差異

如果角色還是會混在一起，試著讓差異更明顯：

| 特徵 | 建議做法 |
|------|----------|
| 髮色 | 用對比色：黑 vs 白、紅 vs 藍 |
| 髮長 | 短髮 vs 長髮 |
| 體型 | tall male vs slim |
| 服裝 | 完全不同風格 |

### 控制人數

| 你要的 | 寫法 | Negative |
|--------|------|----------|
| 剛好 2 人 | `2boys` 或 `1boy 1girl` | `multiple boys, crowd, group` |
| 剛好 3 人 | `3boys` 或 `2boys 1girl` | `4boys, crowd, group` |

### 構圖建議

**容易成功**：
- 並肩站立
- 坐在一起（不重疊）
- 一前一後
- 對視

**難度較高**：
- 擁抱（身體重疊）
- 接吻（臉部靠近）
- 打鬥（動作複雜）

建議從簡單構圖開始，熟練後再挑戰複雜構圖。
