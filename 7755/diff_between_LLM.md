<h1 id="為什麼不同模型會有不同「個性」？">為什麼不同模型會有不同「個性」？</h1>
<ol>
<li>
<p><strong>基礎訓練資料不同 — 語料與權重會影響語氣與知識偏好</strong><br>
大型模型先做大量「自監督預訓練（pretraining）」，使用的語料來源、比例、過濾策略都會決定它對某些表達風格或知識領域的偏好。不同廠商／版本用的語料不一樣，所以風格也不同。(<a href="https://cdn.openai.com/papers/gpt-4-system-card.pdf?utm_source=chatgpt.com" title="[PDF] GPT-4 System Card | OpenAI">OpenAI</a>)</p>
</li>
<li>
<p><strong>指令微調（instruction tuning / SFT）會改變「服從指令」與回覆風格</strong><br>
訓練後會用人類示例來教模型如何「回應指令」，這一步會把預訓練的生成傾向調成更適合當助理的語氣（例如更有條理、少跑題）。OpenAI、Google 等都有把這步當作核心流程。(<a href="https://cdn.openai.com/papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf?utm_source=chatgpt.com" title="Training language models to follow instructions with ...">OpenAI</a>)</p>
</li>
<li>
<p><strong>強化學習與人類偏好（RLHF / DPO / Rule-based rewards 等）會把價值觀／風格「鎖定」</strong><br>
用人類對回覆的偏好（或自動規則）做 reward，讓模型偏向「更安全」「更有禮」「不那麼煽情」或其它設計的行為。OpenAI 有 RLHF 與 rule-based rewards 的實務做法，Anthropic 用的 Constitutional AI / character training 也會塑造模型的性格特質。這些步驟直接形塑了模型看起來的「個性」。(<a href="https://cdn.openai.com/papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf?utm_source=chatgpt.com" title="Training language models to follow instructions with ...">OpenAI</a>)</p>
</li>
<li>
<p><strong>專門的 character / alignment 訓練會讓同一模型產生穩定的「風格」</strong><br>
Anthropic 的「character training / constitution」就是把某些價值與風格以文件化方式灌進去，讓模型在回應時表現出可預期的特質（例如比較溫和、謹慎或偏向思辨）。(<a href="https://www.anthropic.com/research/claude-character?utm_source=chatgpt.com" title="Claude's Character">Anthropic</a>)</p>
</li>
<li>
<p><strong>部署參數與推理設定會放大或收斂風格差異</strong><br>
同一模型在不同服務上呼叫時，會有不同的溫度（temperature）、top_p、max_tokens、system prompt、預設 safety filters、以及額外的後處理規則，這些都會改變回覆的「活潑度／嚴謹度／簡短度」，也就是常說的「個性差異」。(<a href="https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design?utm_source=chatgpt.com" title="Introduction to prompting | Generative AI on Vertex AI">Google Cloud</a>)</p>
</li>
</ol>
<hr>
<h1 id="簡單比喻（幫記憶）">簡單比喻（幫記憶）</h1>
<ul>
<li>預訓練資料像「一個人的成長環境」；</li>
<li>instruction tuning / RLHF / constitution 像「教育與品格塑造」；</li>
<li>推理參數像「當下情緒（喝咖啡還是喝酒）」。</li>
</ul>
<hr>
<h1 id="實務建議：要讓同一個角色在多個服務上演得一致，該怎麼做（checklist）">實務建議：要讓同一個角色在多個服務上演得一致，該怎麼做（Checklist）</h1>
<p>下面給你能直接放到角色卡 / system prompt 的項目（越具體越能對齊多模型）：</p>
<ol>
<li>
<p><strong>統一 system prompt（角色大綱）</strong></p>
<ul>
<li>一段固定的 system prompt，包含：角色核心特質（3~5 句）、常用句式、禁用事項、回覆格式（旁白/動作/對白/心聲）範例。</li>
<li>範例放在每個呼叫前（或放到 Knowledge/context），每個平台都用同一份。</li>
</ul>
</li>
<li>
<p><strong>數值化行為限制</strong>（避免模糊詞）</p>
<ul>
<li>回應長度（例如：每次 6~12 行）</li>
<li>幽默頻率（例如：3 次回應內最多 1 次幽默）</li>
<li>情緒強度上限（例如：1<sub>3，同時用例句定義1</sub>3分別是什麼程度）</li>
<li>禁止事項黑名單（不可使用詩歌體、過度網路梗、暴力語等）<br>
這類數字指令能讓 RLHF 有差異的模型更容易收斂到同一行為範圍。</li>
</ul>
</li>
<li>
<p><strong>固定格式 + 範例（few-shot）</strong></p>
<ul>
<li>在 prompt 裡放 1~3 個示範回應（不同情緒的例子），示範「正確的演出」與「錯誤的演出」。few-shot 可以大量降低模型自由發揮的變異。</li>
</ul>
</li>
<li>
<p><strong>規定推理參數建議（每個平台都要試）</strong></p>
<ul>
<li>建議溫度（temperature）低一點：0.2–0.5（降低生成隨機性）。</li>
<li>top_p 可搭配 0.8–1。</li>
<li>設定合理的 max_tokens 與 stop sequences，避免模型超長發揮。<br>
這能把產出從「創作型」拉回到「穩定型」。</li>
</ul>
</li>
<li>
<p><strong>一致的後處理檢查（client/server 端）</strong></p>
<ul>
<li>用簡單 rule 檢查（格式正確、字數範圍、黑名單、不允許的大幅情緒爆發），若違規就重用短 prompt 要求重寫。</li>
<li>這在不同供應商上都適用，能把極端輸出攔下。</li>
</ul>
</li>
<li>
<p><strong>版本化 A/B 測試</strong></p>
<ul>
<li>定期用同一組測試 prompt 在各平台跑（相同的 system prompt + few-shot + input）。收集差異樣本，形成「差異指標」做微調或在 prompt 加強指示。</li>
</ul>
</li>
<li>
<p><strong>提供一段短的「演出守則」給玩家/其他開發者</strong></p>
<ul>
<li>簡短版（1 段）放在角色卡前面，讓不熟悉的人直接貼就能上線（例如：「回應結構：旁白→動作→對白→心聲；避免詩歌體」）。</li>
</ul>
</li>
</ol>
<hr>
<h1 id="小範例：可直接貼進-system-prompt（短版）">小範例：可直接貼進 system prompt（短版）</h1>
<pre><code>你要扮演OOO。核心：{角色個性}。回應格式固定：旁白(1行)、動作(至少1句)、對白(至少2句)、心聲(1句)。每次回應總長 6~12 行；情緒強度 ≤ 3（情緒強度範圍為1-5 級）。禁止詩歌體、長篇小說式旁白、過度網路迷因或粗俗語。若任何回覆違反上述，請簡短重寫以符合規則。
</code></pre>
<hr>
<h1 id="參考資料">參考資料</h1>
<ul>
<li>OpenAI：instruction tuning / RLHF 文獻與系統說明（說明為何調教會改變行為）。(<a href="https://cdn.openai.com/papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf?utm_source=chatgpt.com" title="Training language models to follow instructions with ...">OpenAI</a>)</li>
<li>OpenAI：Rule-Based Rewards 與安全機制，說明 alignment pipeline 中可加入的明確規則。(<a href="https://openai.com/index/improving-model-safety-behavior-with-rule-based-rewards/?utm_source=chatgpt.com" title="Improving Model Safety Behavior with Rule-Based Rewards">OpenAI</a>)</li>
<li>Anthropic：Constitutional AI 與 character training（把價值/性格用文件化方式注入模型）。(<a href="https://www.anthropic.com/news/claudes-constitution?utm_source=chatgpt.com" title="Claude's Constitution">Anthropic</a>)</li>
<li>Google Vertex：關於微調（tuning）與部署參數對模型行為的影響。(<a href="https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models?utm_source=chatgpt.com" title="Introduction to tuning | Generative AI on Vertex AI">Google Cloud</a>)</li>
</ul>
<hr>

