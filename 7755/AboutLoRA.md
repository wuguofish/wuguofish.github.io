<h1 id="關於lora">關於LoRA</h1>
<h2 id="什麼是lora？">什麼是LoRA？</h2>
<h3 id="low-rank-adaptation（低秩適應），簡稱lora">Low-rank adaptation（低秩適應），簡稱LoRA</h3>
<ul>
<li>對既有模型進行微調的小模型</li>
<li>數學意義：在原始的深度學習模型運算結束後，加上一個矩陣運算，微調最終結果。</li>
<li>可以理解成一種目的性比較強的<strong>圖片濾鏡</strong></li>
</ul>
<h2 id="lora怎麼來的？">LoRA怎麼來的？</h2>
<ul>
<li>準備好大量的訓練圖片</li>
<li>選擇一個算圖模型</li>
<li>告訴程式，在特定關鍵字下，模型算出來的預期結果要像這些訓練圖片一樣</li>
<li>在這個過程中，程式會學會算圖模型的結果必須做什麼樣的<strong>額外運算</strong>才會像訓練圖片</li>
<li>這個額外運算就是LoRA</li>
</ul>
<h3 id="所以選擇lora的時候，必須看當初訓練lora時用的模型來選！">所以選擇LoRA的時候，必須看當初訓練LoRA時用的模型來選！</h3>
<p>舉例：用A模型訓練出來的LoRA，套在B模型上，有可能會和A模型效果差很多</p>
<h3 id="如果算圖時，沒有選擇當初訓練lora時用的模型，會怎麼樣？">如果算圖時，沒有選擇當初訓練LoRA時用的模型，會怎麼樣？</h3>
<ul>
<li>不會怎麼樣，就是效果可能會有點不同於預期。</li>
<li>像是買B牌的咖哩醬，但是用A牌的建議份量去煮</li>
<li>雖然跟預期不符，但可能反而會很好吃</li>
</ul>
<h3 id="算圖時，找不到和模型一致的lora怎麼辦？">算圖時，找不到和模型一致的LoRA怎麼辦？</h3>
<p>退而求其次，選同一個家族的模型。（見下節）</p>
<h2 id="pixai的常見模型">PixAI的常見模型</h2>
<h3 id="目前大多數的模型，都是從其他模型變體而來。">目前大多數的模型，都是從其他模型變體而來。</h3>
<p>也就是拿現有的模型加上一些資料後再訓練過。<br>
意思就是這些模型其實會有相似的表現。<br>
<strong>可以把這些模型其實都是同一個父母生的兄弟姊妹。</strong></p>
<h3 id="兩大xl模型家族：">兩大XL模型家族：</h3>
<ol>
<li><strong><a href="https://civitai.com/articles/8380/tips-for-illustrious-xl-prompting-updates">Illustrious</a></strong>：
<ul>
<li>目前最受歡迎的Stable Diffusion XL模型</li>
<li>由Onoma AI Research基於大量Danbooru標籤數據訓練</li>
<li>常見代表模型：
<ul>
<li>Plant Milk、Nova Orange、Aüngir、NobuAI、Dvine、Letters</li>
</ul>
</li>
</ul>
</li>
<li><strong><a href="https://stable-diffusion-art.com/pony-diffusion-v6-xl/">Pony</a></strong>：
<ul>
<li>前一個SD圈最受歡迎的二次元SDXL模型</li>
<li>透過大量動漫、卡通和超濃起司圖訓練而來</li>
<li>常見代表模型：
<ul>
<li>Mala Style、AutismMix</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3 id="這兩個模型家族認識的提示關鍵字不一樣">這兩個模型家族認識的提示關鍵字不一樣</h3>
<p>例如：<br>
Pony家族提升畫質的關鍵字：<code>score_9, score_8_up, score_7_up</code><br>
對Illustrious家族的來說不適用。</p>
<h2 id="如何知道模型是基於哪個模型而來？">如何知道模型是基於哪個模型而來？</h2>
<p>可以到<a href="https://civitai.com/">CivitAI</a>查詢，大部分的模型都會在那邊發佈。</p>
<ul>
<li>以<a href="https://civitai.com/models/967405/nova-orange-xl">Nova Orange XL</a>為例：</li>
<li>Details的部份，會有兩個關鍵資料
<ul>
<li>type：模型類型
<ul>
<li>Checkpoint Merge：從其他模型變體</li>
<li>Checkpoint Trained：從頭訓練的</li>
</ul>
</li>
<li>Base Model：
<ul>
<li>如果是Checkpoint Merge，這個欄位會寫它是從哪個模型轉移訓練來的</li>
<li>以Nova Orange XL為例，可以看到它的頁面寫<code>Illustrious</code>，由此可知它是屬於Illustrious家族的模型。</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 id="lora權重的影響">LoRA權重的影響</h2>
<p>由於LoRA是濾鏡，所以是可以調整權重的，權重越大，受到LoRA的影響越大，權重越小則受到LoRA的影響越小。<br>
權重=0時等同於沒有套用。</p>
<p>當LoRA為負的時候，表示圖片的效果要把LoRA的部份盡量避免掉。</p>
<p>因此可以視自己需要調整LoRA權重。</p>
<p>有些LoRA作者也會在說明裡面寫建議的權重。</p>

