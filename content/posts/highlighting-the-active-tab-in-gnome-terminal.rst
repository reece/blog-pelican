Highlighting the active tab in GNOME terminal
#############################################
:date: 2013-02-26 21:41
:author: reece
:category: Uncategorized
:tags: gnome, ubuntu
:slug: highlighting-the-active-tab-in-gnome-terminal
:status: published
:attachments: reece/wp-content/uploads/2013/02/Selection_321.png

In recent iterations of GNOME terminal, the active tab is nearly
indistinguishable from the inactive ones.  That makes it harder to
navigate when you've got a bunch of terminals open simultaneously.
Fortunately, GNOME uses a modified CSS scheme to control theme
appearance, and that makes it easy to highlight an active tab. Here's
how.

Create (or edit) ~/.config/gtk-3.0/gtk.css. Add these lines:

::

    @define-color ubuntu_orange #fb9267;

::

    TerminalWindow .notebook tab:active {
     background-color: shade(@ubuntu_orange,1.1);
    }

Then, exit all open terminals, and then open a new terminal and create a
tab. With the above modification, you should see tabs like this:

|GNOME terminal tabs|

.. |GNOME terminal tabs| image:: http://harts.net/reece/wp-content/uploads/2013/02/Selection_321.png
   :class: aligncenter wp-image-476
   :width: 599px
   :height: 64px
   :target: http://harts.net/reece/wp-content/uploads/2013/02/Selection_321.png
