from subprocess import run
from typing import List


def FunctionRunner(run=run):
    def handler(cmd: str):
        run(cmd)

    return handler


class ClassRunner:
    def __init__(self, run=run):
        self._run = run

    def __call__(self, cmd: str):
        self._run(cmd)


def SomeHandler(f_run=FunctionRunner(), c_run=ClassRunner()):
    def handler(args: List[str]):
        f_run(" ".join(args))
        c_run(" ".join(args))

    return handler
