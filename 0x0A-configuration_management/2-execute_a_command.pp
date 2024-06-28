
exec { 'kill_process':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}
