Where is our (Hello) World going?!
##################################
:date: 2011-02-15 14:13
:author: reece
:category: Uncategorized
:slug: where-is-our-hello-world-going
:status: published

Hype and evangelism run rampant in technology. That's not to say there
aren't real and substantial advances, of course. One of my personal
mantras is that simple things should be simple and complex should be
possible. In other words, complexity shouldn't come at the expense
simplicity. (This isn't a novel idea, just my own internal
rephrasing.) With that in mind, I was amused by the following
observation:

| apt12j$ time perl -e 'print "Hello $ARGV[0]\\n"' World
| Hello World

| real 0m0.003s
| user 0m0.000s
| sys 0m0.000s

| apt12j$ time python -c 'import sys; print "Hello " + sys.argv[1]'
  World
| Hello World

| real 0m0.022s
| user 0m0.012s
| sys 0m0.008s

| apt12j$ time groovy -e "println 'Hello ' + args[0]" World
| Hello World

| real 0m1.244s
| user 0m2.108s
| sys 0m0.120s

Progress?

This is really meant to be tongue in cheek... clearly we aspire to more
than Hello World, and there's a lot more to the overall value and
usability of a language than just timing. And I'm not intending to
promulgate or disparage Perl, Python, or Groovy by inclusion above, or
Java, Ruby, Fortran, Lisp, or anything else by exclusion.

Instead, the point was that I was doing some investigation with Groovy
and was struck by sluggish start-up time.
