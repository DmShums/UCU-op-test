def dyvo_insert(sentence, flag):
    """
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті","ки")
    'Диво кит кота по хвилях катав - диво кит у воді, кіт на диво киті'
    """
    buf=""
    sentence=sentence.lower()
    for i in sentence.split(" "):
        if i[0:2]==flag:
            buf+="диво "+i+" "
        else:
            buf+=i+" "
    return buf.capitalize().strip()
if __name__ == "__main__":
    import doctest
    doctest.testmod()