for sym in punctuations:
        file_contents.replace(sym,'')
    frequencies = {}
    file_contents = file_contents.split()
    for word in file_contents:
        if word not in uninteresting_words:
            frequencies[word] = file_contents.count(word)
