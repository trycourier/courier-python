# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MergeAlgorithm(str, enum.Enum):
    REPLACE = "replace"
    NONE = "none"
    OVERWRITE = "overwrite"
    SOFT_MERGE = "soft-merge"

    def visit(
        self,
        replace: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        overwrite: typing.Callable[[], T_Result],
        soft_merge: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MergeAlgorithm.REPLACE:
            return replace()
        if self is MergeAlgorithm.NONE:
            return none()
        if self is MergeAlgorithm.OVERWRITE:
            return overwrite()
        if self is MergeAlgorithm.SOFT_MERGE:
            return soft_merge()
