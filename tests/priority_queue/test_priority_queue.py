import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Crie uma instância da PriorityQueue
    queue = PriorityQueue()

    # Teste 1: Enqueue e Dequeue de um único item
    queue.enqueue({"qtd_linhas": 7})
    data = queue.dequeue()
    assert data == {"qtd_linhas": 7}
    assert queue.regular_priority.data == []

    # Teste 2: Enqueue de vários itens e Dequeue
    queue.enqueue({"qtd_linhas": 3})
    queue.enqueue({"qtd_linhas": 6})
    queue.enqueue({"qtd_linhas": 2})

    data_2 = queue.dequeue()
    assert data_2 == {"qtd_linhas": 3}
    data_3 = queue.dequeue()
    assert data_3 == {"qtd_linhas": 2}

    # Teste 3: Enqueue e Search
    queue.enqueue({"qtd_linhas": 3})

    data_4 = queue.search(1)
    assert data_4 == {"qtd_linhas": 6}

    # Teste 4: Search com índice inválido
    with pytest.raises(IndexError):
        queue.search(99)
