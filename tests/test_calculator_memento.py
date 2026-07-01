from app.calculator_memento import Memento, Caretaker


def test_memento_stores_copy():
    state = [1, 2, 3]
    memento = Memento(state)
    state.append(4)
    assert memento.state == [1, 2, 3]


def test_undo_empty():
    assert Caretaker().undo([1]) is None


def test_redo_empty():
    assert Caretaker().redo([1]) is None


def test_save_and_undo():
    c = Caretaker()
    c.save([1])
    assert c.undo([1, 2]) == [1]


def test_undo_then_redo():
    c = Caretaker()
    c.save(["a"])
    assert c.undo(["a", "b"]) == ["a"]
    assert c.redo(["a"]) == ["a", "b"]


def test_save_clears_redo():
    c = Caretaker()
    c.save([1])
    c.undo([1, 2])
    c.save([3])
    assert c.redo([3]) is None