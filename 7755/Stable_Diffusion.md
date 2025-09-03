<h1 id="stable-diffusion提示詞技巧（適用pixai-xl模型）">Stable Diffusion提示詞技巧（適用PixAI XL模型）</h1>
<h2 id="提示詞的書寫建議">提示詞的書寫建議</h2>
<h3 id="先看模型的預設建議提示詞">先看模型的預設建議提示詞</h3>
<p>每個模型在訓練後，會被歸納出特別容易反應的提示詞。<br>
有正向也有負向。<br>
意思是，這個模型的訓練資料特別適合算這些內容。</p>
<h3 id="建議依照以下排序">建議依照以下排序</h3>
<ul>
<li>畫面主元素</li>
<li>畫面細節元素</li>
<li>鏡頭</li>
<li>畫風</li>
<li>增加畫質的詞條</li>
</ul>
<p>範例：</p>
<pre><code>1boy, black hair, upper body portrait, anime style, masterpiece
</code></pre>
<p>每個元素可以不只一個單字，每個單字用逗號分隔。<br>
提示詞可以分行，但運算的時候分行會被省略，所以分行後也要記得用逗號隔開。</p>
<h2 id="提示詞符號">提示詞符號</h2>
<h3 id="權重符號">權重符號</h3>
<p>沒有下符號的情況下，預設每個提示詞權重都是1。<br>
如果有特定的提示詞希望模型比較重視/忽略，可以用權重符號修改提示詞的權重</p>

<table>
<thead>
<tr>
<th>寫法</th>
<th>範例</th>
<th>數值算法</th>
<th>說明</th>
</tr>
</thead>
<tbody>
<tr>
<td>(關鍵字: 權重)</td>
<td>(black hair: 1.2)</td>
<td>直接等於使用者寫的權重值</td>
<td>權重&lt;1時，表示減弱；權重&gt;1時，表示增強。範圍為0.1~100</td>
</tr>
<tr>
<td>(關鍵字)</td>
<td>((black hair))</td>
<td>每增加一層括號，乘1.1倍。</td>
<td>範例為1.1 * 1.1 = 1.21</td>
</tr>
<tr>
<td>{關鍵字}</td>
<td>{{black hair}}</td>
<td>每增加一層括號，乘1.05倍。</td>
<td>範例為1.05 * 1.05 = 1.1025</td>
</tr>
<tr>
<td>[關鍵字]</td>
<td>[[black hair]]</td>
<td>每增加一層括號，除以1.05。</td>
<td>範例為1/1.05/1.05 = 0.907</td>
</tr>
</tbody>
</table><blockquote>
<p>注意，如果關鍵字內想要單純的表達括號，可以用\( \)來表示。<br>
例如：1girl \(red hair\)<br>
但不建議這個寫法。</p>
</blockquote>
<h3 id="運算符號">運算符號</h3>

