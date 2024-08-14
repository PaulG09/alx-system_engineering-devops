# This Puppet manifest ensures the correct Apache configuration is in place
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  source  => 'puppet:///modules/apache/apache2.conf',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  require   => File['/etc/apache2/apache2.conf'],
}
