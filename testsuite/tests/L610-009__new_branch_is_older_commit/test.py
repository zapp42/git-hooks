from support import *

class TestRun(TestCase):
    def test_push_commit_on_master(self):
        """Try pushing new branch on remote.

        In this testcase, the release-0.1-branch points to a commit
        that's one of the older commits in the "master" branch.
        """
        cd ('%s/repo' % TEST_DIR)

        p = Run('git push origin release-0.1-branch'.split())
        expected_out = """\
remote: *** email notification for new commits not implemented yet.
To ../bare/repo.git
 * [new branch]      release-0.1-branch -> release-0.1-branch
"""

        self.assertTrue(p.status == 0, p.image)
        self.assertEqual(expected_out, p.cmd_out, p.image)

        # Verify that the branch has been created in the remote
        # repository and that it points to the expected commit.

        cd('%s/bare/repo.git' % TEST_DIR)

        p = Run('git show-ref -s release-0.1-branch'.split())
        expected_out = """\
4a325b31f594b1dc2c66ac15c4b6b68702bd0cdf
"""

        self.assertTrue(p.status == 0, p.image)
        self.assertEqual(expected_out, p.cmd_out, p.image)


if __name__ == '__main__':
    runtests()
