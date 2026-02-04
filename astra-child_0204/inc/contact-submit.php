<?php

declare(strict_types=1);

function astra_child_0204_contact_submit_action(): string {
	return 'astra_child_0204_contact_submit';
}

function astra_child_0204_contact_submit_register(): void {
	add_action( 'admin_post_nopriv_' . astra_child_0204_contact_submit_action(), 'astra_child_0204_contact_submit_handle' );
	add_action( 'admin_post_' . astra_child_0204_contact_submit_action(), 'astra_child_0204_contact_submit_handle' );
}

add_action( 'init', 'astra_child_0204_contact_submit_register' );

function astra_child_0204_contact_submit_redirect_url( string $status ): string {
	$redirect = wp_get_referer();
	if ( ! is_string( $redirect ) || $redirect === '' ) {
		$redirect = home_url( '/contact/' );
	}

	$key = $status === 'sent' ? 'contact_sent' : 'contact_error';
	return add_query_arg( $key, '1', $redirect );
}

function astra_child_0204_contact_submit_handle(): void {
	if ( $_SERVER['REQUEST_METHOD'] !== 'POST' ) {
		wp_safe_redirect( astra_child_0204_contact_submit_redirect_url( 'error' ) );
		exit;
	}

	$nonce = isset( $_POST['_wpnonce'] ) ? (string) wp_unslash( $_POST['_wpnonce'] ) : '';
	if ( $nonce === '' || ! wp_verify_nonce( $nonce, astra_child_0204_contact_submit_action() ) ) {
		wp_safe_redirect( astra_child_0204_contact_submit_redirect_url( 'error' ) );
		exit;
	}

	$honeypot = isset( $_POST['website'] ) ? (string) wp_unslash( $_POST['website'] ) : '';
	if ( trim( $honeypot ) !== '' ) {
		wp_safe_redirect( astra_child_0204_contact_submit_redirect_url( 'sent' ) );
		exit;
	}

	$name    = isset( $_POST['name'] ) ? sanitize_text_field( (string) wp_unslash( $_POST['name'] ) ) : '';
	$kana    = isset( $_POST['kana'] ) ? sanitize_text_field( (string) wp_unslash( $_POST['kana'] ) ) : '';
	$tel     = isset( $_POST['tel'] ) ? sanitize_text_field( (string) wp_unslash( $_POST['tel'] ) ) : '';
	$email   = isset( $_POST['email'] ) ? sanitize_email( (string) wp_unslash( $_POST['email'] ) ) : '';
	$store   = isset( $_POST['store'] ) ? sanitize_text_field( (string) wp_unslash( $_POST['store'] ) ) : '';
	$message = isset( $_POST['message'] ) ? sanitize_textarea_field( (string) wp_unslash( $_POST['message'] ) ) : '';

	if ( $name === '' || $kana === '' || $tel === '' || $email === '' || $store === '' || $message === '' || ! is_email( $email ) ) {
		wp_safe_redirect( astra_child_0204_contact_submit_redirect_url( 'error' ) );
		exit;
	}

	$to      = 'hiroto.shimokawa@blooo.co.jp';
	$subject = '【ゆめハウス】お問い合わせ';
	$body    = implode(
		"\n",
		array(
			"お名前: {$name}",
			"フリガナ: {$kana}",
			"電話番号: {$tel}",
			"メールアドレス: {$email}",
			"お問い合わせ店舗: {$store}",
			'',
			'お問い合わせ内容:',
			$message,
			'',
			'---',
			'送信情報:',
			'日時: ' . gmdate( 'Y-m-d H:i:s' ) . ' UTC',
			'IP: ' . ( isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( (string) wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '' ),
			'UA: ' . ( isset( $_SERVER['HTTP_USER_AGENT'] ) ? sanitize_text_field( (string) wp_unslash( $_SERVER['HTTP_USER_AGENT'] ) ) : '' ),
		)
	);

	$headers = array(
		'Content-Type: text/plain; charset=UTF-8',
		'Reply-To: ' . $email,
	);

	$ok = wp_mail( $to, $subject, $body, $headers );
	wp_safe_redirect( astra_child_0204_contact_submit_redirect_url( $ok ? 'sent' : 'error' ) );
	exit;
}

