from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "astra-child_0204" / "assets" / "site"

PHONE = "096-383-2001"
ADDRESS = "〒862-0926 熊本県熊本市東区保田窪5-7-11"
VERSION = "20260521-strongblue1"
SUUMO_URL = "https://suumo.jp/ikkodate/kaisha/__JJ_JJ051FD001_arz1090z2bsz1020z2kcz1181414001.html"
ATHOME_URL = "https://www.athome.co.jp/ahks/blooo.html"

NAV = [
    ("1._home", "Home", "ホーム"),
    ("2._property_search", "Search", "物件を見る"),
    ("4._guide_flow", "Guide", "購入の流れ"),
    ("5._our_strengths", "Strength", "選ばれる理由"),
    ("6._testimonials", "Case", "相談事例"),
    ("7._company_info", "Company", "会社情報"),
    ("8._contact", "Contact", "相談する"),
]

IMAGES = {
    "home": "../estate-images/generated-20260521/selected/hero-desktop.jpg",
    "home_mobile": "../estate-images/generated-20260521/selected/hero-mobile.jpg",
    "house": "../estate-images/generated-20260521/selected/property-used-house.jpg",
    "apartment": "../estate-images/generated-20260521/selected/property-apartment.jpg",
    "land": "../estate-images/generated-20260521/selected/property-vacant-land.jpg",
    "street": "../estate-images/generated-20260521/selected/property-narrow-street.jpg",
    "parking_generated": "../estate-images/generated-20260521/selected/property-parking.jpg",
    "older_house": "../estate-images/generated-20260521/selected/property-older-house.jpg",
    "living": "../estate-images/generated-20260521/selected/consultation-office.jpg",
    "kitchen": "../estate-images/generated-20260521/selected/keys-and-floorplan.jpg",
    "interior": "../estate-images/generated-20260521/selected/consultation-desk-close.jpg",
    "city": "../estate-images/generated-20260521/selected/hero-desktop.jpg",
    "sale_banner": "../estate-images/generated-20260521/selected/banner-sale-consultation.jpg",
    "search_banner": "../estate-images/generated-20260521/banner/regional-bg-03.jpg",
    "land_banner": "../estate-images/generated-20260521/selected/banner-land-sale.jpg",
    "loan_banner": "../estate-images/generated-20260521/selected/banner-loan-consultation.jpg",
    "regional": "../estate-images/generated-20260521/banner/regional-bg-02.jpg",
    "riverside": "../estate-images/generated-20260521/banner/regional-bg-03.jpg",
    "neighborhood": "../estate-images/generated-20260521/banner/regional-bg-04.jpg",
    "store": "../image4/hero_storefront_front_sunny.jpg",
    "store_crop": "../image4/hero_storefront_front_sunny_cropped.jpg",
    "parking": "../estate-images/generated-20260521/selected/property-parking.jpg",
    "office": "../estate-images/generated-20260521/selected/consultation-office.jpg",
    "guide": "../estate-images/generated-20260521/selected/keys-and-floorplan.jpg",
    "guide2": "../estate-images/generated-20260521/selected/banner-loan-consultation.jpg",
    "strength": "../estate-images/generated-20260521/banner/regional-bg-02.jpg",
    "consult": "../estate-images/generated-20260521/selected/consultation-desk-close.jpg",
    "garden": "../estate-images/generated-20260521/selected/property-narrow-street.jpg",
}


def e(value: str) -> str:
    return escape(value, quote=True)


def img(key: str) -> str:
    return IMAGES[key]


def page_href(slug: str) -> str:
    return f"../{slug}/code.html?v={VERSION}"


def title_lines(*parts: str) -> str:
    return "".join(f'<span class="estate-title-line">{e(part)}</span>' for part in parts)


