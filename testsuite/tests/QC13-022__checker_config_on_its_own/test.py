        # to the refs/meta/config branch. However, the file it points
        # to does not exist in that reference, nor is is added by
        # the commit we're pusing. So this should be rejected.

        p = Run('git push origin meta-config-missing:refs/meta/config'.split())
        expected_out = """\
remote: *** Cannot find style_checker config file: `style.yaml'.
remote: ***
remote: *** Your repository is configured to provide a configuration file to
remote: *** the style_checker; however, this configuration file (style.yaml)
remote: *** cannot be found in commit b2657ce03d358899ce2c779ecf68ac7e8e670dd0.
remote: ***
remote: *** Perhaps you haven't added this configuration file to this branch
remote: *** yet?
remote: error: hook declined to update refs/meta/config
To ../bare/repo.git
 ! [remote rejected] meta-config-missing -> refs/meta/config (hook declined)
error: failed to push some refs to '../bare/repo.git'
"""

        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, expected_out)

        # Do the same as above, but this time with a commit which
        # provides both the config file at the same time it adds
        # the style-checker-config-file option.  This time, the update
        # should be accepted.

remote: *** cvs_check: `--config' `style.yaml' `repo' < `project.config' `style.yaml'
remote: *** # A YaML file (with nothing in it)
remote: ***
remote: X-Git-Newrev: da1ac955c54687142c885c2c5b211cd035c7d53e
remote: commit da1ac955c54687142c885c2c5b211cd035c7d53e
remote:  style.yaml     | 1 +
remote:  2 files changed, 2 insertions(+)
remote: diff --git a/style.yaml b/style.yaml
remote: new file mode 100644
remote: index 0000000..b3fcae2
remote: --- /dev/null
remote: +++ b/style.yaml
remote: @@ -0,0 +1 @@
remote: +# A YaML file (with nothing in it)
   a681757..da1ac95  meta-config -> refs/meta/config