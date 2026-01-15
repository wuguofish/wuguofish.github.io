# SD Prompt 實戰指南

> Stable Diffusion / Illustrious XL 系列模型的 Prompt 實戰指南

## 這是什麼？

這份指南專門解決 AI 繪圖模型的「偏科問題」——模型很會畫可愛女生，但畫其他東西就需要特別技巧。

## 適合誰？

- 想畫**男性角色**但一直畫成女生的人
- 想畫**純風景/物件**但一直冒出人的人
- 想畫 **BL / 耽美**的創作者
- 想畫**夢圖**（自己的 OC 和喜歡的角色同框）的人
- 想畫**乙女遊戲風 CG**的人

## 快速開始

| 我想要... | 看這篇 |
|-----------|--------|
| 畫男生 | [畫男性角色](basics/02-drawing-males.md) |
| 畫風景/物件 | [純風景/純物件](basics/03-no-humans.md) |
| 畫 BL | [BL / 耽美指南](female-oriented/01-bl-guide.md) |
| 畫夢圖 | [夢圖指南](female-oriented/02-dream-pictures.md) |
| 畫乙女 CG | [第一人稱乙女 CG](female-oriented/03-otome-pov.md) |
| 查 Tag 怎麼寫 | [常用 Tag 中英對照](basics/06-tag-lookup.md) |

## 重要觀念

### Tag 必須存在於資料庫

AI 模型是用 Danbooru / e621 的圖片訓練的，所以 **只有資料庫裡有的 tag 才有效**。

常見錯誤：
- ❌ `young man` → 不存在（改用 `1boy` + 具體特徵）
- ❌ `handsome` → 不存在（改用 `bishounen` 或 `manly`）
- ❌ `narrow eyes` → 不存在（正確是 `narrowed eyes`）

### 底線要換成空白

資料庫用底線（`black_hair`），但實際輸入時用空白（`black hair`）。

## 資料來源

本指南的 tag 都經過 Danbooru / e621 資料庫驗證：
- [Danbooru Tag 搜尋](https://danbooru.donmai.us/tags)
- [e621 Tag 搜尋](https://e621.net/tags)
- [Tag 資料庫 (GitHub)](https://github.com/DraconicDragon/dbr-e621-lists-archive)

---

## 給 AI 助理使用者

如果你使用 ChatGPT、Gemini 或其他 AI 助理，可以：
1. 把這個網站的網址貼給 AI，請它「閱讀這個網頁」
2. 或直接複製需要的章節內容給 AI 參考

---

*最後更新：2025-01*
