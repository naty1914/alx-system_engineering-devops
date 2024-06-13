# It fixes ngnix server to accept more request
exec {'modify nginx service limit':
  command => 'sed -i "s/15/20000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
