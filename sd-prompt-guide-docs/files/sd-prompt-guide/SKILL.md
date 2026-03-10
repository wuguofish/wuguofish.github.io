---
name: sd-prompt-guide
description: |
  Stable Diffusion / Illustrious XL 系列模型的 Prompt 實戰指南。
  包含 Danbooru tag 資料庫，可協助使用者查詢有效的 tag 和中英對照。
  
  通用功能：
  (1) 協助使用者撰寫 prompt（任何主題）
  (2) 查詢 Danbooru tag 是否存在、使用次數、別名
  (3) 中英對照查詢
  (4) 模型推薦
  (5) 常見實用小技巧

  特別教學章節（模型較不擅長的領域）：
  (6) 畫男性角色（模型預設偏向女性）
  (7) 畫純風景/物件（模型預設會加入人物）
  (8) 多角色構圖控制（避免特徵混在一起）

  進階技術：
  (9) LoRA 基礎與疊加技巧
  (10) 在 PixAI 上訓練自己的 LoRA
  (11) 加速 LoRA（LCM、DMD2、PCM、WAI-Rectified）
  (12) HiRes 高解析度放大
  (13) Inpaint/Outpaint 局部編輯
  (14) 推薦 DiT 模型（Tsubaki、Serin 等）

  女性向專區：
  (15) BL / 耽美
  (16) 夢圖（OC × 喜歡的角色）
  (17) 乙女遊戲風格的第一人稱 CG

  其他：
  (18) PixAI 點數取得方式
  (19) 參考資料與延伸閱讀
---

# Stable Diffusion Prompt 實戰指南

本指南協助使用者撰寫有效的 AI 繪圖 prompt。
適用於 Illustrious XL、NoobAI、Pony 等 Danbooru 系模型。

