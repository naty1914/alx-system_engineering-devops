# Terminates killmenow process if it's running using exec resource

exec { 'terminate_killmenow':
  command => 'pkill  killmenow',
  path    => '/bin/',
  onlyif  => 'pgrep killmenow',
}