def header(active: str) -> str:
    desktop = "\n".join(
        f'<a href="{page_href(slug)}"{" aria-current=\"page\"" if slug == active else ""}>{jp}</a>'
        for slug, _en, jp in NAV
    )
    mobile = "\n".join(
        f'<a href="{page_href(slug)}">{"● " if slug == active else ""}{jp}</a>'
        for slug, _en, jp in NAV
    )
    return f"""
    <header class="estate-header">
        <div class="estate-container estate-header__inner">
            <a class="estate-logo" href="{page_href('1._home')}" aria-label="ゆめハウス ホーム">
                <img src="../image4/yumehouse_logo_horizontal.png" alt="ゆめハウス" />
            </a>
            <nav class="estate-nav" aria-label="グローバルナビゲーション">
                {desktop}
            </nav>
            <div class="estate-header__actions">
                <a class="estate-button-light" href="tel:{PHONE}">{PHONE}</a>
                <a class="estate-button" href="{page_href('8._contact')}">無料相談</a>
            </div>
            <details class="estate-mobile-nav">
                <summary class="estate-menu-button" aria-label="メニューを開く"><span aria-hidden="true">☰</span></summary>
                <nav class="estate-mobile-nav__panel" aria-label="モバイルナビゲーション">
                    {mobile}
                    <a href="tel:{PHONE}">電話する {PHONE}</a>
                </nav>
            </details>
        </div>
    </header>
    """


def footer() -> str:
    nav1 = "\n".join(f'<a href="{page_href(slug)}">{jp}</a>' for slug, _en, jp in NAV[:4])
    nav2 = "\n".join(f'<a href="{page_href(slug)}">{jp}</a>' for slug, _en, jp in NAV[4:])
    return f"""
    <footer class="estate-footer">
        <div class="estate-container estate-footer__grid">
            <div>
                <h2>ゆめハウス</h2>
                <p>{ADDRESS}<br />TEL: {PHONE}<br />営業時間 10:00-19:00 / 定休日 火・水</p>
            </div>
            <div>
                <h3>住まい探し</h3>
                <div class="estate-list">{nav1}</div>
            </div>
            <div>
                <h3>会社・相談</h3>
                <div class="estate-list">{nav2}</div>
            </div>
            <div>
                <h3>掲載物件</h3>
                <div class="estate-list">
                    <a href="{SUUMO_URL}" target="_blank" rel="noopener noreferrer">SUUMOで見る</a>
                    <a href="{ATHOME_URL}" target="_blank" rel="noopener noreferrer">at homeで見る</a>
                    <a href="{page_href('11._privacy')}">プライバシーポリシー</a>
                </div>
            </div>
        </div>
    </footer>
    """


def hero(
    title: str,
    lead: str,
    image: str,
    kicker: str = "YUME HOUSE",
    compact: bool = False,
    mobile_image: str | None = None,
    position: str = "center",
) -> str:
    compact_class = " estate-hero--compact" if compact else ""
    mobile = mobile_image or image
    facts = "" if compact else f"""
        <div class="estate-hero__facts">
            <div class="estate-hero__fact"><span>対応エリア</span><strong>熊本市東区を中心にご提案</strong></div>
            <div class="estate-hero__fact"><span>資金計画</span><strong>月々支払い・事前審査から相談</strong></div>
            <div class="estate-hero__fact"><span>相談範囲</span><strong>購入・売却・賃貸管理まで対応</strong></div>
        </div>
    """
    return f"""
    <section class="estate-hero{compact_class}">
        <div class="estate-hero__image" style="--estate-hero-image:url('{image}');--estate-hero-image-mobile:url('{mobile}');--estate-hero-position:{position}"></div>
        <div class="estate-container estate-hero__content">
            <div class="estate-kicker">{e(kicker)}</div>
            <h1>{title}</h1>
            <div class="estate-hero__lead"><span>{lead}</span></div>
            <div class="estate-hero__buttons">
                <a class="estate-button" href="{page_href('8._contact')}">無料で相談する</a>
                <a class="estate-button-outline" href="{page_href('2._property_search')}">掲載物件を見る</a>
            </div>
        </div>
    </section>
    {facts}
    """


def image_banner(title: str, text: str, image: str, href: str, tag: str, wide: bool = False) -> str:
    wide_class = " estate-image-banner--wide" if wide else ""
    return f"""
    <a class="estate-image-banner{wide_class}" href="{href}" style="--estate-banner-image:url('{image}')">
        <span class="estate-image-banner__content">
            <span class="estate-image-banner__tag">{e(tag)}</span>
            <strong>{title}</strong>
            <span>{text}</span>
        </span>
        <span class="estate-image-banner__arrow" aria-hidden="true">→</span>
    </a>
    """


