import logging

from mir import scm
from mir.commands import base
from mir.tools import checker
from mir.tools.code import MirCode


class CmdTag(base.BaseCommand):
    """
    add tag to commit
    """
    @staticmethod
    def run_with_args(mir_root: str, tag: str) -> int:
        return_code = checker.check(mir_root,
                                    [checker.Prerequisites.IS_INSIDE_MIR_REPO, checker.Prerequisites.IS_CLEAN])
        if return_code != MirCode.RC_OK:
            return return_code
        if not tag:
            logging.error('empty tag')
            return MirCode.RC_CMD_INVALID_ARGS

        repo_git = scm.Scm(root_dir=mir_root, scm_executable='git')
        repo_git.tag(tag)

        return MirCode.RC_OK
