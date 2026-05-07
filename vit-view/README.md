# AI 是怎麼看你的圖的

純前端的 ViT (Vision Transformer) 視覺退化模擬工具。把任何一張圖丟進來,看看多模態 LLM 的 vision encoder 拿到的是什麼。

## 為什麼做這個

很多人不理解為什麼 AI 對圖片的反應有時候很怪——把麵包誤判成裸照、看不懂藝術筆觸、把寶可夢的訓練師認成寶貝球。其實這些「錯誤」都來自同一個機制:vision encoder 為了把圖翻譯成 LLM 能讀的 token,做了大量的有損壓縮。

這個工具用四格對照,直觀呈現那個壓縮過程:

1. **Original** — 原圖
2. **Resized to 224×224** — ViT 標準輸入尺寸,第一次資訊損失
3. **16×16 patch average** — 切成 patches 取顏色平均,空間細節死亡
4. **Semantic collapse** — 模擬 CLIP 風格的特徵壓縮,只剩粗略色塊語意

## 隱私

**這是純前端的工具,所有運算在你的瀏覽器中完成。圖片不會被上傳到任何伺服器。**

不信的話打開開發者工具的 Network 分頁,選圖、處理、下載,全程不會看到任何 outbound HTTP request。

如果連 GitHub Pages 都不想用,你也可以 clone 這個 repo,直接用瀏覽器打開 `index.html`(`file://` 協議)使用。完全離線。

## 使用

線上版:`https://<your-username>.github.io/<repo-name>/`

本地用:下載 `index.html`,雙擊用瀏覽器打開即可。

## 技術細節

- 純 HTML + CSS + JavaScript,無任何第三方依賴
- 使用 Canvas API 處理像素
- K-means 用 JS 從頭實作(seed=42,輸出可重現)
- 上傳的圖會先縮到最長邊 2048px(避免吃光記憶體)

## 部署到自己的 GitHub Pages

```bash
git clone <this-repo>
cd <this-repo>
git remote set-url origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

然後到 repo 的 Settings → Pages → Source 選 main branch / root,等幾分鐘就會上線。

## License

MIT