def action_banners() -> str:
    return f"""
    <section class="estate-section estate-section--banner">
        <div class="estate-container estate-image-banners">
            {image_banner("不動産売却・住み替えを相談", "査定、売却、貸す選択肢、次の購入予算まで一緒に整理します。", img("sale_banner"), page_href("9._rental_business"), "売却・管理", True)}
            {image_banner("掲載物件を見る", "SUUMO / at home の掲載物件を見ながら、月々支払いも確認できます。", img("search_banner"), page_href("2._property_search"), "物件検索")}
            {image_banner("住宅ローンから相談", "借入可能額ではなく、続けられる月々支払いから探します。", img("loan_banner"), page_href("8._contact"), "ローン相談")}
        </div>
    </section>
    """


def section(title: str, lead: str, body: str, soft: bool = False, warm: bool = False, dark: bool = False, kicker: str = "") -> str:
    cls = "estate-section"
    if soft:
        cls += " estate-section--soft"
    if warm:
        cls += " estate-section--warm"
    if dark:
        cls += " estate-section--dark"
    kicker_html = f'<div class="estate-kicker estate-kicker--section">{e(kicker)}</div>' if kicker else ""
    return f"""
    <section class="{cls}">
        <div class="estate-container">
            <div class="estate-section-head">
                <div>
                    {kicker_html}
                    <h2>{title}</h2>
                    <p>{lead}</p>
                </div>
            </div>
            {body}
        </div>
    </section>
    """


def card(title: str, text: str, image: str | None = None, tags: list[str] | None = None, href: str | None = None) -> str:
    image_html = f'<img class="estate-card__image" src="{image}" alt="" loading="lazy" />' if image else ""
    card_class = "estate-card estate-card--media" if image else "estate-card estate-card--text"
    tag_html = ""
    if tags:
        tag_html = '<div class="estate-tag-row">' + "".join(f'<span class="estate-tag">{e(tag)}</span>' for tag in tags) + "</div>"
    inner = f"""{image_html}<div class="estate-card__body"><h3>{title}</h3><p>{text}</p>{tag_html}</div>"""
    if href:
        return f'<a class="{card_class}" href="{href}">{inner}</a>'
    return f'<div class="{card_class}">{inner}</div>'


def grid(cards: list[str], cols: int = 3) -> str:
    return f'<div class="estate-grid estate-grid--{cols}">' + "\n".join(cards) + "</div>"


def steps(items: list[tuple[str, str]]) -> str:
    return '<div class="estate-steps">' + "\n".join(
        f'<div class="estate-step"><div><h3>{title}</h3><p>{text}</p></div></div>' for title, text in items
    ) + "</div>"


def faq(items: list[tuple[str, str]]) -> str:
    return '<div class="estate-faq">' + "\n".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items
    ) + "</div>"


def table(rows: list[tuple[str, str]]) -> str:
    return '<table class="estate-table"><tbody>' + "\n".join(
        f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in rows
    ) + "</tbody></table>"


def cta(title: str = "買えるか不安な段階から、無料で相談できます。", text: str = "月々支払い、校区、駐車台数、通勤距離まで。物件を決める前に、まず資金計画と条件を整理しましょう。") -> str:
    return f"""
    <section class="estate-section estate-section--dark">
        <div class="estate-container estate-band">
            <div>
                <div class="estate-kicker">無料相談</div>
                <h2>{title}</h2>
                <p>{text}</p>
                <div class="estate-actions">
                    <a class="estate-button-light" href="{page_href('8._contact')}">無料相談する</a>
                    <a class="estate-button-outline" href="tel:{PHONE}">{PHONE}</a>
                </div>
            </div>
            <img src="{img('store_crop')}" alt="ゆめハウス店舗外観" loading="lazy" />
        </div>
    </section>
    """


PROPERTY_CARDS = [
    card("熊本市東区 長嶺｜新築戸建て", "駐車2台、校区と買い物動線を重視したファミリー向け。月々支払いの目安から比較できます。", img("house"), ["4LDK", "駐車2台", "月々8万円台"], page_href("3._property_details")),
    card("熊本市中央区 水前寺｜中古マンション", "通勤、管理費、将来の売りやすさまで一緒に確認したい方へ。", img("apartment"), ["3LDK", "駅徒歩圏", "リフォーム相談可"], page_href("3._property_details")),
    card("熊本市北区 楠｜住宅用地", "建築会社が未定でも、土地選びと総予算を先に整理できます。", img("land"), ["土地", "校区相談", "建築費込み比較"], page_href("3._property_details")),
]


