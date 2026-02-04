<?php
/*
Template Name: Static Local (Theme Ignored)
Template Post Type: page
*/

declare(strict_types=1);

function astra_child_0204_static_local_routes(): array {
	return array(
		'home'            => array(
			'html' => '1._home/code.html',
			'url'  => home_url( '/home/' ),
		),
		'property-search' => array(
			'html' => '2._property_search/code.html',
			'url'  => home_url( '/property-search/' ),
		),
		'property-details' => array(
			'html' => '3._property_details/code.html',
			'url'  => home_url( '/property-details/' ),
		),
		'guide-flow'      => array(
			'html' => '4._guide_flow/code.html',
			'url'  => home_url( '/guide-flow/' ),
		),
		'our-strengths'   => array(
			'html' => '5._our_strengths/code.html',
			'url'  => home_url( '/our-strengths/' ),
		),
		'testimonials'    => array(
			'html' => '6._testimonials/code.html',
			'url'  => home_url( '/testimonials/' ),
		),
		'company-info'    => array(
			'html' => '7._company_info/code.html',
			'url'  => home_url( '/company-info/' ),
		),
		'contact'         => array(
			'html' => '8._contact/code.html',
			'url'  => home_url( '/contact/' ),
		),
		'rental-business' => array(
			'html' => '9._rental_business/code.html',
			'url'  => home_url( '/rental-business/' ),
		),
		'faq'             => array(
			'html' => '10._faq/code.html',
			'url'  => home_url( '/faq/' ),
		),
		'privacy'         => array(
			'html' => '11._privacy/code.html',
			'url'  => home_url( '/privacy/' ),
		),
	);
}

function astra_child_0204_static_local_current_slug(): string {
	if ( is_front_page() ) {
		return 'home';
	}

	$page_id = get_queried_object_id();
	if ( ! is_int( $page_id ) || $page_id <= 0 ) {
		return '';
	}

	$slug = sanitize_title( (string) get_post_field( 'post_name', $page_id ) );
	return $slug;
}

function astra_child_0204_static_local_insert_base_href( string $html, string $base_href ): string {
	if ( stripos( $html, '<base' ) !== false ) {
		return $html;
	}

	if ( stripos( $html, '<head' ) === false ) {
		return $html;
	}

	$base_tag = '<base href="' . esc_url( $base_href ) . '">';

	$updated = preg_replace(
		'/<head(\b[^>]*)>/i',
		'<head$1>' . $base_tag,
		$html,
		1
	);

	return is_string( $updated ) ? $updated : $html;
}

function astra_child_0204_static_local_rewrite_links_to_wordpress( string $html, array $routes ): string {
	$static_to_wp = array();
	foreach ( $routes as $route ) {
		if ( ! is_array( $route ) || empty( $route['html'] ) || empty( $route['url'] ) ) {
			continue;
		}

		$static_to_wp[ '../' . $route['html'] ] = $route['url'];
	}

	$html = preg_replace_callback(
		'/\bhref=(["\'])(\.\.\/[0-9]+\._[a-z_]+\/code\.html)([^"\']*)\1/i',
		static function ( array $matches ) use ( $static_to_wp ): string {
			$quote  = $matches[1];
			$target = $matches[2];
			$suffix = $matches[3];

			if ( ! isset( $static_to_wp[ $target ] ) ) {
				return $matches[0];
			}

			return 'href=' . $quote . esc_url( $static_to_wp[ $target ] . $suffix ) . $quote;
		},
		$html
	);

	return is_string( $html ) ? $html : '';
}

function astra_child_0204_static_local_rewrite_fragment_only_hrefs( string $html, string $current_url ): string {
	$html = preg_replace_callback(
		'/\bhref=(["\'])(#[^"\']*)\1/i',
		static function ( array $matches ) use ( $current_url ): string {
			$quote    = $matches[1];
			$fragment = $matches[2];

			return 'href=' . $quote . esc_url( $current_url . $fragment ) . $quote;
		},
		$html
	);

	return is_string( $html ) ? $html : '';
}

function astra_child_0204_static_local_contact_action_url(): string {
	return admin_url( 'admin-post.php' );
}

