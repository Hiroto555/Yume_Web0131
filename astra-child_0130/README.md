# astra-child_0130（Static Local 配信）

この子テーマは **WordPress（Astra）を“配信用の箱”として使い**、`assets/site/` に同梱した静的HTMLを **ほぼそのまま** 表示するためのものです。

## 目的

- ローカルでプレビューできているHTML/CSS/画像構成を、WordPress上でも同じ見た目で出す
- Astra のヘッダー/フッター/スタイルの影響を受けない（テンプレ内で `get_header/get_footer/wp_head/wp_footer` を呼びません）
- 既存の `code.html` は編集せず、出力時にだけリンクをWordPress側URLへ差し替えます

## 使い方（WordPress側）

1. **Astra** を親テーマとしてインストールして有効化
2. この子テーマ `astra-child_0130` をアップロードして有効化
3. 固定ページを下記のスラッグで作成し、テンプレートに **「Static Local (Theme Ignored)」** を割り当てて公開
   - ※最近の構成では `page-{slug}.php` も同梱しているため、**テンプレート選択をしなくても表示は成立**します（「デフォルトテンプレート」のままでもOK）

| Page Slug | 表示するHTML |
| --- | --- |
| `home` | `assets/site/1._home/code.html` |
| `property-search` | `assets/site/2._property_search/code.html` |
| `property-details` | `assets/site/3._property_details/code.html` |
| `guide-flow` | `assets/site/4._guide_flow/code.html` |
| `our-strengths` | `assets/site/5._our_strengths/code.html` |
| `testimonials` | `assets/site/6._testimonials/code.html` |
| `company-info` | `assets/site/7._company_info/code.html` |
| `contact` | `assets/site/8._contact/code.html` |
| `rental-business` | `assets/site/9._rental_business/code.html` |

4. `/` を `home` と同内容にしたい場合：WordPressの **設定 → 表示設定 → ホームページの表示** で、フロントページに `home` を指定してください  
   - ※テンプレ側でも `is_front_page()` の場合は `home` 扱いで `1._home/code.html` を返します

## 静的ファイルの置き場所

- `assets/site/` 配下に、既存の `stitch_yume_site1New/` を **構造そのまま** 同梱しています
  - `1._home/code.html` など
  - `image2/`, `image3/`, `Image/` など

## ZIP化（任意）

`astra-child_0130/scripts/zip-theme.sh` を実行すると、親ディレクトリに `astra-child_0130.zip` を作成します。