def home_page() -> str:
    body = hero(
        title_lines("熊本市東区で", "住まい探しの相談を。"),
        "物件、住宅ローン、校区、通勤、駐車台数まで。購入前の不安を一つずつ整理します。",
        img("store_crop"),
        "熊本市東区の不動産相談",
        mobile_image=img("store_crop"),
        position="center 48%",
    )
    body += action_banners()
    body += section(
        "ご相談内容",
        "物件探し、資金計画、売却・管理まで、今の状況に合わせて相談できます。",
        grid([
            card("掲載物件を見る", "SUUMO / at home の掲載物件へ。気になる物件は見学前に費用感も確認できます。", None, ["SUUMO", "at home"], page_href("2._property_search")),
            card("月々支払いから相談", "借入可能額、頭金、諸費用、事前審査まで整理してから探せます。", None, ["住宅ローン", "事前審査"], page_href("8._contact")),
            card("売却・賃貸管理を相談", "住み替え、査定、賃貸管理、空室対策まで同じ窓口で比較できます。", None, ["売却", "管理"], page_href("9._rental_business")),
        ], 3),
        soft=True,
        kicker="相談メニュー",
    )
    body += section("おすすめ物件", "価格だけでなく、月々支払い、周辺環境、生活条件も一緒に確認できます。", grid(PROPERTY_CARDS, 3), kicker="掲載物件")
    body += section(
        "ゆめハウスが選ばれる理由",
        "地域の生活圏と資金計画をふまえて、無理のない住まい探しをお手伝いします。",
        grid([
            card("ローンから逆算", "買える価格ではなく、続けられる月々支払いから物件候補を絞ります。", None, ["資金計画"]),
            card("熊本の生活圏で比較", "校区、駐車台数、買い物、通勤距離など、暮らしの条件で整理します。", None, ["生活圏"]),
            card("売る・貸すも同時に相談", "住み替えでは、売却・賃貸管理・購入後の支払いまで並べて見ます。", None, ["住み替え"]),
        ], 3),
        warm=True,
        kicker="選ばれる理由",
    )
    body += section(
        "購入までの流れ",
        "相談から入居までの全体像を先に見せることで、問い合わせ前の不安を減らします。",
        steps([
            ("無料相談", "家賃、貯蓄、希望エリア、校区、駐車台数を確認します。"),
            ("資金計画", "月々支払い、諸費用、頭金、事前審査の進め方を整理します。"),
            ("物件比較", "価格、立地、周辺環境、将来の売りやすさを比較します。"),
            ("内覧・申込", "気になる物件を見学し、必要な条件を確認します。"),
            ("契約・入居", "契約、ローン、引渡しまでスケジュールを管理します。"),
        ]),
        kicker="購入の流れ",
    )
    body += section(
        "相談事例",
        "実際の悩みに近い入口を用意し、自分ごと化しやすくします。",
        grid([
            card("家賃と同じくらいで買えますか？", "中央区で中古マンションを検討。諸費用と管理費込みで月々支払いを比較しました。", None, ["ローン不安"]),
            card("子どもの校区を変えずに探したい", "東区で新築戸建てを検討。校区、駐車2台、通勤時間を同時に整理しました。", None, ["ファミリー"]),
            card("戸建てを売るか貸すか迷っています", "住み替え前に、査定額、賃料、管理費、購入後の支払いを並べて判断しました。", None, ["住み替え"]),
        ], 3),
        soft=True,
        kicker="相談事例",
    )
    body += section("よくある不安", "問い合わせ前の代表的な不安を先に解消します。", faq(DEFAULT_FAQ), warm=True, kicker="よくある質問")
    body += cta()
    return body


DEFAULT_FAQ = [
    ("まだ買うと決めていなくても相談できますか？", "はい。今の家賃、貯蓄、希望条件から、買う場合と買わない場合を比較する相談としてご利用ください。"),
    ("住宅ローンに自信がありません。", "借入可能額だけでなく、無理のない月々支払い、諸費用、頭金、事前審査の進め方まで整理します。"),
    ("売却や賃貸管理も同時に相談できますか？", "はい。住み替えでは、売る、貸す、買うを同じ窓口で比較できます。"),
]