> 📺 **圖解版簡報**：部分章節內容整理自 [PixAI 使用心得分享](https://www.canva.com/design/DAG3-sZjTHQ/Mqk015B--mLh5hR-x6t5nA/view)，想看圖文並茂的說明可以參考原始簡報。

## 本指南能幫你什麼？

### 🔍 通用功能

- **Tag 查詢**：確認某個 tag 是否存在、使用次數多少、有什麼別名
- **中英對照**：不知道某個概念的英文 tag 怎麼寫
- **Prompt 建議**：根據你想畫的內容，建議有效的 tag 組合
- **模型推薦**：根據你的需求推薦適合的模型

### 📘 特別教學

針對「模型不擅長」的領域提供詳細指南：

| 主題 | 為什麼需要特別教學 |
|------|-------------------|
| 男性角色 | 訓練資料中女性圖是男性的 4 倍以上，模型預設偏向畫女生 |
| 純風景/物件 | 模型習慣加入人物 |
| 多角色構圖 | 特徵容易混在一起 |

**畫可愛女生不需要特別教學**——這是模型的強項，正常寫 prompt 就能得到好結果。

### 💜 女性向專區

針對女性向創作需求的專門指南：BL、夢圖、乙女 CG 等。

---

## 快速導覽

### 📘 基礎篇

| 我想要... | 參考文件 |
|-----------|----------|
| 快速上手常見技巧 | `references/basics/00-quick-tips.md` |
| 了解模型的特性與限制 | `references/basics/01-why-default-girls.md` |
| 畫出男性角色 | `references/basics/02-drawing-males.md` |
| 畫純風景或純物件 | `references/basics/03-no-humans.md` |
| 控制多角色構圖 | `references/basics/04-multi-character.md` |
| 找適合的 SDXL 模型 | `references/basics/05-recommended-models.md` |
| 中英 prompt 對照 | `references/basics/06-tag-lookup.md` |
| 男性角色 tag 大全 | `references/basics/07-male-tags.md` |
| 了解 LoRA 基礎與疊加 | `references/basics/08-lora-basics.md` |
| 在 PixAI 訓練自己的 LoRA | `references/basics/08b-lora-training.md` |
| 用加速 LoRA 省時間 | `references/basics/09-acceleration-lora.md` |
| 用 HiRes 放大圖片 | `references/basics/10-hires-upscale.md` |
| 用 Inpaint/Outpaint 修圖 | `references/basics/11-inpaint-outpaint.md` |
| 找適合的 DiT 模型 | `references/basics/16-recommended-dit-models.md` |

### 💜 女性向專區

| 我想要... | 參考文件 |
|-----------|----------|
| 畫 BL / 耽美圖 | `references/female-oriented/01-bl-guide.md` |
| 畫夢圖（OC × 角色同框） | `references/female-oriented/02-dream-pictures.md` |
| 畫第一人稱乙女 CG | `references/female-oriented/03-otome-pov.md` |

### 📎 其他

| 我想要... | 參考文件 |
|-----------|----------|
| 了解 PixAI 點數取得方式 | `references/basics/pixai-credits-guide.md` |
| 查看參考資料與延伸閱讀 | `references/basics/15-references.md` |

---

## Tag 資料庫（內建）

本 skill 內建已分類的 Danbooru + e621 合併版 tag 資料庫。

### 檔案結構

```
assets/tags/
├── common.csv              # 常用 tag（使用次數 > 50,000），約 1,030 個
└── categories/
    ├── character.csv       # 角色名（> 1,000 次），約 2,476 個
    ├── artist.csv          # 繪師名（> 1,000 次），約 417 個
    ├── copyright.csv       # 作品名（> 1,000 次），約 1,105 個
    ├── male.csv            # 男性相關（227 個）
    ├── appearance.csv      # 外觀：髮型、髮色、眼睛等（774 個）
    ├── expression.csv      # 表情（58 個）
    ├── composition.csv     # 構圖與視角（41 個）
    ├── pose.csv            # 姿勢與動作（77 個）
    ├── clothing.csv        # 服裝（61 個）
    └── background.csv      # 場景與背景（72 個）
```

### 使用方式

**根據使用者需求選擇對應的分類檔案查詢**：

| 使用者想畫... | 查詢檔案 |
|---------------|----------|
| 特定角色（如初音、2B） | `categories/character.csv` |
| 特定繪師風格 | `categories/artist.csv` |
| 特定作品的角色 | `categories/copyright.csv` |
| 男性角色 | `categories/male.csv` |
| 髮型、髮色、眼睛 | `categories/appearance.csv` |
| 表情 | `categories/expression.csv` |
| 視角、構圖 | `categories/composition.csv` |
| 姿勢、動作 | `categories/pose.csv` |
| 服裝 | `categories/clothing.csv` |
| 場景、背景 | `categories/background.csv` |
| 不確定 / 通用 | `common.csv` |

**查詢範例**：
```bash
# 查詢微笑相關的 tag
grep -i "smile" assets/tags/categories/expression.csv

# 查詢黑髮相關的 tag
grep -i "black.*hair" assets/tags/categories/appearance.csv

# 查詢咖啡廳相關的 tag
grep -i "cafe" assets/tags/categories/background.csv
```

### CSV 格式

```
tag名稱,分類代碼,使用次數,"別名1,別名2"
```

### 底線與空白

**重要**：CSV 中的 tag 使用底線（如 `black_hair`），但實際在 PixAI、ComfyUI 等 SDXL 平台輸入時，通常會轉為空白：

| 資料庫中 | 實際輸入 |
|----------|----------|
| `black_hair` | `black hair` |
| `looking_at_viewer` | `looking at viewer` |
| `1girl` | `1girl`（數字開頭不變）|

查詢時用底線搜尋資料庫，給使用者建議時用空白格式。

### 分類代碼對照表

**Danbooru（代碼 0-5）**：

| 代碼 | 分類 | 說明 |
|------|------|------|
| 0 | general | 一般 tag |
| 1 | artist | 繪師名 |
| 3 | copyright | 作品名（動漫、遊戲等） |
| 4 | character | 角色名 |
| 5 | meta | 圖片屬性（如 highres） |

**e621（合併版中代碼 +7 偏移，變成 8-15）**：

| 代碼 | 分類 | 說明 |
|------|------|------|
| 8 | general | 一般 tag |
| 9 | artist | 繪師名 |
| 11 | character | 角色名 |
| 12 | species | 物種（e621 特有） |
| 13 | invalid | 無效 |
| 14 | meta | 圖片屬性 |
| 15 | lore | 設定/世界觀 |

### 致謝

Tag 資料由 [DraconicDragon](https://github.com/DraconicDragon) 維護，感謝其開源貢獻。

---

## 使用方式

### ⚠️ 重要原則：務必驗證 tag 存在

**在建議任何 tag 之前，必須先確認該 tag 存在於 Danbooru 或 e621 資料庫。**

許多看似合理的英文詞彙其實不是有效的 tag，例如：
- ❌ `young man` → 兩邊都不存在（改用 `1boy` + 具體特徵）
- ❌ `handsome` → 兩邊都不存在（改用 `bishounen` 或 `manly`）
- ❌ `narrow eyes` → 兩邊都不存在（正確是 `narrowed eyes`）
- ❌ `beautiful sky` → 兩邊都不存在（改用 `sky`）

**注意：有些 tag 只存在於其中一邊**：
- `masculine` → e621 ✅ / Danbooru ❌（NoobAI 等混合訓練模型可用）
- `manly` → Danbooru ✅ / e621 ❌（Illustrious 等純 Danbooru 模型用這個）

**驗證方法**：兩階段查詢

**第一階段：查詢本地資料庫**
1. 根據使用者需求，選擇對應的分類檔案
2. 用 grep 搜尋確認 tag 存在
3. 如果分類檔案找不到，再查 `common.csv`

```bash
# 範例：查詢表情相關
grep -i "smile" assets/tags/categories/expression.csv

# 範例：查詢常用 tag
grep -i "cafe" assets/tags/common.csv
```

**第二階段：查詢線上完整資料庫**（本地找不到時）

使用 `web_fetch` 取得完整 CSV 並搜尋：
```
https://raw.githubusercontent.com/DraconicDragon/dbr-e621-lists-archive/main/tag-lists/danbooru_e621_merged/danbooru_e621_merged_2024-12-22_pt25-ia-dd-ed.csv
```

只有在線上也找不到時，才能確定該 tag 不存在。

**注意**：線上 CSV 約 15MB，包含 70 萬+ 個 tag，建議只在本地找不到時才查詢。

### 📖 Tag 定義查詢：Danbooru Wiki

許多 tag 的定義並不直覺，尤其是：
- 相似 tag 之間的差異（如 `chess` vs `chess_piece` vs `chessboard`）
- 專有名詞或特定概念
- 有特殊使用規則的 tag

**引導使用者查看 Wiki**：
```
https://danbooru.donmai.us/wiki_pages/{tag名稱}
```

**範例**：使用者想畫下棋相關的圖，但不確定該用哪個 tag

→ 提供三個相關 tag 的 Wiki 連結讓使用者自行確認差異：
- https://danbooru.donmai.us/wiki_pages/chess （下棋這個活動）
- https://danbooru.donmai.us/wiki_pages/chess_piece （棋子）
- https://danbooru.donmai.us/wiki_pages/chessboard （棋盤）

**何時引導查 Wiki**：
- 找到多個相似 tag，不確定哪個最符合使用者需求
- tag 名稱看起來有歧義或專業術語
- 使用者對 tag 的效果有疑問

**分類代碼說明**（混合版）：
- Danbooru：0=一般, 1=繪師, 3=作品, 4=角色, 5=meta
- e621：8=一般, 9=繪師, 11=角色, 12=物種, 14=meta, 15=lore

### 查詢 tag

使用者：「請問『微笑』的英文 tag 是什麼？」

→ 微笑是表情，查詢 expression.csv：
```bash
grep -i "smile" assets/tags/categories/expression.csv
```

→ 回答：`smile`（使用次數 2,873,890）

### 確認 tag 是否存在

使用者：「young man 這個 tag 存在嗎？」

→ 查詢 common.csv 和 male.csv 都沒有結果，告知使用者這不是有效的 tag，並建議替代方案（如 `1boy`, `male_focus`, `bishounen` 等）。

### 協助撰寫 prompt

使用者：「我想畫一個在咖啡廳看書的黑髮眼鏡少女」

→ 拆解需求並查詢對應分類：
1. 少女 → `common.csv` → `1girl`
2. 黑髮 → `appearance.csv` → `black_hair`
3. 眼鏡 → `appearance.csv` → `glasses`
4. 看書 → `pose.csv` → `reading`, `book`
5. 咖啡廳 → `background.csv` → `cafe`

→ 組合成 prompt（使用空白格式）：
```
1girl, solo, black hair, glasses,
reading, book, 
cafe, indoors
```

### 除錯

使用者：「為什麼我畫男生一直出現女生？」

→ 參考 `references/basics/02-drawing-males.md` 提供解決方案
