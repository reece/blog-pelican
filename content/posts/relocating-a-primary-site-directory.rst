Relocating a primary site directory
###################################
:date: 2010-03-04 12:22
:author: reece
:category: Problems of a Prop Head
:slug: relocating-a-primary-site-directory
:status: published

My hosting provider, \ `HostMonster <http://hostmonster.com>`__,
uses \ `cPanel <http://www.cpanel.net/>`__ to enable account
administrators to configure their domains and services. By default,
Hostmonster and cPanel place web data for the primary domain in
~/public\_html/, with subdomains and "add-on" domains as subdirectories
therein. That means that files for the primary domain are comingled with
the document roots of other domains. The incongruency of that layout
causes heartburn for people like me. This post tells you how to relocate
those files AND have them served by the original URLs for the primary
domain.

UPDATE: The following \*mostly\* works, but I've had yet unresolvable
problems with directory URLs not being rewritten to append the /, which
causes failure. A slow investigation is in progress...

There are several reasons why you might want relocate files for the
primary domain. First, there's the compulsive disorder desire for
organization that provides better containment of files related to a
site, and nothing else. Good organization often leads to reduced errors
and improved efficiency (not accounting for the time it takes to blog
about them). A second reason is that people might access one domain's
data through the URL of a primary domain, such as
http://primary.com/secondary.com/. This isn't a concern in my case, but
it might be for others. (I do use this nesting in other contexts to make
dev.domain.com equivalent to domain.com/dev, but that'll be a different
story.)

My original directory structure looked something like this:

::

    $ ls ~/public_html
    400.shtml             401.shtml             403.shtml
    404.shtml             500.php               500.shtml
    beaconcoaching            bruceandhanna.com         cgi-bin
    dev.genome-commons.org        fastphp.ini           favicon.ico
    genome-commons.org        genomeinterpretation.org      glenparkassociation.org
    home-exchange             index.html            nctgi
    reece                 reece-ex-wp           robots.txt
    spat                  tahoe             tmp
    unison-db.org

See how the the error pages, my subdirectory, and other primary domain
files are scattered among the document roots that serve domains for
`Beacon Coaching <http://beaconcoaching.com>`__, a development `Genome
Commons <http://genomecommons.org>`__ site, and `Unison
database <http://unison-db.org>`__? Yuk.

I prefer to name directories for the domains they serve, such as
~/public\_html/harts.net/. Sure, I could move the primary domain files
there, but then they'd be served by URLs like
http://harts.net/harts.net/reece/. [N.B. This is a bogus link that
illustrates what I didn't want.] Preserve the original URLs is critical.

The solution is to move files for the primary domain into a dedicated
directory and tell apache,
via \ `mod\_rewrite <http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html>`__
rules in ~/public\_html/.htaccess, where to look for primary domain
files.

Specifically, I did this:

#. ssh to the domain
#. cd ~/public\_html
#. mkdir harts.net
#. mv --target=harts.net [primary domain files]
#. add the following stanza to ~/public\_html/.htaccess:

::

    RewriteEngine on

    # rewrite requests for primary domain into harts.net/
    RewriteCond %{HTTP_HOST} ^(www\.)?harts\.net
    RewriteCond %{REQUEST_URI} !^/harts.net
    RewriteCond %{REMOTE_HOST} !www.simplescripts.com
    RewriteRule ^(.*)$ /harts.net/$1 [L]

Notice the exception for `SimpleScripts <http://simplescripts.com>`__ --
without that, simplescripts will be unable to manage domain
installations. (SimpleScripts is a terrific tool that greatly
facilitates installing and upgrading many common blogging, CMS, forum,
wiki, commerce, and customer service tools.)
