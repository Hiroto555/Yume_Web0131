<?php
/*
Template Name: Static Local (Theme Ignored)
Template Post Type: page
*/

declare(strict_types=1);

function astra_child_0130_static_local_routes(): array {
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
	);
}

function astra_child_0130_static_local_current_slug(): string {
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

function astra_child_0130_static_local_insert_base_href( string $html, string $base_href ): string {
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

function astra_child_0130_static_local_rewrite_links_to_wordpress( string $html, array $routes ): string {
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

function astra_child_0130_static_local_rewrite_fragment_only_hrefs( string $html, string $current_url ): string {
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

$routes = astra_child_0130_static_local_routes();
$slug   = astra_child_0130_static_local_current_slug();

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

$html = astra_child_0130_static_local_insert_base_href( $html, $base_href );
$html = astra_child_0130_static_local_rewrite_links_to_wordpress( $html, $routes );
if ( is_string( $current_url ) && $current_url !== '' ) {
	$html = astra_child_0130_static_local_rewrite_fragment_only_hrefs( $html, $current_url );
}

header( 'Content-Type: text/html; charset=UTF-8' );
echo $html;
exit;
