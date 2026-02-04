# Nagaoka/site/index.html 画像精査（2026-01-31）

対象: `Nagaoka/site/index.html`（トップページ）

取得方法（確実に漏れなくするため）:
- HTMLの `<img src>` + CSSの `background-image` 等を、実ブラウザで全スクロールして収集（遅延読み込みも含む）
- 追加で、slickの読み込み状態で一瞬使われる `ajax-loader.gif` も含めています

## サマリー
- 画像ファイル数（ローカル）: **32**
- 画像形式内訳: `.gif` 2, `.jpg` 10, `.png` 13, `.svg` 7
- 種別内訳: **SEC06（アイコン）** 4, **UI（lightboxプラグイン）** 4, **SEC02（理由/説明写真）** 3, **SEC04（背景/装飾）** 3, **コンテンツ（実績/写真）** 2, **コンテンツ（お客様アイコン）** 2, **MV（ヒーロー写真）** 2, **背景（共通）** 2, **CV装飾（MV追加）** 2, **SEC01（装飾SVG）** 2, **フロー装飾（共通）** 2, **ロゴ（ヘッダー）** 1, **ロゴ（フッター）** 1, **SEC03（装飾）** 1, **UI（slick読み込み中）** 1

※ 1×1のdata URI（透明GIF）も読み込まれますが、ファイルではないので表から除外しています。

## 画像一覧（用途/容量/参照箇所）