def property_search_page() -> str:
    body = hero(title_lines("掲載物件は、", "外部ポータルと", "店頭相談で", "確認できます。"), "SUUMO / at home の掲載情報を見ながら、月々支払い、諸費用、校区、駐車台数まで一緒に確認できます。", img("search_banner"), "物件検索", True)
    body += section(
        "掲載物件を見る",
        "外部ポータルへ直接移動できます。気になる物件があれば、URLや物件名を送ってください。",
        grid([
            card("SUUMOで見る", "一戸建て・土地などの掲載情報を確認できます。", "../image4/portal_suumo_logo.jpg", ["外部サイト"], SUUMO_URL),
            card("at homeで見る", "掲載中の物件情報と会社情報を確認できます。", "../image4/portal_athome_logo.png", ["外部サイト"], ATHOME_URL),
        ], 2),
    )
    body += section("おすすめ物件の見方", "価格だけでなく、支払いと生活条件で比較します。", grid(PROPERTY_CARDS, 3), soft=True)
    body += section("物件探しのチェックポイント", "問い合わせ前に整理すると、内覧後の判断が早くなります。", grid([
        card("月々支払い", "物件価格、金利、諸費用、管理費を含めた実感値で確認します。"),
        card("生活圏", "校区、通勤、買い物、病院、実家との距離を整理します。"),
        card("将来の選択肢", "売りやすさ、貸しやすさ、維持費も見ておきます。"),
    ], 3), kicker="見るポイント")
    body += cta("気になる物件があれば、見学前に費用感を確認できます。")
    return body


def property_detail_page() -> str:
    body = hero(title_lines("熊本市東区 長嶺", "新築戸建て"), "価格、月々支払い、間取り、周辺環境、見学予約までまとめて確認できます。", img("house"), "物件詳細", True)
    body += section("物件概要", "購入判断に必要な情報を先にまとめます。", grid([
        card("外観・駐車場", "駐車2台想定。前面道路と出入りのしやすさも内覧で確認します。", img("house"), ["外観"]),
        card("前面道路", "毎日の出入り、車通り、駐車のしやすさは現地で確認します。", img("street"), ["道路"]),
        card("資金計画", "物件価格だけでなく、諸費用や月々支払いまで確認します。", img("kitchen"), ["費用"]),
    ], 3))
    body += section("価格と条件", "価格だけでなく、月々支払いと生活条件を並べます。", table([
        ("価格", "3,280万円"),
        ("月々支払い目安", "約8.4万円台から（借入条件により変動）"),
        ("所在地", "熊本市東区 長嶺エリア"),
        ("間取り", "4LDK / 駐車2台想定"),
        ("相談ポイント", "校区、通勤、諸費用、事前審査、引渡し時期"),
    ]), soft=True)
    body += section("見学前に確認したいこと", "内覧の前に支払いと条件を整理すると、見学が無駄になりません。", steps([
        ("総額を確認", "物件価格に加え、諸費用、登記、保険、引越し費用を確認。"),
        ("ローン仮説", "月々支払いとボーナス払いの有無を試算。"),
        ("生活条件", "校区、駐車場、通勤、買い物動線を確認。"),
    ]))
    body += cta("この物件を見学する前に、支払い目安を確認できます。")
    return body


def guide_page() -> str:
    body = hero(title_lines("初回相談から入居まで、", "6つのステップで進めます。"), "何から始めればいいか分からない方に向けて、住宅購入の流れを先に見える化します。", img("guide2"), "購入の流れ", True)
    body += section("購入までの流れ", "問い合わせ後の流れを先に確認できるので、初めての方でも進め方が分かります。", steps([
        ("希望条件の整理", "エリア、予算、校区、駐車台数、入居時期を確認します。"),
        ("資金計画", "借入可能額ではなく、続けられる月々支払いから考えます。"),
        ("物件提案", "ポータル掲載物件と未公開相談を含めて候補を整理します。"),
        ("内覧", "写真では分からない採光、音、道路、駐車を確認します。"),
        ("申込・ローン", "買付、事前審査、契約条件を確認します。"),
        ("契約・引渡し", "重要事項説明、契約、決済、入居まで進行管理します。"),
    ]))
    body += section("最初に決めなくていいこと", "完璧な条件がなくても相談できます。", grid([
        card("買うかどうか", "買う場合と賃貸継続の場合を比較してから判断できます。"),
        card("金融機関", "候補を比較し、事前審査の進め方を一緒に整理します。"),
        card("物件の細かい条件", "譲れない条件と、できれば条件を分けるところから始めます。"),
    ], 3), soft=True, kicker="最初の整理")
    body += cta("購入の流れを聞くだけでも大丈夫です。")
    return body


