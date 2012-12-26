from support import *

class TestRun(TestCase):
    def test_push_branch_with_merge_commit(self):
        """Try pushing an update to master adding one merge commit.
        """
        cd ('%s/repo' % TEST_DIR)

        # Push master to the `origin' remote.  The delta should be one
        # commit with one file being modified.
        p = Run('git push origin master:topic/resync'.split())
        expected_out = """\
remote: DEBUG: Content-Type: text/plain; charset="us-ascii"
remote: MIME-Version: 1.0
remote: Content-Transfer-Encoding: 7bit
remote: From: Test Suite <testsuite@adacore.com>
remote: To: git-hooks-ci@example.com
remote: Bcc: file-ci@gnat.com
remote: Subject: [repo] Created branch topic/resync
remote: X-ACT-checkin: repo
remote: X-Git-Refname: refs/heads/topic/resync
remote: X-Git-Oldrev: 0000000000000000000000000000000000000000
remote: X-Git-Newrev: ffb05b4a606fdb7b2919b209c725fe3b71880c00
remote:
remote: The branch 'topic/resync' was created pointing to:
remote:
remote:  ffb05b4... Merge topic branch fsf-head.
To ../bare/repo.git
 * [new branch]      master -> topic/resync
"""

        self.assertEqual(p.status, 0, p.image)
        self.assertEqual(expected_out, p.cmd_out, p.image)

if __name__ == '__main__':
    runtests()