def exists_word(word, instance):
    results = []

    for i in range(len(instance)):
        file_info = instance.search(i)
        file_name = file_info["nome_do_arquivo"]
        lines = file_info["linhas_do_arquivo"]

        occurrences = [
            {"linha": j + 1}
            for j, line in enumerate(lines)
            if word.lower() in line.lower()
        ]

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
