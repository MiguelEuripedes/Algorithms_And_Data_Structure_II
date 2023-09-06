from avl_class import AVLTree
from BST import BST
import timeit

class Autocompleter:
    """
    This class implements the word autocompleter.

    Based on a given prefix, it returns a list of words that starts with that prefix.
    
    Input: 
    - prefix: The prefix to be searched.

    output:
    - list of words in the corpus that starts with the given prefix.

    """
    def __init__(self, corpus, prefix) -> None:

        self.corpus = corpus
        self.prefix = prefix

    def avl_autocompleter_search(self):
        """
        This method uses the AVL tree to search for the words.

        Output:
            - list of words in the corpus that starts with the given prefix.
            - list of the time to insert each words in the AVL tree.
            - Time to search for the words in the AVL tree.
            - And the avl height.
        """
        # Create AVL tree
        avl = AVLTree()
        avl_insertion_times = []
        # Inserting words into the AVL tree
        for word in self.corpus.words:
            avl_insertion_startime = timeit.default_timer()
            avl.add(word)
            avl_insertion_endtime = timeit.default_timer()
            
            avl_insertion_time = avl_insertion_endtime - avl_insertion_startime
            avl_insertion_times.append(avl_insertion_time)

        # Starting the word search
        start = timeit.default_timer()
        resultado = avl.search_with_prefix(self.prefix)
        end = timeit.default_timer()
        search_time = end - start

        # display the search results
        return resultado, avl_insertion_times, search_time, avl.get_height()

    def list_autocompleter_search(self):
        """
        Returns a list of words that starts with a given prefix and the processing time.

        Output:
            - list of words in the corpus that starts with the given prefix.
            - Lits of the Time to insert each words in the list.
            - Time to search for the words in the list.
        """

        # Create a list of words for comparison
        words_list = []
        list_insertion_times = []

        # Inserting words into the list
        for word in self.corpus.words:
            list_insertion_startime = timeit.default_timer()
            words_list.append(word)
            list_insertion_endtime = timeit.default_timer()

            list_insertion_time = list_insertion_endtime - list_insertion_startime
            list_insertion_times.append(list_insertion_time)

        # Starting the word search
        start = timeit.default_timer()
        resultado = self._list_search_with_prefix(self.prefix, words_list)
        end = timeit.default_timer()

        search_time = end - start

        # display the search results
        return resultado, list_insertion_times, search_time
    
    def _list_search_with_prefix(self, prefix, words_list):
        """
        Returns a list of words that starts with a given prefix.
        """
        resultado = []
        for word in words_list:
            if word.startswith(prefix):
                resultado.append(word)
        return resultado
    
    def bst_autocompleter_search(self):
        """
        This method uses the BST to search for the words.

        Output:
            - list of words in the corpus that starts with the given prefix.
            - list of the time to insert each words in the AVL tree.
            - Time to search for the words in the AVL tree.
            - And the avl height.
        """
        # Create AVL tree
        bst = BST()
        bst_insertion_times = []
        # Inserting words into the AVL tree
        for word in self.corpus.words:
            bst_insertion_startime = timeit.default_timer()
            bst.add(word)
            bst_insertion_endtime = timeit.default_timer()
            
            bst_insertion_time = bst_insertion_endtime - bst_insertion_startime
            bst_insertion_times.append(bst_insertion_time)

        # Starting the word search
        start = timeit.default_timer()
        resultado = bst.seach_prefix_word(self.prefix)
        end = timeit.default_timer()
        search_time = end - start

        # display the search results
        return resultado, bst_insertion_times, search_time, bst.get_height()
    

    def autocompleter_print_result(self, prefix, resultado, list_insertion_times, search_time, avl_height=None, name=None):
        """
        Prints the results of the autocompleter.
        Including list of word, time of insertion and time of search.
        """

        print("\n - Resultado(s) da busca por prefixo: ", prefix, "\n")

        print(" ========== [LISTA DE PALAVRAS ENCONTRADAS] ========= \n")
        print(resultado) 

        print("\n ============== [ANALISE DE DESEMPENHO] ============= \n")
        
        total_insertion_time = sum(list_insertion_times)
        avg_insertion_time = total_insertion_time / len(list_insertion_times)
        
        if avl_height != None:
            print(" - [TIME] Tempo de insercao total ({}): {}".format(name, total_insertion_time))
            print(" - [TIME] Tempo de insercao medio ({}): {}".format(name, avg_insertion_time))
            print('\n - [TIME] Tempo de busca ({}): {}'.format(name, search_time))
            print(" - Altura da arvore: %.0f" % (avl_height))
        else:
            print(" - [TIME] Tempo de insercao total ({}): {}".format(name, total_insertion_time))
            print(" - [TIME] Tempo de insercao medio ({}): {}".format(name, avg_insertion_time))
            print(' - [TIME] Tempo de busca ({}): {}'.format(name, search_time))

        print("\n ==================================================== \n\n\n\n\n")


    