from werkzeug.exceptions import HTTPException


class CalibreRuntimeError(Exception):
    """Raise when calibredb command line execution returns a non-zero exit code."""

    def __init__(self, cmd: str, exit_code: int, stdout: str, stderr: str):
        self.cmd = cmd
        self.exit_code = exit_code
        self.stdout = stdout
        self.stderr = stderr

        message = f"{cmd} exited with status {str(exit_code)}.\n\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}"
        super().__init__(message)


class InvalidPayloadError(HTTPException):
    """Raise when HTTP request payload is invalid or missing."""

    code = 400

    def __init__(self, message: str):
        super().__init__(description=message)


class ExistingItemError(Exception):
    pass


class NoItemsError(Exception):
    pass
