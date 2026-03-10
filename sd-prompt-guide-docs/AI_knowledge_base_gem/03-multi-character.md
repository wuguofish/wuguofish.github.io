# 多角色構圖控制指南

## 常見問題

當你想畫兩個以上的角色時，常會遇到：

1. **特徵混在一起** — A 角色的紅髮跑到 B 角色身上
2. **變成同一個人** — 兩個角色長得一模一樣
3. **人數錯誤** — 要兩個人卻出現三個，或只剩一個
4. **性別錯誤** — 要畫兩個男生卻出現女生

**⚠️ 重要提醒：多人構圖不是 SDXL 的強項**
SDXL 模型在處理多角色時容易出現「特徵互染」問題。如果你需要畫**三個人以上**，建議考慮使用 **DiT 模型**，它對多人構圖的處理能力更強。詳見 推薦 DiT 模型。

## 解決方案：區塊分離語法

> **⚠️ 重要提醒：SDXL模型沒有理解提示詞內構圖配置的能力**
>
>
> 本章節提供的建議寫法是目前中文區社群的大量測試後發現能提高機率的方式之一。
>
> 目前**推測**此方法能提高成功率是靠CLIP的基礎理解能力，但prompt越長效果越差。
>
> 增加 CFG 或許能提升效果，但並不保證能成功。

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

🖼️ 實際生成效果：[範例圖](<https://pixai.art/artwork/1969578350609405807>)

Positive:
```
2boys, Kuro at right, Shiro at left, standing, talking, cafe,

right: Kuro, short hair, black hair, red eyes, tall male, black jacket,
left: Shiro, long hair, white hair, blue eyes, slim, white coat,

```

Negative:
```
1girl, 2girls, breasts,

```

### 範例 2：一男一女

🖼️ 實際生成效果：

- [範例圖 1](<https://pixai.art/artwork/1969579562679412461>)
- [範例圖 2](<https://pixai.art/artwork/1969579640697197971>)

Positive:
```
1boy, 1girl, holding hands, walking, street, sunset,

boy: short hair, brown hair, tall male, casual clothes,
girl: long hair, blonde hair, sundress, smile,

```

Negative:
```
yaoi, yuri

```

### 範例 3：三人以上

人數越多越難控制，建議：

- 明確寫出人數（`3boys`, `2boys 1girl`）
- 每個角色的特徵差異要大（髮色完全不同）
- 構圖保持簡單（並排站立比複雜互動容易成功）

🖼️ 實際生成效果：（可以看出三個人多少會互相汙染）

- [範例圖 1](<https://pixai.art/artwork/1969583487796045788>)
- [範例圖 2](<https://pixai.art/artwork/1969583317821939169>)

Positive:
```
3boys, standing, simple background,

leftmost: short hair, black hair, glasses,
center: medium hair, red hair, tall male,
rightmost: long hair, blonde hair, slim,

```

Negative:
```
1girl, 2girls, 3girls

```

---

## 進階技巧

### 調高 CFG Scale

畫多人時，把 **CFG Scale 調高到 5.5 ~ 6.5**，可以讓模型更嚴格遵守你的提示詞，減少特徵互染的問題。

💡 一般單人圖建議 CFG 5~7，但多人構圖拉到 6 以上效果會比較好。太高（超過 8）可能會崩圖，請自行測試找到平衡點。

### 加大特徵差異

如果角色還是會混在一起，試著讓差異更明顯：

| 特徵  | 建議做法               |
|-----|--------------------|
| 髮色  | 用對比色：黑 vs 白、紅 vs 藍 |
| 髮長  | 短髮 vs 長髮           |
| 體型  | tall male vs slim  |
| 服裝  | 完全不同風格             |

### 控制人數

| 你要的    | 寫法                      | Negative                      |
|--------|-------------------------|-------------------------------|
| 剛好 2 人 | `2boys` 或 `1boy 1girl`  | `multiple boys, crowd, group` |
| 剛好 3 人 | `3boys` 或 `2boys 1girl` | `4boys, crowd, group`         |

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

---

## 補救方案：Inpaint

如果生成後發現特徵還是互染了，不用氣餒！可以使用 **Inpaint**功能來局部修正：

- 框選出問題區域（例如髮色錯誤的部分）
- 在 Inpaint 的提示詞中只寫該區域應該有的特徵
- 重新生成該區域即可

詳細操作請參考 Inpaint/Outpaint 指南。