<table>
<thead>
<tr>
<th>寫法</th>
<th>範例</th>
<th>說明</th>
</tr>
</thead>
<tbody>
<tr>
<td>AND</td>
<td>a cat AND a dog</td>
<td>把兩個提示詞結合在一起，表示需同時滿足兩者條件，注意AND一定要完全大寫</td>
</tr>
<tr>
<td>+</td>
<td>a cat + a dog</td>
<td>把兩個提示詞結合在一起，表示需同時滿足兩者條件</td>
</tr>
<tr>
<td>|</td>
<td>a busy city street|illustration|cinematic lighting</td>
<td>或，使用這個表示方式，模型將會產出可能的組合，以範例為例，出現的圖片會變成這三個元素的所有可能組合（元素有可能不出現）。</td>
</tr>
<tr>
<td>[|]</td>
<td>[cow|horse] in a field</td>
<td>循環取樣，以範例來說，最後會得到一個介於牛和馬之間的動物</td>
</tr>
<tr>
<td>_</td>
<td>coffee_cake</td>
<td>連接號，表示兩個關鍵字為同一個單字，以範例來說，會生成咖啡口味的蛋糕，如果沒有加連接號，可能會生成一杯咖啡和一塊蛋糕</td>
</tr>
</tbody>
</table><h3 id="生成控制符號">生成控制符號</h3>
<p>可以用以下格式來控制模型產圖片時的取樣時機</p>
<pre><code>[from:to:when]
</code></pre>
<p>from跟to可以擇一填寫，例如：</p>
<ul>
<li>全寫：[mountain:lake:0.25]</li>
<li>只有from：[mountain::0.25]</li>
<li>只有to：[lake:0.25]</li>
</ul>
<p>其中when代表取樣時機，假設when = 0.25時，表示：<br>
進度0% ~ 25%的時候要取樣"from"的元素；<br>
進度25% ~ 100%要取樣"to"的元素。</p>
<h2 id="常用提示詞參考">常用提示詞參考</h2>
<h3 id="鏡頭遠近">鏡頭遠近</h3>
<ul>
<li><code>extreme close-up</code>  超近鏡</li>
<li><code>close-up</code>  近鏡</li>
<li><code>medium close-up</code>  中近鏡</li>
<li><code>medium shot</code>  中景鏡</li>
<li><code>cowboy shot</code>  上半身至大腿</li>
<li><code>medium full shot</code>  中風全景鏡</li>
<li><code>full shot</code>  全景鏡</li>
<li><code>long shot</code>  遠鏡</li>
<li><code>establishing shot</code>  場景鏡</li>
</ul>
<h3 id="鏡頭聚焦">鏡頭聚焦</h3>
<ul>
<li><code>upper body</code>  上半身</li>
<li><code>full body</code>  全身</li>
<li><code>wide angle view</code> 廣角鏡</li>
</ul>
<h3 id="鏡頭視角">鏡頭視角</h3>
<ul>
<li><code>point-of-view</code>、<code>pov</code>  主觀視角</li>
<li><code>female pov</code> （女性向）主觀視角</li>
<li><code>dutch angle</code> 斜角鏡頭</li>
<li><code>shot from side</code> 從人物側面拍攝</li>
<li><code>shot from back</code>、<code>shot from behind</code> 從人物背面拍攝</li>
<li><code>shot from below</code> 從下方拍攝</li>
<li><code>shot from above</code> 從上方拍攝</li>
<li><code>overhead shot</code>  俯視</li>
<li><code>bird's eye view</code>  鳥瞰</li>
<li><code>high angle</code>  高角度</li>
<li><code>slightly above</code>  微高角度</li>
<li><code>straight on</code>  水平拍攝</li>
<li><code>selfie</code>  自拍</li>
<li><code>45 degree angle</code> 45度角</li>
<li><code>three-quarter view</code> 四分之三視圖，特別用在描述人物肖像畫上，視角介於側臉輪廓與正面全臉之間</li>
</ul>
<h3 id="畫風">畫風</h3>
<ul>
<li>illustration, painting, paintbrush</li>
<li>anime, comic, digital art, game CG</li>
<li>semi-realistic, 2.5D</li>
<li>photorealistic, realistic, photograph</li>
</ul>
<h3 id="畫質">畫質</h3>
<ul>
<li>通用：best quality, ultra-detailed, masterpiece, 8k</li>
<li>超高解析度或寫實風格適用：extremely detailed</li>
<li>3D建模風格適用：unreal engine rendered, 3D rendered</li>
</ul>
<h3 id="人物篇">人物篇</h3>
<h4 id="頭髮">頭髮</h4>
<p>– <strong>長度</strong></p>
<ul>
<li>absurdly long hair</li>
<li>very long hair</li>
<li>waist-length hair</li>
<li>long hair</li>
<li>medium hair</li>
<li>shoulder-length hair</li>
<li>short hair</li>
<li>very short hair</li>
</ul>
<p>– <strong>髮色</strong></p>
<ul>
<li>多髮色
<ul>
<li>two-tone hair</li>
<li>multicolored hair</li>
<li>gradient hair</li>
</ul>
</li>
<li>blonde hair</li>
<li>brown hair</li>
<li>black hair</li>
<li>blue hair</li>
<li>purple hair</li>
<li>white hair</li>
<li>red hair</li>
<li>grey hair</li>
<li>green hair</li>
<li>silver hair</li>
<li>orange hair</li>
<li>aqua hair</li>
<li>light brown hair</li>
</ul>
<p>– <strong>髮型</strong></p>
<ul>
<li>flipped hair</li>
<li>spiked hair</li>
<li>messy hair</li>
<li>wavy hair</li>
<li>curly hair</li>
<li>ringlets</li>
<li>big hair</li>
<li>afro</li>
<li>dreadlocks</li>
<li>bob cut</li>
<li>hime cut</li>
<li>hair bun
<ul>
<li>double bun</li>
<li>single hair bun</li>
<li>braided bun</li>
<li>cone hair bun</li>
<li>topknot</li>
</ul>
</li>
<li>ponytail
<ul>
<li>short ponytail</li>
<li>high ponytail</li>
<li>side ponytail</li>
<li>folded ponytail</li>
</ul>
</li>
<li>braid
<ul>
<li>single braid</li>
<li>twin braids</li>
<li>side braid</li>
<li>french braid</li>
</ul>
</li>
<li>twintails
<ul>
<li>low twintails</li>
<li>short twintails</li>
<li>quad tails</li>
<li>twin drills</li>
</ul>
</li>
<li>half updo</li>
<li>bald</li>
</ul>
<p>– <strong>瀏海</strong></p>
<ul>
<li>bangs</li>
<li>natural bangs</li>
<li>parted bangs</li>
<li>blunt bangs</li>
<li>swept bangs</li>
<li>overlap bangs</li>
<li>crossed bangs、hair between eyes</li>
<li>asymmetrical bangs</li>
<li>arched bangs</li>
<li>hair pulled back</li>
<li>hair slicked back</li>
<li>bangs pinned back</li>
<li>hair over one eye</li>
</ul>
<p>– <strong>呆毛</strong></p>
<ul>
<li>ahoge</li>
<li>huge ahoge</li>
<li>antenna hair</li>
</ul>
<hr>
<h3 id="參考資料">參考資料</h3>
<p><a href="https://github.com/Stability-AI/stablediffusion">https://github.com/Stability-AI/stablediffusion</a><br>
<a href="https://stable-diffusion-art.com/models/">https://stable-diffusion-art.com/models/</a><br>
<a href="https://stable-diffusion-art.com/prompt-guide/">https://stable-diffusion-art.com/prompt-guide/</a><br>
<a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">https://github.com/AUTOMATIC1111/stable-diffusion-webui</a><br>
<a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#stable-diffusion-20">https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#stable-diffusion-20</a></p>
<h3 id="額外補充">額外補充</h3>
<p>SDXL的原始論文：<a href="https://arxiv.org/abs/2307.01952">https://arxiv.org/abs/2307.01952</a></p>

