from support import *

class TestRun(TestCase):
    def test_push_commit_on_master(self):
        """Try pushing commit on master.
        """
        cd ('%s/repo' % TEST_DIR)

        p = Run('git push origin master'.split())
        expected_out = """\
remote: *** cvs_check: `trunk/repo/pck.ads'
To ../bare/repo.git
   f826248..52f1517  master -> master
"""

        self.assertTrue(p.status == 0, p.image)
        self.assertEqual(expected_out, p.cmd_out, p.image)

if __name__ == '__main__':
    runtests()
