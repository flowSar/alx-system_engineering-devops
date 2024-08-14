
# specific Apache configuration or PHP file

exec { 'fix_php_typo':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