def strengths_page() -> str:
    body = hero(title_lines("なぜ、ゆめハウスが", "選ばれるのか。"), "熊本の生活圏と資金計画を一緒に見ながら、無理のない住まい探しをサポートします。", img("strength"), "選ばれる理由", True)
    body += section("4つの強み", "地域の事情、資金計画、物件の見方をまとめて相談できます。", grid([
        card("月々支払いから逆算", "ローン、諸費用、頭金まで整理してから候補を見ます。"),
        card("熊本の暮らしに合わせる", "校区、駐車台数、通勤距離、生活施設をまとめて確認します。"),
        card("良い点も弱点も伝える", "道路、築年数、維持費、将来の売却性も含めて比較します。"),
        card("購入後も相談できる", "売却、賃貸管理、住み替えまで同じ窓口で対応します。"),
    ], 4), kicker="相談の強み")
    body += section("比較してから決める", "急がせる営業ではなく、判断材料を揃える相談に寄せます。", table([
        ("資金", "月々支払い / 諸費用 / 事前審査 / 頭金"),
        ("暮らし", "校区 / 駐車台数 / 通勤 / 買い物 / 病院"),
        ("物件", "築年数 / 断熱 / 駐車 / 道路 / 維持費"),
        ("将来", "売却しやすさ / 貸しやすさ / 住み替え"),
    ]), warm=True)
    body += cta()
    return body


def testimonials_page() -> str:
    body = hero(title_lines("よくあるご相談を", "事例で紹介します。"), "住宅ローン、校区、住み替え、賃貸管理など、実際に多い悩みをテーマ別にまとめました。", img("living"), "相談事例", True)
    body += section("相談事例", "自分と近い悩みから相談の入口を選べます。", grid([
        card("家賃がもったいない。でもローンが怖い。", "中古マンション購入前に、管理費込みの月々支払いを試算しました。", None, ["単身", "中古マンション"]),
        card("校区を変えずに戸建てを探したい。", "東区で新築戸建てを検討。駐車2台と通学距離を優先しました。", None, ["家族", "新築戸建て"]),
        card("戸建てを売るか貸すか迷っている。", "住み替え前に査定額と賃料を比較し、次の購入予算を確認しました。", None, ["住み替え"]),
        card("土地から探すと総額が不安。", "土地代、建築費、外構、諸費用まで含めて上限を確認しました。", None, ["土地"]),
        card("親の家の管理をどうするか。", "賃貸管理、売却、空き家管理の選択肢を比較しました。", None, ["管理"]),
        card("物件を見すぎて分からなくなった。", "条件をMust/Wantに分け、候補を3件に絞って比較しました。", None, ["条件整理"]),
    ], 3), kicker="よくある相談")
    body += cta("同じような悩みを、そのまま相談できます。")
    return body


def company_page() -> str:
    body = hero("ゆめハウスについて", "熊本市東区保田窪の店舗を拠点に、購入、売却、賃貸管理まで相談できる不動産窓口です。", img("store"), "会社情報", True)
    body += section("店舗・アクセス", "ご来店前に、所在地、駐車場、電話番号をご確認いただけます。", grid([
        card("ゆめハウス 熊本店", f"{ADDRESS}。お車でのご来店もしやすい店舗です。", img("store_crop"), ["熊本市東区"]),
        card("相談スペース", "住宅ローン、物件比較、売却/管理の相談を落ち着いて行えます。", img("office"), ["無料相談"]),
    ], 2))
    body += section("会社概要", "問い合わせ前に確認したい基本情報です。", table([
        ("事業名", "ゆめハウス"),
        ("運営会社", "株式会社Blooo"),
        ("所在地", ADDRESS),
        ("電話番号", PHONE),
        ("事業エリア", "熊本県・福岡県"),
        ("相談内容", "不動産購入、売却、賃貸管理、住み替え、住宅ローン相談"),
    ]), soft=True)
    body += section("アクセスマップ", "来店前に場所を確認できます。", '<div class="estate-card"><iframe title="ゆめハウス 熊本店 Google Map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3353.216975527012!2d130.7529666!3d32.813015500000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3540f1fb30f04c85%3A0x1d6765d6e7b624c7!2z44KG44KB44OP44Km44K554aK5pys5bqX!5e0!3m2!1sen!2sjp!4v1753280052056!5m2!1sen!2sjp" style="width:100%;height:420px;border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>')
    body += cta("来店相談も、オンライン相談も受付しています。")
    return body


