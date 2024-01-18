# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RoutingStrategyMethod(str, enum.Enum):
    ALL = "all"
    SINGLE = "single"

    def visit(self, all: typing.Callable[[], T_Result], single: typing.Callable[[], T_Result]) -> T_Result:
        if self is RoutingStrategyMethod.ALL:
            return all()
        if self is RoutingStrategyMethod.SINGLE:
            return single()
