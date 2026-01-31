覚えてます。いまのゴールはこれですよね：

* **WordPress（Astra＋Astra Child）を“配信用の箱”にする**
* **ローカル（PCのPreview）で見えるHTML/CSS/JSを、そのままWordPressでも同じ見た目で出す**
* テーマの見た目（ヘッダー/フッター/余計なCSS）には **できるだけ影響されない**ようにしたい

その発想なら、結論はこうです：

✅ **Astra Child のフォルダの中に、あなたのローカルサイト一式（HTML/CSS/JS/画像）を同梱してOK**
✅ そして **「固定ページに割り当てる専用テンプレ（PHP）1枚」**を子テーマに入れて、そこから静的HTMLを“読み込んでそのまま出す”のが一番確実です

---

# 仕組みの全体像（これで “Preview＝WP” を担保する）

* 子テーマ内に `assets/site/` を作る
  → ここにローカルサイトの成果物（`index.html`, `css/`, `js/`, `img/`）を丸ごと置く
* 子テーマ内に **ページテンプレ**を1枚作る
  → **WPのスラッグ**に応じて `assets/site/{slug}.html` を出す
  → フロントページだけ `index.html` を出す

こうすると、WordPressは「URLの箱」になるので、ローカルと一致しやすいです。

---

# 1) Astra Child のフォルダ構造（おすすめ）

子テーマフォルダはこうします（このままZIPにしてアップOK）：

```
astra-child/
  style.css
  functions.php             （無くても動くけど、入れておくと後で便利）
  templates/
    tpl-static-local.php     ← これが肝
  assets/
    site/
      index.html
      about.html
      service.html
      css/
      js/
      img/
```

> ポイント：**ローカルで見ている“そのままの構造”を `assets/site/` 配下に再現**するのがコツです。

---

# 2) “テーマの影響を受けない”テンプレ（これを入れる）

`templates/tpl-static-local.php` を子テーマに追加します。

これは **Astraのheader/footerを一切呼ばず**、HTMLをそのまま返します（＝ローカル再現が最強）。

```php
<?php
/*
Template Name: Static Local（ローカル再現・テーマ無視）
*/

$page_id = get_queried_object_id();
$slug    = sanitize_title(get_post_field('post_name', $page_id));

// フロントページは index.html を返す（WP側で「このページをホームにする」設定を想定）
if (is_front_page() || $slug === 'home') {
  $slug = 'index';
}

// ローカル成果物の置き場
$base_dir = trailingslashit(get_stylesheet_directory()) . 'assets/site/';
$file     = $base_dir . $slug . '.html';

if (!file_exists($file)) {
  status_header(404);
  header('Content-Type: text/html; charset=UTF-8');
  echo "<h1>404</h1><p>HTML not found: <code>" . htmlspecialchars($slug . '.html', ENT_QUOTES, 'UTF-8') . "</code></p>";
  exit;
}

$html = file_get_contents($file);

// 相対パスの css/js/img を assets/site/ に向ける（超重要）
$base_href = trailingslashit(get_stylesheet_directory_uri()) . 'assets/site/';

// <head>直後に <base> を差し込む（headが無いHTMLならそのまま）
if (stripos($html, '<head') !== false) {
  $html = preg_replace(
    '/<head(\b[^>]*)>/i',
    '<head$1><base href="' . htmlspecialchars($base_href, ENT_QUOTES, 'UTF-8') . '">',
    $html,
    1
  );
}

header('Content-Type: text/html; charset=UTF-8');
echo $html;
exit;
```

### これで何が解決する？

* AstraのCSS/JS、ヘッダー/フッターが **一切混ざらない**
* HTMLが `css/style.css` のような相対パスでも、`<base>`のおかげで
  `…/wp-content/themes/あなたの子テーマ/assets/site/css/style.css` に解決される

> 注意：ローカルHTMLが `/css/style.css` みたいな **先頭がスラッシュの“ルート相対”**を多用してる場合は、そのままだと合いません。
> その場合は **相対パスに寄せる（`css/style.css`）**か、Codexに一括置換させるのが早いです。

---

# 3) WordPress側でやること（超少ない）

1. **固定ページ**を作る（例：タイトル「About」スラッグ `about`）
2. 右側の **テンプレート**で
   **「Static Local（ローカル再現・テーマ無視）」** を選ぶ
3. 公開 → 表示
   → `assets/site/about.html` がそのまま出ます

ホームも同じで、

