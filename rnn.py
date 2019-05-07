# this is the file in which all of the RNN and text generation work is defined

# first, import what we need
from textgenrnn import textgenrnn
# these are the weights for the RNN, they are stored in the same folder as the files
textgen = textgenrnn(weights_path='poetry5_weights.hdf5',
                vocab_path='poetry5_vocab.json',
                config_path='poetry5_config.json')

# this function will trim a multi-line file of generated poetry to just the second line.
def trim_results(file_name):
    f_read = open(file_name, 'r')       # the text is generated to a file, so first we open the file
    file_text = f_read.read().strip()   # then we add the text to a variable we can work with easily
    print(file_text)
    idx = file_text.find('\n')          # to get to the first line break
    print(idx)
    subset = file_text[idx + 1:]        # make a subset that deletes everything before the first line break
    print(subset)
    idx2 = subset.find('\n')            # now for the second line break
    print(idx2)
    subset2 = subset[:idx2]             # now a second subset that deletes everything after the second line break
    print(subset2)
    f_read.close()                      # the text in the file itself has not been altered
    return subset2                      # returns the subset

# this function will generate a file of poetry, trim it, then return the single line
def seed_to_line(seed, file):       # we input the seed word for the prefix and the file for the text generation
    n = 1                           # we are making one generation
    max_gen_length = 250            # generates 250 characters
    textgen.generate_to_file(file, temperature=0.8,     # this is a function within textgenrnn
                         prefix=seed,
                         n=n,
                         max_gen_length=max_gen_length)
    line = trim_results(file)
    return line


if __name__ == "__main__":          # and then everything after this is just some testing I did along the way

    seed_word = "imagination"

    test1 = seed_to_line1(seed_word, file="line1.txt")
    test2 = seed_to_line2(seed_word, file="line2.txt")
    test3 = seed_to_line3(seed_word, file="line3.txt")
    print("FIRST LINE")
    print(test1)
    print("SECOND LINE")
    print(test2)
    print("THIRD LINE")
    print(test3)


