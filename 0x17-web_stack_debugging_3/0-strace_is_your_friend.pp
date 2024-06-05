# A puppet manifest to rename class-wp-locale.php to class-wp-locale.phpp and restart Apache
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => 'file',
  source => '/var/www/html/wp-includes/class-wp-locale.php',
  before => File['/var/www/html/wp-includes/class-wp-locale.php'],
}

file { '/var/www/html/wp-includes/class-wp-locale.php':
  ensure  => 'absent',
  require => File['/var/www/html/wp-includes/class-wp-locale.phpp'],
}


# It ensures Apache service is running and will be notified if the file changes
service { 'apache2':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/var/www/html/wp-includes/class-wp-locale.phpp'],
}
