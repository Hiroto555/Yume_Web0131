# お手本サイト画像・デザイン分析メモ

## 1. このメモの目的

このメモは、住宅情報館系のお手本サイトを画像・デザイン面から分解し、ゆめハウス側の再制作やAI画像生成に使える判断材料として残すためのものです。

単に「きれい」「古い」と評価するのではなく、どの画像がどの役割を担い、どの順番で信頼感・地域感・問い合わせ導線を作っているかを整理します。

## 2. 分析対象

- 参照URL: `http://127.0.0.1:8125/www.jyuutakujyouhoukan.com/index.html`
- ローカル素材フォルダ: `reference-sites/jyuutakujyouhoukan-full-2026-05-21/www.jyuutakujyouhoukan.com`
- ブラウザ抽出データ: `/tmp/reference-design-analysis/browser-visual-data.json`
- 主要画像一覧シート: `/tmp/reference-design-analysis/reference-core-image-contact-sheet.jpg`

## 3. 結論

このサイトが視覚的に強く見える理由は、個々の写真が特別に高級だからではありません。

一番大きい理由は、画像の役割分担が明確なことです。

1. ファーストビューで地域の空撮を大きく使う
2. 白い大きなコピーで「地域の不動産会社」感を作る
3. 黒い短文コピーで売主・買主をつなぐ会社の意味を補足する
4. 直後に大きい売却バナーを置いて行動導線を作る
5. 物件写真は下層で「実在感」として見せる
6. 相談・スタッフ写真は「人に相談できる安心感」のために使う
7. オレンジのCTAを繰り返して、どこを押せばいいかを迷わせない

つまり、画像を「飾り」として置いているのではなく、地域感、信頼感、行動導線、実在感を順番に作っています。

## 4. 主要画像の役割分担

### 4.1 ファーストビュー

- `wp-content/themes/jyuutakujyouhoukan/img/top/mainvisual.jpg`
- サイズ: `2800x1040`
- ブラウザ表示: 約 `1280x475`

特徴:

- 街・川・港・ランドマークが入った横長の地域景観
- 上部に広い青空があり、白いコピーを載せやすい
- 物件そのものではなく「この地域の会社」という印象を先に作る
- 彩度が高く、青と水色が強いので第一印象が明るい

ゆめハウスへの示唆:

- ヒーロー画像は、家の外観単体よりも「熊本の街・住宅地・川・道路・空」を広く見せる方が良い
- AI生成するなら、PC用は `2800x1040` 前後の超横長、スマホ用は `1280x1300` 前後の縦寄り構図で別生成または別トリミングする
- 文字を入れる予定の場所に空や余白を確保する

### 4.2 ヒーローコピー画像

- `maincatch.png`: `1598x248`
- `maincatch_02.png`: `620x236`

特徴:

- テキスト自体を画像化している
- 大きな白い明朝系コピーで、柔らかく地域密着感を出している
- 補足コピーは黒帯に白文字で、背景写真に負けない

注意:

- SEOや保守性としては、テキスト画像は現代的には弱い
- ただし、見た目の一体感は出しやすい

ゆめハウスへの示唆:

- 実装ではHTMLテキストで作る方がよい
- ただし見た目は、白い明朝系の大きなコピーと、黒帯の補足コピーを参考にできる

### 4.3 売却・購入バナー

- `bnr_top_03.png`: `2155x361`
- `bnr_bg_01.jpg`: `2155x337`
- `bnr_top_01.jpg`: `900x180`
- `bnr_top_02.jpg`: `900x180`

特徴:

- 横長で、情報量を絞った大きな導線になっている
- 右端に丸い矢印ボタンがあり、クリック先が明確
- イラスト線画・街並み・空などを背景に使い、文字が読みやすい
- 売却系は青・白・赤の組み合わせ、CTAはオレンジで強調

ゆめハウスへの示唆:

- トップ直下に「売却相談」「物件を探す」「住宅ローン相談」などの大きな横長バナーを置くと不動産サイトらしさが強くなる
- AI生成では背景写真そのものより、文字を載せやすい薄い背景・線画・住宅地イメージを作る方が使いやすい

### 4.4 物件写真

主な表示:

- ブラウザ上では物件カード画像が約 `280x220`
- 元画像は `1024x768`, `800x600`, `1477x1108` など、ほぼ4:3系

特徴:

- 正直、写真自体は高級でも洗練でもない
- 土地、住宅外観、現地写真などのリアルな記録写真が中心
- ただし、それが「実際に物件を扱っている会社」という説得力を作っている

ゆめハウスへの示唆:

- 物件カードには、過度に美しすぎるAI住宅写真を入れすぎない方がよい
- 実在感が必要なので、普通の住宅地、土地、道路、外観、現地確認っぽい写真が向いている
- 物件画像は4:3で統一すると、カード一覧が整いやすい

### 4.5 相談・説明系画像

- `top_img_01.jpg`: `630x420`
- `reason_img_03.jpg`: 相談風景
- `reason_img_04.jpg`: 図面・打ち合わせ風景
- `staff_img_00.jpg`: `920x400`

特徴:

- 物件ではなく「相談」「検討」「手続き」を表す写真
- 人物写真は清潔なオフィス、机、ノートPC、資料で構成されている
- 表情や実名よりも、相談できる雰囲気を作る役割が大きい

ゆめハウスへの示唆:

- 店内写真がまだなくても、相談シーン風の画像は使える
- ただしAI生成の場合、手や顔が不自然になりやすいので、人物を小さめ・後ろ姿・横顔寄りにする方が安全
- 図面、鍵、ノート、電卓、住宅模型などの小物写真はAI生成と相性が良い

## 5. デザイン面の強さ

### 5.1 色

中心色:

- 青・水色: 地域景観、空、清潔感
- オレンジ: CTA、問い合わせ、売却相談
- 黒: 補足コピー、信頼感、締まり
- 薄いグレー: セクション背景、余白の整理

この色設計により、画面全体は明るいが、行動ボタンだけはかなり目立ちます。

### 5.2 余白とサイズ

- ファーストビュー画像を画面幅いっぱいに使う
- その直後に大きなバナーを置く
- セクションごとに十分な上下余白を取る
- 物件カードは小さく整理し、主役にしすぎない

「大きく見せる場所」と「一覧で整理する場所」が分かれているため、古い実装でも見た目が安定しています。

### 5.3 書体

- 大見出しは明朝・セリフ系で柔らかい信頼感
- 本文やナビはゴシック系で読みやすい
- 英字や装飾タイトルは控えめ

ゆめハウス側でも、見出しだけ少し明朝寄りにして、本文・ボタンは読みやすいゴシックにするのが相性良いです。

## 6. ゆめハウスでAI生成すべき画像セット

優先度順:

1. トップPCヒーロー: `2800x1040` 前後。熊本の街・川・住宅地・青空。文字を置ける余白あり。
2. トップスマホヒーロー: `1280x1300` 前後。同じ世界観で縦構図。上部に空、下部に街。
3. 売却相談バナー背景: 横長。住宅地・線画・書類・街並み。文字なし。
4. 物件検索バナー背景: 横長。住宅街・戸建て・道路。文字なし。
5. 相談シーン: オフィス、図面、ノートPC、鍵、住宅資料。人物は小さめ。
6. 物件カード用ダミー: 普通の日本の住宅、土地、道路、マンション外観を4:3で複数。
7. 下層ページ用ヘッダー: 地域景観または住宅街の薄い背景。文字なし。

## 7. AI画像生成時の禁止条件

生成AI感を避けるため、以下は避けるべきです。

- 画像内の文字、看板、ロゴ
- 不自然な漢字や英字
- 高級住宅・豪邸・海外郊外風
- 夕焼け、夜景、映画風の過剰なライティング
- 過度なボケ、過度なレンズフレア
- 人物の手や顔が大きく写る構図
- 不自然な窓、歪んだ屋根、ありえない道路
- 使い回し感の強いイラスト調・CG調

## 8. 推奨プロンプト方針

### ヒーロー画像

```text
Realistic documentary-style wide panoramic photo for a Japanese local real estate website, Kumamoto city residential area and river under clear blue sky, calm daytime, natural colors, large clean sky area for website headline, ordinary Japanese homes and low-rise cityscape, no text, no logo, no people, no luxury mansion, no CGI, no dramatic lighting, 2800x1040 composition
```

### スマホヒーロー

```text
Realistic vertical crop for a Japanese local real estate website, Kumamoto residential cityscape with river and blue sky, generous sky space at top, city and homes in lower half, calm daytime, natural documentary photo, no text, no logo, no people, no distorted buildings, 1280x1300 composition
```

### 相談シーン

```text
Realistic Japanese real estate consultation desk, house floor plan, keys, laptop, documents, calculator, bright clean office, people only partially visible from side or back, trustworthy local agency atmosphere, no readable text, no logo, natural daylight, documentary style
```

### 物件カード

```text
Realistic ordinary Japanese residential property photo, detached house or vacant land in a suburban neighborhood, daytime, natural colors, practical real estate listing photo, no text, no logo, no luxury, no dramatic lighting, 4:3 aspect ratio
```

## 9. 重要な判断

お手本を真似るなら、画像を1枚だけ差し替えても足りません。

必要なのは、以下のような画像設計です。

- トップは地域景観
- 直下は行動バナー
- 物件一覧は実在感
- 理由・流れ・相談は説明用写真
- 会社・スタッフは安心感
- CTAはオレンジで統一

この役割分担を守ると、AI生成画像でもかなり不動産サイトらしくできます。

## 10. 次に読むべきファイル

- `reference-sites/jyuutakujyouhoukan-full-2026-05-21/www.jyuutakujyouhoukan.com/index.html`
- `reference-sites/jyuutakujyouhoukan-full-2026-05-21/www.jyuutakujyouhoukan.com/wp-content/themes/jyuutakujyouhoukan/css/common.css`
- `docs/codex-memos/2026-05-21-reference-site-analysis.md`
- `docs/codex-memos/2026-05-21-yume-house-reference-like-photo-tuning.md`

## 11. 次の実装方針

次にやるなら、先にAI生成の画像リストを固定し、トップから順に差し替えるのが良いです。

おすすめの順番:

1. PC/スマホのヒーロー画像を作る
2. ヒーロー上のコピーと黒帯コピーを調整する
3. トップ直下に売却・検索・ローン相談の横長バナーを作る
4. 物件カード用の4:3画像を複数作る
5. 相談・理由・流れセクションの説明写真を入れる
6. 全ページの下層ヘッダー画像を統一する

ここまでやると、現在のゆめハウスサイトの「ちゃちさ」はかなり消せるはずです。