function astra_child_0204_static_local_contact_form_hidden_fields_html(): string {
	$nonce = wp_create_nonce( astra_child_0204_contact_submit_action() );

	$fields = array(
		'<input type="hidden" name="action" value="' . esc_attr( astra_child_0204_contact_submit_action() ) . '">',
		'<input type="hidden" name="_wpnonce" value="' . esc_attr( $nonce ) . '">',
		'<div style="position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden;"><label>Leave this field empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>',
	);

	return implode( '', $fields );
}

function astra_child_0204_static_local_contact_flash_html(): string {
	if ( isset( $_GET['contact_sent'] ) && (string) $_GET['contact_sent'] === '1' ) {
		return '<div style="margin:12px 0;padding:12px 14px;border:1px solid #86efac;background:#dcfce7;color:#166534;border-radius:10px;font-weight:700;">送信が完了しました。</div>';
	}
	if ( isset( $_GET['contact_error'] ) && (string) $_GET['contact_error'] === '1' ) {
		return '<div style="margin:12px 0;padding:12px 14px;border:1px solid #fecaca;background:#fee2e2;color:#991b1b;border-radius:10px;font-weight:700;">送信に失敗しました。入力内容をご確認のうえ、もう一度お試しください。</div>';
	}
	return '';
}

function astra_child_0204_static_local_rewrite_contact_form( string $html ): string {
	$action_url = esc_url( astra_child_0204_static_local_contact_action_url() );
	$hidden     = astra_child_0204_static_local_contact_form_hidden_fields_html();
	$flash      = astra_child_0204_static_local_contact_flash_html();

	$updated = preg_replace_callback(
		'/<form\b[^>]*>/i',
		static function ( array $matches ) use ( $action_url, $hidden, $flash ): string {
			$form_tag = $matches[0];

			if ( stripos( $form_tag, 'action=' ) !== false ) {
				$form_tag = preg_replace( '/\baction=(["\'])(.*?)\1/i', 'action="' . $action_url . '"', $form_tag, 1 );
			} else {
				$form_tag = rtrim( $form_tag, '>' ) . ' action="' . $action_url . '">';
			}

			if ( stripos( $form_tag, 'method=' ) === false ) {
				$form_tag = rtrim( $form_tag, '>' ) . ' method="POST">';
			}

			return $form_tag . $flash . $hidden;
		},
		$html,
		1
	);

	return is_string( $updated ) ? $updated : $html;
}

$routes = astra_child_0204_static_local_routes();
$slug   = astra_child_0204_static_local_current_slug();

if ( $slug === '' || ! isset( $routes[ $slug ] ) ) {
	status_header( 404 );
	header( 'Content-Type: text/html; charset=UTF-8' );
	echo '<h1>404</h1><p>Unknown page slug.</p>';
	exit;
}

$rel_html_path = (string) $routes[ $slug ]['html'];

$base_dir  = trailingslashit( get_stylesheet_directory() ) . 'assets/site/';
$file_path = $base_dir . $rel_html_path;

if ( ! file_exists( $file_path ) ) {
	status_header( 404 );
	header( 'Content-Type: text/html; charset=UTF-8' );
	echo '<h1>404</h1><p>HTML not found: <code>' . esc_html( $rel_html_path ) . '</code></p>';
	exit;
}

$html = file_get_contents( $file_path );
if ( $html === false ) {
	status_header( 500 );
	header( 'Content-Type: text/html; charset=UTF-8' );
	echo '<h1>500</h1><p>Failed to read HTML.</p>';
	exit;
}

$html_dir   = dirname( $rel_html_path );
$base_href  = trailingslashit( get_stylesheet_directory_uri() ) . 'assets/site/' . trim( $html_dir, '/' ) . '/';
$current_url = get_permalink( get_queried_object_id() );

$html = astra_child_0204_static_local_insert_base_href( $html, $base_href );
$html = astra_child_0204_static_local_rewrite_links_to_wordpress( $html, $routes );
if ( is_string( $current_url ) && $current_url !== '' ) {
	$html = astra_child_0204_static_local_rewrite_fragment_only_hrefs( $html, $current_url );
}
if ( $slug === 'contact' ) {
	$html = astra_child_0204_static_local_rewrite_contact_form( $html );
}

header( 'Content-Type: text/html; charset=UTF-8' );
echo $html;
exit;