def contact_page() -> str:
    form = f"""
    <div class="estate-grid estate-grid--2">
        <div class="estate-card"><div class="estate-card__body">
            <h3>相談できる内容</h3>
            <ul class="estate-list">
                <li>月々支払いや住宅ローンの不安</li>
                <li>気になる物件の見学相談</li>
                <li>売却査定、住み替え、賃貸管理</li>
                <li>熊本市内のエリア・校区相談</li>
            </ul>
            <div class="estate-actions"><a class="estate-button-light" href="tel:{PHONE}">電話する {PHONE}</a></div>
        </div></div>
        <form class="estate-card estate-card__body estate-form" action="#" method="post">
            <div class="estate-field"><label for="name">お名前</label><input id="name" name="name" required autocomplete="name" /></div>
            <div class="estate-field"><label for="tel">電話番号</label><input id="tel" name="tel" required autocomplete="tel" /></div>
            <div class="estate-field"><label for="email">メールアドレス</label><input id="email" name="email" type="email" autocomplete="email" /></div>
            <div class="estate-field"><label for="type">相談内容</label><select id="type" name="type"><option>物件購入</option><option>住宅ローン</option><option>売却・査定</option><option>賃貸管理</option><option>その他</option></select></div>
            <div class="estate-field"><label for="message">お問い合わせ内容</label><textarea id="message" name="message" rows="6" required placeholder="気になる物件名、希望エリア、月々支払いの不安などをご記入ください"></textarea></div>
            <button class="estate-button" type="submit">内容を送信する</button>
        </form>
    </div>
    """
    body = hero(title_lines("まずはお気軽に", "ご相談ください。"), "買うか決めていない段階でも大丈夫です。物件、ローン、売却、賃貸管理の不安をそのまま送ってください。", img("office"), "お問い合わせ", True)
    body += section("無料相談フォーム", "所要時間は1分程度です。営業時間外でも送信できます。", form)
    body += section("よくある相談", "最初の相談で多い内容です。", faq(DEFAULT_FAQ), soft=True)
    return body


def rental_page() -> str:
    body = hero(title_lines("賃貸経営のお悩み、", "まずはご相談ください。"), "空室対策、募集、管理、売却との比較まで、オーナー様の状況に合わせて整理します。", img("land_banner"), "賃貸管理", True)
    body += section("賃貸管理でできること", "管理を任せる前に、どこまで対応できるかを明確にします。", grid([
        card("入居者募集", "ポータル掲載、写真、条件設定を見直し、空室期間を短くします。"),
        card("管理業務", "入居者対応、更新、退去、原状回復などを整理します。"),
        card("売却との比較", "貸すべきか、売るべきか、手残りと将来性で比較します。"),
    ], 3), kicker="オーナー様向け")
    body += section("相談の流れ", "物件状況が分からなくても相談できます。", steps([
        ("現状確認", "所在地、築年数、空室状況、家賃、修繕履歴を確認します。"),
        ("選択肢の比較", "募集継続、条件変更、リフォーム、売却を比較します。"),
        ("実行プラン", "募集条件、管理範囲、費用、スケジュールを決めます。"),
    ]), soft=True)
    body += cta("空室や管理の不安も、無料で相談できます。")
    return body


def faq_page() -> str:
    body = hero("よくあるご質問", "住宅ローン、諸費用、内覧、契約、売却、賃貸管理まで。問い合わせ前の不安をまとめました。", img("interior"), "よくある質問", True)
    body += section("購入・ローン", "購入前に多い質問です。", faq(DEFAULT_FAQ))
    body += section("内覧・契約", "見学から契約までの不安を整理します。", faq([
        ("内覧だけでもできますか？", "はい。ただし見学前に予算感を確認しておくと、判断しやすくなります。"),
        ("手付金はいくら必要ですか？", "物件や条件により異なります。契約前に金額、支払い時期、解除条件を説明します。"),
        ("諸費用はどれくらい見ればいいですか？", "登記、保険、ローン費用、仲介手数料などがあり、物件ごとに試算します。"),
    ]), soft=True)
    body += section("売却・賃貸管理", "住み替えやオーナー様向けの質問です。", faq([
        ("売るか貸すか迷っています。", "査定額、想定賃料、管理費、修繕リスクを並べて比較できます。"),
        ("空室だけ相談できますか？", "はい。募集条件、写真、設備、家賃設定などを確認します。"),
    ]))
    body += cta("FAQで解決しない不安は、そのまま相談できます。")
    return body


