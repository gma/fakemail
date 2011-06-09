#!/usr/bin/env python
#
# $Id$


from distutils.core import *


setup(name="fakemail-python",
      version="1.0",
      author="Graham Ashton",
      author_email="graham@effectif.com",
      url="http://fakemail.sourceforge.net/",
      download_url="http://sourceforge.net/project/showfiles.php?group_id=130951&package_id=168675",
      scripts=["fakemail.py"],
      description="Fake SMTP server for use in software testing",
      long_description="""fakemail is a fake mail server that captures
      emails as files for acceptance testing. This avoids the excessive
      configuration of setting up a real mail server and trying to
      extract mail queue content.""",
      classifiers=["Development Status :: 4 - Beta",
                   "Topic :: Software Development :: Testing",
                   "Topic :: Communications :: Email",
                   "Programming Language :: Python",
                   "Operating System :: OS Independent"]
)
