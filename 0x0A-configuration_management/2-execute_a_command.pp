
# kill process killmenow using pkill
exec { 'kill_process_killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}
