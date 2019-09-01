import superstack


def run_commands(stack, stack_commands):
    for command in stack_commands:
        if len(command) == 2:
            func, arg = command
            if func.__name__ == 'push':
                stack.push(*arg)
            elif func.__name__ == 'inc':
                stack.inc(*arg)
        else:
            (func,) = command
            if func.__name__ == 'pop':
                stack.pop()


def test_commands_0():
    stack_object = superstack.SuperStack()
    commands = [
        (stack_object.push, (4,)), (stack_object.pop,),
        (stack_object.push, (3,)), (stack_object.push, (5,)),
        (stack_object.push, (2,)), (stack_object.inc, (3, 1)),
        (stack_object.pop,), (stack_object.push, (1,)),
        (stack_object.inc, (2, 2)), (stack_object.push, (4,)),
        (stack_object.pop,), (stack_object.pop,)]
    # Execute the commands
    for result in run_commands(stack_object, commands):
        pass
    assert stack_object.stack == [6, 8]
