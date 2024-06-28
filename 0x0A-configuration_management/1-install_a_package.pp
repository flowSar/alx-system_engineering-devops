
# check if pip3 is installed
package {'python3-pip':
  ensure => installed,
}

# install flask version 2.1.0
# first we run the unless command to check if flask instlled 
# before running command
exec { 'install_flask_2.1.0':
  command => '/usr/bin/pip3 install Flask==2.0.1',
  unless  => '/usr/bin/pip3 show Flask | grep "Version: 2.1.0"',
  require => Package['python3-pip'],
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}
