Monitor your router with (r)syslogd 
####################################
:date: 2011-02-12 21:19
:author: reece
:slug: monitor-your-router-with-rsyslogd
:status: published
:attachments: reece/wp-content/uploads/2011/02/Screenshot-D-LINK-CORPORATION-INC-WIRELESS-ROUTER-HOME-Chromium.png

I'm having lots of dropped connections at home. Unfortunately,
consumer-grade routers typically have poor monitoring facilities out of
the box. Unix/Linux environments have long been able to aggregate
logging messages across multiple hosts through a service called syslog.
Many routers use embedded Linux and support sending messages to remote
systems via syslog. (Emailing logs is supported, but that's a clumsy
option.) This post is a short tip on how to configure a D-Link
DI-825 (rev B1) to send system messages to an Ubuntu 10.0 host, but the
general method will apply to many routers and nearly all Unix/Linux
hosts are capable of acting as logging destinations.

First, you'll need to configure your syslog destination to listen for
messages. Ubuntu 10.10 uses rsyslog, which has a mercifully modular
configuration mechanism. The configuration is:

| [text]
| whoville$ cat /etc/rsyslog.d/40-router.conf
| $ModLoad imudp
| $UDPServerRun 514

| $ModLoad imtcp
| $InputTCPServerRun 514

| if $fromhost-ip startswith '192.168.0.' then /var/log/router.log
| [/text]

Restart rsyslog with something like
﻿﻿﻿﻿﻿﻿\ ``sudo service rsyslog reload``. Your machine is now listening
for syslog events and you should see that ``/var/log/router.log`` was
created.

Then, configure your router. The DI-825 configuration looks like this:

|image0|

192.168.0.175 is the internal IP address of the syslog destination.

| You should now be able to monitor your router, like this:
| [text]
| whoville$ sudo tail -f /var/log/router.log
| Feb 12 20:34:26 192.168.0.1 udhcpd[782]: UDHCPD sendOffer : find a
  free IP
| Feb 12 20:34:28 192.168.0.1 udhcpd[782]: UDHCPD sending OFFER of
  192.168.0.104
| Feb 12 20:34:28 192.168.0.1 udhcpd[782]: UDHCPD sendOffer :
  device\_lan\_ip=192.168.0.1 , device\_lan\_subnet\_mask=255.255.255.0
| Feb 12 20:34:28 192.168.0.1 udhcpd[782]: UDHCPD sendOffer : client is
  in lease/offered table
| Feb 12 20:34:28 192.168.0.1 udhcpd[782]: UDHCPD sending OFFER of
  192.168.0.104
| Feb 12 20:34:29 192.168.0.1 udhcpd[782]: UDHCPD sending ACK to
  192.168.0.104
| Feb 12 20:35:03 192.168.0.1 udhcpd[782]: UDHCPD sending ACK to
  192.168.0.104
| [/text]

.. |image0| image:: http://harts.net/reece/wp-content/uploads/2011/02/Screenshot-D-LINK-CORPORATION-INC-WIRELESS-ROUTER-HOME-Chromium.png
   :class: alignnone size-full wp-image-350
   :width: 582px
   :height: 274px
   :target: http://harts.net/reece/2011/02/12/monitor-your-router-with-rsyslogd/screenshot-d-link-corporation-inc-wireless-router-home-chromium/