* 「Home」ページを作る（スラッグ `home` とか）
* そのページにテンプレ割当
* **設定 → 表示設定 → ホームページの表示 → 固定ページ**で Home を指定
  → `assets/site/index.html` がトップに出ます（テンプレで `index` に寄せてるため）

---

# 4) 「ZIPでアップしてOK？」への答え

はい、OKです。やり方は：

* Astra Child generatorでZIPを作る
* PCで解凍して、上の `templates/` と `assets/site/` を追加
* **“子テーマフォルダごと”**ZIPにし直す
* WordPressの **外観 → テーマ → 新規追加 → テーマのアップロード**で入れる

注意点は1つだけ：

* ZIPの中身が `astra-child/style.css ...` みたいに **フォルダから始まる形**になってる必要があります
  （中身だけを直ZIPにすると失敗しやすい）

そして、ローカルサイトが大きい場合：

* WordPressのアップロード上限に引っかかることがあります
  → その時は **Xserverのファイルマネージャ / SFTP** で `wp-content/themes/` に直接アップが確実です

---

# 5) これをCodexにやらせたい：どう伝える？

Codexに任せるのはめちゃくちゃ相性いいです。
Codexは **ローカルのディレクトリを読んで、編集して、コマンドも実行できる**ので、子テーマの組み立て作業を丸ごとやらせられます。 ([developers.openai.com][1])

## Codexの使い方（CLI）

* インストール：`npm i -g @openai/codex`
* 起動：`codex`（初回はサインインが出ます） ([developers.openai.com][1])

> Codex CLIは「選んだディレクトリ内のコードを読んで、変更して、実行できる」前提の道具です。 ([developers.openai.com][1])

## Codexに“ルール”を覚えさせる方法（超おすすめ）

リポジトリに `AGENTS.md` を置くと、Codexがその指示に従いやすくなります。 ([openai.com][2])

---

# 6) そのままコピペで使える「Codexへの指示文」

これをCodexに貼れば、あなたの子テーマ構築をほぼ自動化できます。

> **Codex用プロンプト（コピペ用）**

```text
目的：
ローカルでプレビューできている静的Webサイト（HTML/CSS/JS）を、WordPressのAstra子テーマに同梱して配信したい。
WordPressは「配信用の箱」として使い、Astraのヘッダー/フッター/スタイルの影響を受けずに、ローカルと同じ見た目で表示させたい。

手元の構成：
- ./local_site/ にローカルサイトの成果物（index.html, css/, js/, img/ など）がある想定
- ./astra-child/ に Astra Child Theme Generator で作った子テーマ雛形がある想定

やってほしいこと：
1) astra-child/ の中に以下を作成
   - templates/tpl-static-local.php
     - WordPress固定ページテンプレとして動作
     - get_header/get_footer は呼ばない（Astraの影響を排除）
     - ページのスラッグに応じて assets/site/{slug}.html を読み込み、そのまま返す
     - フロントページ(or slug=home)は assets/site/index.html を返す
     - <head>直後に <base href="{child_theme_uri}/assets/site/"> を挿入して、相対パスのCSS/JS/画像が解決できるようにする
     - path traversal対策として slug は sanitize_title 相当で安全化する
     - ファイルが無い場合は 404 を返す

2) astra-child/assets/site/ を作成し、local_site/ の中身を同じ構造でコピーする

3) README.md を追加し、WordPress側で
   - 固定ページを作ってテンプレを割り当てる手順
   - ホームページ表示設定でHomeページをトップにする手順
   を書く

4) 可能なら、astra-child をZIP化する手順（またはスクリプト）も用意

受け入れ条件：
- dev環境のWordPressでテンプレを割り当てたページを開くと、ローカルのHTMLと同じ見た目になる
- Astraのヘッダー/フッターが出ない
```

---

## 最短の次アクション（おすすめ）

1. ローカルサイトの「成果物フォルダ」（プレビューしているやつ）を `local_site/` として用意
2. Astra child雛形を `astra-child/` に展開
3. Codexをそのディレクトリで起動して、上のプロンプトを投げる ([developers.openai.com][1])
4. 完成した `astra-child` をZIPしてWPにアップ → devで確認

---

もしローカルが **Vite/React/Nextの“ビルド成果物（dist）”型**なら、テンプレ設計がさらに最適化できる（manifest読む等）ので、ローカルの構成だけ一言でいいので教えて。
（例：「ただのHTML」「Viteでdistが出る」「Nextでoutが出る」など）

[1]: https://developers.openai.com/codex/cli/ "Codex CLI"
[2]: https://openai.com/index/introducing-codex/ "Introducing Codex | OpenAI"
