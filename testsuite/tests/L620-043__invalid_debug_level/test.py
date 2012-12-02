from support import *
import os

class TestRun(TestCase):
    def test_push(self):
        """Try pushing one single-file commit on master.

        The operation should fail due to either config.debuglevel
        having an invalid value, or GIT_HOOKS_DEBUG_LEVEL having
        an invalid value.
        """
        cd ('%s/repo' % TEST_DIR)

        # Push master to the `origin' remote.
        p = Run('git push origin master'.split())
        expected_out = """\
remote: *** Invalid hooks.debuglevel value: -1 (must be integer >= 0)
remote: error: hook declined to update refs/heads/master
To ../bare/repo.git
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to '../bare/repo.git'
"""

        self.assertTrue(p.status != 0, p.image)
        self.assertEqual(expected_out, p.cmd_out, p.image)

        # Same thing, but with an invalid GIT_HOOKS_DEBUG_LEVEL value.
        self.set_debug_level('true')

        p = Run('git push origin master'.split())
        expected_out = """\
remote: *** Invalid value for GIT_HOOKS_DEBUG_LEVEL: true (must be integer >= 0)
remote: error: hook declined to update refs/heads/master
To ../bare/repo.git
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to '../bare/repo.git'
"""

        self.assertTrue(p.status != 0, p.image)
        self.assertEqual(expected_out, p.cmd_out, p.image)


if __name__ == '__main__':
    runtests()
