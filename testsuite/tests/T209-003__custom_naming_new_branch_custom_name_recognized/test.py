from support import Run, TEST_DIR, TestCase, cd, runtests


class TestRun(TestCase):
    def test_create_branch_custom_name_recognized(self):
        """Create a new branch with a custom reference name.

        This reference name is recognized as a branch by the repository's
        naming scheme.
        """
        cd('%s/repo' % TEST_DIR)

        p = Run('git push origin master:refs/vendor/name/topic'.split())
        expected_out = """\
remote: DEBUG: Content-Type: text/plain; charset="us-ascii"
remote: MIME-Version: 1.0
remote: Content-Transfer-Encoding: 7bit
remote: From: Test Suite <testsuite@adacore.com>
remote: To: git-hooks-ci@example.com
remote: Subject: [repo] Created branch 'name/topic' in namespace 'refs/vendor'
remote: X-Act-Checkin: repo
remote: X-Git-Author: Test Suite <testsuite@adacore.com>
remote: X-Git-Refname: refs/vendor/name/topic
remote: X-Git-Oldrev: 0000000000000000000000000000000000000000
remote: X-Git-Newrev: d065089ff184d97934c010ccd0e7e8ed94cb7165
remote:
remote: The branch 'name/topic' was created in namespace 'refs/vendor' pointing to:
remote:
remote:  d065089... New file: a.
To ../bare/repo.git
 * [new branch]      master -> refs/vendor/name/topic
"""

        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, expected_out)


if __name__ == '__main__':
    runtests()