def privacy_page() -> str:
    body = hero("プライバシーポリシー", "お問い合わせでお預かりする個人情報の取り扱いについてご説明します。", img("office"), "個人情報保護方針", True)
    body += section("個人情報の取り扱い", "安心してお問い合わせいただくための基本方針です。", table([
        ("利用目的", "お問い合わせ対応、物件紹介、内覧調整、売却/賃貸管理相談、必要な連絡のために利用します。"),
        ("第三者提供", "法令に基づく場合、または金融機関・士業・関係事業者との手続きに必要な場合を除き、本人の同意なく第三者に提供しません。"),
        ("安全管理", "取得した情報は適切に管理し、不要になった情報は合理的な範囲で削除します。"),
        ("開示・訂正", "ご本人からの開示、訂正、利用停止等のご請求には、本人確認のうえ対応します。"),
        ("お問い合わせ先", f"ゆめハウス / {PHONE} / {ADDRESS}"),
    ]))
    body += cta("個人情報に関するお問い合わせはこちら。", "フォームまたはお電話でお問い合わせください。")
    return body


PAGES = {
    "1._home": ("ゆめハウス｜熊本の住まい探し・住宅ローン相談", "熊本市東区のゆめハウス。物件探し、住宅ローン、売却、賃貸管理まで相談できる不動産窓口です。", home_page),
    "2._property_search": ("物件を見る｜ゆめハウス", "SUUMO / at home の掲載物件と、月々支払いからの住まい探し相談。", property_search_page),
    "3._property_details": ("物件詳細｜ゆめハウス", "物件価格、月々支払い、間取り、周辺環境、見学相談まで確認できます。", property_detail_page),
    "4._guide_flow": ("購入の流れ｜ゆめハウス", "初回相談から入居までの流れを、住宅ローンと物件探しの順番で説明します。", guide_page),
    "5._our_strengths": ("選ばれる理由｜ゆめハウス", "熊本の生活圏と資金計画を一緒に整理する、ゆめハウスの強み。", strengths_page),
    "6._testimonials": ("相談事例｜ゆめハウス", "住宅ローン、校区、住み替え、賃貸管理などの相談事例。", testimonials_page),
    "7._company_info": ("会社情報・アクセス｜ゆめハウス", "ゆめハウス熊本店の所在地、運営会社、アクセス情報。", company_page),
    "8._contact": ("無料相談・お問い合わせ｜ゆめハウス", "住まい探し、住宅ローン、売却、賃貸管理の無料相談フォーム。", contact_page),
    "9._rental_business": ("賃貸管理｜ゆめハウス", "空室対策、募集、管理、売却との比較まで相談できる賃貸管理ページ。", rental_page),
    "10._faq": ("よくある質問｜ゆめハウス", "住宅ローン、諸費用、内覧、売却、賃貸管理のよくある質問。", faq_page),
    "11._privacy": ("プライバシーポリシー｜ゆめハウス", "ゆめハウスの個人情報保護方針。", privacy_page),
}


def render(slug: str, title: str, description: str, body_func) -> str:
    body = body_func()
    html = f"""<!doctype html>
<html lang="ja" class="light">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{e(title)}</title>
    <meta name="description" content="{e(description)}" />
    <meta property="og:title" content="{e(title)}" />
    <meta property="og:description" content="{e(description)}" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="ゆめハウス" />
    <meta property="og:locale" content="ja_JP" />
    <meta name="theme-color" content="#16324f" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&family=Noto+Sans+JP:wght@400;500;700;900&family=Noto+Serif+JP:wght@600;700;900&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="../shared/base.css?v={VERSION}" />
</head>
<body class="estate-page">
{header(slug)}
<main class="estate-main">
{body}
</main>
{footer()}
</body>
</html>
"""
    return "\n".join(line.rstrip() for line in html.splitlines()) + "\n"


def main() -> None:
    for slug, (title, description, body_func) in PAGES.items():
        path = SITE / slug / "code.html"
        path.write_text(render(slug, title, description, body_func), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