| 種別 | BP | パス | 形式 | サイズ | 画像サイズ | 参照 | 備考 | 描写 |
|---|---|---|---|---:|---:|---|---|---|
| コンテンツ（実績/写真） | PC/SP | `wp-content/uploads/2025/01/DSC_0001-scaled.jpg` | `image/jpeg` | 363.5 KB | 2560×1702 | `Nagaoka/site/index.html:598,629` | alt: 長岡市中興野・戸建 / loading: lazy | 戸建て住宅の正面外観。玄関アプローチと階段が写り、左手に車の一部が見える（昼間）。 |
| コンテンツ（実績/写真） | PC/SP | `wp-content/uploads/2025/01/DSC_0003-scaled.jpg` | `image/jpeg` | 522.0 KB | 2560×1702 | `Nagaoka/site/index.html:601,632` | alt: 長岡市中興野・戸建 / loading: lazy | 戸建て住宅の外観を斜め下から撮影。庭木と空が入り、家全体のボリューム感が分かる（昼間）。 |
| コンテンツ（お客様アイコン） | PC/SP | `wp-content/uploads/2020/08/icon02.png` | `image/png` | 2.4 KB | 160×160 | `Nagaoka/site/index.html:497` | alt: お客様アイコン（50代男性） / loading: lazy | 丸枠の中に人物シルエット（短髪風）の線画アイコン。 |
| コンテンツ（お客様アイコン） | PC/SP | `wp-content/uploads/2020/08/icon05.png` | `image/png` | 2.7 KB | 160×160 | `Nagaoka/site/index.html:566` | alt: お客様アイコン（70代女性） / loading: lazy | 丸枠の中に人物シルエット（長髪風）の線画アイコン。 |
| MV（ヒーロー写真） | PC/SP | `wp-content/themes/glandmarket/img/top/mv/slide_img01.jpg` | `image/jpeg` | 312.2 KB | 1960×840 | `Nagaoka/site/index.html:254` | alt: あなたの所有する不動産、どこよりも高く買い取ります。 | 青空と住宅街の写真に、キャッチコピーと実績数字（円形バッジ）・対応エリアを重ねたヒーロー用ビジュアル。 |
| MV（ヒーロー写真） | SP | `wp-content/themes/glandmarket/img/top/mv/slide_img01_sp.jpg` | `image/jpeg` | 410.1 KB | 1280×1600 | `Nagaoka/site/index.html:256` | alt: あなたの所有する不動産、どこよりも高く買い取ります。 | ヒーロー画像のスマホ縦長版。住宅街＋キャッチコピー＋実績数字バッジ＋対応エリア表記の構成。 |
| SEC02（理由/説明写真） | PC/SP | `wp-content/themes/glandmarket/img/top/sec02/sec02_img01.jpg` | `image/jpeg` | 77.3 KB | 660×300 | `Nagaoka/site/index.html:328` | alt: 不動産の目利き力 / loading: lazy | 模型の家を虫眼鏡で覗くイメージ（査定/目利きの象徴）。背景は緑のボケ。 |
| SEC02（理由/説明写真） | PC/SP | `wp-content/themes/glandmarket/img/top/sec02/sec02_img02.jpg` | `image/jpeg` | 104.8 KB | 660×300 | `Nagaoka/site/index.html:337` | alt: 卓越した企画・商品力 / loading: lazy | テーブル上で写真資料とカラースウォッチ等を見ながら打ち合わせしている手元。 |
| SEC02（理由/説明写真） | PC/SP | `wp-content/themes/glandmarket/img/top/sec02/sec02_img03.jpg` | `image/jpeg` | 77.8 KB | 660×300 | `Nagaoka/site/index.html:346` | alt: 地元金融機関様とのファイナンス協力 | 机上の書類や小物を背景に握手しているビジネスシーン（信頼/契約の象徴）。 |
| ロゴ（ヘッダー） | PC/SP | `wp-content/themes/glandmarket/img/common/hd_logo.svg` | `image/svg+xml` | 52.0 KB | 273.100×60.700 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:15030,15233` | - | ロゴ。地域の形状を思わせるシルエット＋サイト名（日本語）の組み合わせ。 |
| ロゴ（フッター） | PC/SP | `wp-content/themes/glandmarket/img/common/ft_logo.svg` | `image/svg+xml` | 52.0 KB | 273.100×60.700 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:15942` | - | フッター用ロゴ（ヘッダーロゴと同系）。地域シルエット＋サイト名の組み合わせ。 |
| 背景（共通） | PC/SP | `wp-content/themes/glandmarket/img/common/bg/bg01.jpg` | `image/jpeg` | 111.9 KB | 1400×920 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17365` | - | 白〜グレーのぼかし背景（抽象的な質感）。セクション背景として薄く敷く用途。 |
| 背景（共通） | PC/SP | `wp-content/themes/glandmarket/img/common/bg/bg02.jpg` | `image/jpeg` | 136.7 KB | 1400×1110 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17771` | - | 白〜薄いブルー寄りのぼかし背景（抽象的な質感）。セクション背景として薄く敷く用途。 |
| CV装飾（MV追加） | PC | `wp-content/themes/glandmarket/img/top/cv/mv_add_pc.png` | `image/png` | 270.1 KB | 1288×310 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17028` | - | 「私たちが査定にお伺いします」の文字と、スタッフ集合写真を右側に配置した横長バナー（PC向け）。 |
| CV装飾（MV追加） | SP | `wp-content/themes/glandmarket/img/top/cv/mv_add_sp.png` | `image/png` | 151.4 KB | 1089×220 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17040` | - | 「私たちが査定にお伺いします」の文字とスタッフ写真の横長バナー（SP向けのサイズ/トリミング）。 |
| SEC01（装飾SVG） | PC/SP | `wp-content/themes/glandmarket/img/top/sec01/professional.svg` | `image/svg+xml` | 11.8 KB | 1079.460×111.580 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17350` | - | 背景装飾の文字アート（薄い英字「We are professional」系の大きな見出しを透かしで敷く）。 |
| SEC01（装飾SVG） | PC/SP | `wp-content/themes/glandmarket/img/top/sec01/sec01_img01.svg` | `image/svg+xml` | 198.4 KB | 630×347 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17419` | - | 見出し用の装飾SVG。金色系の文字と罫線、地域シルエットなどでタイトル周りを演出。 |
| SEC03（装飾） | PC/SP | `wp-content/themes/glandmarket/img/top/sec03/before.png` | `image/png` | 113.5 KB | 960×480 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17517` | - | スーツ姿の胸元（手を胸に当てる）＋ミニチュアの建物群を並べた合成イメージ（誠実さ/専門性の象徴）。 |
| SEC04（背景/装飾） | PC/SP | `wp-content/themes/glandmarket/img/top/sec04/bg.jpg` | `image/jpeg` | 105.6 KB | 1400×800 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17540` | - | ノートPCでビデオ通話しているシーン（オンライン相談のイメージ）。 |
| SEC04（背景/装飾） | PC/SP | `wp-content/themes/glandmarket/img/top/sec04/fukidashi.png` | `image/png` | 11.8 KB | 922×244 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17745` | - | 濃紺の吹き出しラベル。「オンライン相談も受付中！」の文字入り。 |
| SEC04（背景/装飾） | PC/SP | `wp-content/themes/glandmarket/img/top/sec04/online.svg` | `image/svg+xml` | 4.0 KB | 282.710×70.260 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:17562` | - | 背景装飾の文字アート（薄い英字「Online」系の大きな透かし文字）。 |
| SEC06（アイコン） | PC/SP | `wp-content/themes/glandmarket/img/top/sec06/sec06_icon01.png` | `image/png` | 2.3 KB | 80×80 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:16512` | - | 丸枠の家/建物アイコン（線画）。 |
| SEC06（アイコン） | PC/SP | `wp-content/themes/glandmarket/img/top/sec06/sec06_icon02.png` | `image/png` | 2.2 KB | 80×80 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:16515` | - | 丸枠の配送/スピード感のあるアイコン（線画）。 |
| SEC06（アイコン） | PC/SP | `wp-content/themes/glandmarket/img/top/sec06/sec06_icon03.png` | `image/png` | 2.3 KB | 80×80 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:16518` | - | 丸枠の書類＋ペン（契約/手続き）アイコン（線画）。 |
| SEC06（アイコン） | PC/SP | `wp-content/themes/glandmarket/img/top/sec06/sec06_icon04.png` | `image/png` | 2.7 KB | 80×80 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:16521` | - | 丸枠の虫眼鏡＋書類/家（調査/査定）アイコン（線画）。 |
| フロー装飾（共通） | PC/SP | `wp-content/themes/glandmarket/img/common/flow/flow_before.svg` | `image/svg+xml` | 36.5 KB | 273.800×77.700 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:18579` | - | フロー周りの装飾。金色のコの字罫線＋注意書き（「査定ご報告まで[平均3日]程度」「即日・翌日回答も可能」など）。 |
| フロー装飾（共通） | SP | `wp-content/themes/glandmarket/img/common/flow/flow_before_sp.svg` | `image/svg+xml` | 34.0 KB | 273.800×40.800 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:18621` | - | 上記フロー装飾のスマホ版（縦寸法が短い）。 |
| UI（lightboxプラグイン） | PC/SP | `wp-content/themes/glandmarket/img/plugin/lightbox/close.png` | `image/png` | 280 B | 27×27 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:11640,11820` | - | ライトボックスの閉じるボタン（×）。 |
| UI（lightboxプラグイン） | PC/SP | `wp-content/themes/glandmarket/img/plugin/lightbox/loading.gif` | `image/gif` | 8.3 KB | 32×32 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:11640,11715` | - | ライトボックスの読み込み中スピナー。 |
| UI（lightboxプラグイン） | PC/SP | `wp-content/themes/glandmarket/img/plugin/lightbox/next.png` | `image/png` | 1.3 KB | 50×45 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:11640,11762` | - | ライトボックスの次へボタン（右矢印）。 |
| UI（lightboxプラグイン） | PC/SP | `wp-content/themes/glandmarket/img/plugin/lightbox/prev.png` | `image/png` | 1.3 KB | 50×45 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:11640,11746` | - | ライトボックスの前へボタン（左矢印）。 |
| UI（slick読み込み中） | PC/SP | `wp-content/themes/glandmarket/css/ajax-loader.gif` | `image/gif` | 4.1 KB | 32×32 | `Nagaoka/site/wp-content/themes/glandmarket/css/common.css:11837` | - | スライダー等の読み込み中スピナー（小さな回転アイコン）。 |

## data URI（ファイルではないが読み込まれるもの）
- `data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==`（1×1の透明GIF）

