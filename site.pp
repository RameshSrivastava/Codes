class ssh {
  file  {  '/etc/ssh/sshd_config':
	ensure => present,
	notify   => Service ['ssh']
}
service { 'ssh' :
	ensure => 'running',
	enable => 'true',
}
concat { '/etc/ssh/sshd_config':
  ensure => present,
}

concat::fragment { 'sshd_config':
  target  => '/etc/ssh/sshd_config',
  content => 'AllowUsers test',
  order   => '01'
}
}
