
# we creating a school file with "I love puppet content"
# and 0744 is the permission of the file and the www-data
# is the owner and group of the file

file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
