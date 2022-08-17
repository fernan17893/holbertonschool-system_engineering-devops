#kills process "killmenow"
exec{'kill':
  command => 'pkill -f killmenow',
  path    => 'usr/bin/:/usr/local/bin/:/bin/',
}
