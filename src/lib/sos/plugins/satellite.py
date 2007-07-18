### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sos.plugintools

class satellite(sos.plugintools.PluginBase):
    """RHN Satellite related information
    """

    def defaultenabled(self):
        return False

    def setup(self):
        self.addCopySpec("/etc/httpd/conf")
        self.addCopySpec("/etc/rhn")
        self.addCopySpec("/etc/sysconfig/rhn")
        self.addCopySpec("/etc/tnsnames.ora")	
        self.addCopySpec("/var/log/httpd")	# httpd-logs
        self.addCopySpec("/var/log/rhn*")	# rhn-logs
        self.addCopySpec("/var/log/rhn/rhn-database-installation.log")
        self.addCopySpec("/etc/jabberd")

	# tomcat for satellite 400+
        self.addCopySpec("/etc/tomcat5")
        self.addCopySpec("/var/log/tomcat5")

	# all these used to go in $DIR/mon-logs
        self.addCopySpec("/opt/notification/var/*.log*")
        self.addCopySpec("/var/tmp/ack_handler.log*")
        self.addCopySpec("/var/tmp/enqueue.log*")

        self.addCopySpec("/home/nocpulse/var/*.log*")
        self.addCopySpec("/home/nocpulse/var/commands/*.log*")
        self.addCopySpec("/var/tmp/ack_handler.log*")
        self.addCopySpec("/var/tmp/enqueue.log*")

        self.addCopySpec("/root/ssl-build")
        self.addCopySpec("rpm -qa --last") # $DIR/rpm-manifest
        self.addCopySpec("/usr/bin/rhn-schema-version") # $DIR/database-schema-version
        self.addCopySpec("/usr/bin/rhn-charsets") # $DIR/database-character-sets

        return
