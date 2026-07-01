class Memento:
    """Stores a snapshot of history state."""

    def __init__(self, state):
        # store a copy so later changes don't mutate the snapshot
        self.state = list(state)


class Caretaker:
    """Manages mementos for undo and redo."""

    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, state):
        self._undo_stack.append(Memento(state))
        self._redo_stack.clear()

    def undo(self, current_state):
        if not self._undo_stack:
            return None
        self._redo_stack.append(Memento(current_state))
        memento = self._undo_stack.pop()
        return memento.state

    def redo(self, current_state):
        if not self._redo_stack:
            return None
        self._undo_stack.append(Memento(current_state))
        memento = self._redo_stack.pop()
        return memento.state