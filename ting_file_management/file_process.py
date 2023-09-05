import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    if len(instance.data) > 0:
        if (items["nome_do_arquivo"] == path_file for items in instance.data):
            return None
    instance.enqueue(data)
    sys.stdout.write(f"{data}\n")


def remove(instance):
    if len(instance.data) == 0:
        return sys.stdout.write("Não há elementos\n")
    sys.stdout.write(
        f"Arquivo {instance.dequeue()['nome_do_arquivo']} "
        "removido com sucesso\n"
    )


def file_metadata(instance, position):
    if position not in range(len(instance.data)):
        return sys.stderr.write("Posição inválida\n")
    sys.stdout.write(f"{instance.search(position)}\n")
