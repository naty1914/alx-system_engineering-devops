# It installs flask using Puppet from pip3 with specific instruction
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':,
  ensure   => '2.0.2',
  provider => 'pip3',
}
