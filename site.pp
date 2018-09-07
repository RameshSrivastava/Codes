class ssh {
  file  {  '/etc/ssh/sshd_config':
	ensure => present,
	notify   => Service ['ssh']
}
service { 'ssh' :
	ensure => 'running',
	enable => 'true',
}
}