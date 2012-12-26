        # Get the hash of our submodule commit.  We will need it
        # to match the output of the push command.
        p = Run(['git rev-parse HEAD'.split()])
        self.assertTrue(p.status == 0, p.image)
        subm_rev = p.out.strip()

        # Also get the "author date" for our commit.  We need this
        # info as part of the expected output.
        p = Run(['git log -n1 --pretty=format:%ad'.split()])
        self.assertTrue(p.status == 0, p.image)
        author_date = p.out.strip()

        # Same for the hash of the .gitmodules file...
        p = Run(['git ls-tree HEAD .gitmodules'.split()])
        self.assertTrue(p.status == 0, p.image)
        gitmodules_hash = p.out.split()[2]

        expected_out = """\
remote:   DEBUG: check_update(ref_name=refs/heads/master, old_rev=7a373b536b65b600a449b5c739c137301f6fd364, new_rev=%(subm_rev)s)
remote: DEBUG: validate_ref_update (refs/heads/master, 7a373b536b65b600a449b5c739c137301f6fd364, %(subm_rev)s)
remote: DEBUG: update base: 7a373b536b65b600a449b5c739c137301f6fd364
remote: DEBUG: (commit-per-commit style checking)
remote: DEBUG: check_commit(old_rev=7a373b536b65b600a449b5c739c137301f6fd364, new_rev=%(subm_rev)s)
remote: *** cvs_check: `trunk/repo/.gitmodules'
remote:   DEBUG: subproject entry ignored: subm
remote: DEBUG: post_receive_one(ref_name=refs/heads/master
remote:                         old_rev=7a373b536b65b600a449b5c739c137301f6fd364
remote:                         new_rev=%(subm_rev)s)
remote: DEBUG: update base: 7a373b536b65b600a449b5c739c137301f6fd364
remote: DEBUG: Content-Type: text/plain; charset="us-ascii"
remote: MIME-Version: 1.0
remote: Content-Transfer-Encoding: 7bit
remote: From: Test Suite <testsuite@adacore.com>
remote: To: git-hooks-ci@example.com
remote: Bcc: file-ci@gnat.com
remote: Subject: [repo] Add submodule subm
remote: X-ACT-checkin: repo
remote: X-Git-Refname: refs/heads/master
remote: X-Git-Oldrev: 7a373b536b65b600a449b5c739c137301f6fd364
remote: X-Git-Newrev: %(subm_rev)s
remote:
remote: commit %(subm_rev)s
remote: Author: Joel Brobecker <brobecker@adacore.com>
remote: Date:   %(author_date)s
remote:
remote:     Add submodule subm
remote:
remote: Diff:
remote: ---
remote:  .gitmodules |    3 +++
remote:  subm        |    1 +
remote:  2 files changed, 4 insertions(+)
remote:
remote: diff --git a/.gitmodules b/.gitmodules
remote: new file mode 100644
remote: index 0000000..%(gitmodules_short_hash)s
remote: --- /dev/null
remote: +++ b/.gitmodules
remote: @@ -0,0 +1,3 @@
remote: +[submodule "subm"]
remote: +	path = subm
remote: +	url = %(TEST_DIR)s/bare/subm.git
remote: diff --git a/subm b/subm
remote: new file mode 160000
remote: index 0000000..8adf3db
remote: --- /dev/null
remote: +++ b/subm
remote: @@ -0,0 +1 @@
remote: +Subproject commit 8adf3dbfb04e35b0322bdcc12e96d1493f6e4502
To ../bare/repo.git
   7a373b5..%(short_subm_rev)s  master -> master
""" % {'subm_rev' : subm_rev,
       'short_subm_rev' : subm_rev[0:7],
       'author_date' : author_date,
       'gitmodules_short_hash' : gitmodules_hash[:7],
       'TEST_DIR' : TEST_DIR,
      }

        self.assertEqual(expected_out, p.cmd_out, p.image + '\n\n\n Expected:\n' + expected_out)