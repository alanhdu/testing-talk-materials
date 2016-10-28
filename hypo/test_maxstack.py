from hypothesis import given
from hypothesis.strategies import integers, lists, none, one_of


class MaxStack():
    def __init__(self):
        self.m = []
        self.stack = []

    def max(self):
        return self.m[-1]

    def push(self, x):
        self.stack.append(x)
        if not self.m or self.m[-1] <= x:
            self.m.append(x)

    def pop(self):
        x = self.stack.pop()
        if self.m and x == self.m[-1]:
            self.m.pop()
        return x

    def __len__(self):
        return len(self.stack)


@given(lists(one_of(integers(), none())))
def test_max_stack(xs):
    stack = MaxStack()
    count = 0
    for x in xs:
        if x is None:
            if len(stack) > 0:
                count -= 1
                result = stack.pop()
        else:
            stack.push(x)
            count += 1

        if len(stack) > 0:
            assert stack.max() == max(stack.stack)

        assert len(stack) == count
