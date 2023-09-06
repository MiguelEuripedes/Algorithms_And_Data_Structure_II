
from avl_class import AVLTree, visualize_avl_tree
from pre_processing import Corpus_preprocessing, read_file_corpus
from autocompleter import Autocompleter
import timeit
import csv

# read the corpus
archive_name = r'dicionario.txt'

#text_example = "A Academia Brasileira de Letras é uma instituição literária, fundada em 1897, que reúne alguns dos maiores escritores da literatura brasileira. Seu objetivo é promover a língua e a literatura brasileira, bem como preservar a memória e o legado dos autores nacionais. Entre seus membros ilustres, destacam-se nomes como Machado de Assis, Guimarães Rosa, Clarice Lispector, Jorge Amado, Érico Veríssimo e tantos outros que contribuíram significativamente para a cultura literária do país. A ABL realiza diversas atividades culturais, como palestras, debates, lançamentos de livros e saraus literários, e tem como sede o belo edifício Petit Trianon, localizado no Rio de Janeiro. A cada ano, a instituição premia escritores com o cobiçado Prêmio Machado de Assis, reconhecendo a excelência de suas obras e contribuições para a literatura nacional. Além disso, a ABL desfruta de uma rica biblioteca e é um ponto de encontro para amantes da literatura, proporcionando um espaço único para o intercâmbio de ideias e o enriquecimento cultural. A língua portuguesa e a literatura brasileira têm na Academia Brasileira de Letras uma importante guardiã e promotora de sua história e tradição."

text = read_file_corpus(archive_name) 

# Corpus pre-processing
corpus_processing_startime = timeit.default_timer()
corpus = Corpus_preprocessing(text)
corpus_processing_endtime = timeit.default_timer()
processing_time = corpus_processing_endtime - corpus_processing_startime

# Showing the pre-processing results
print("\n ----------- Resultados Processamento ----------- \n")
numberofwords = len(corpus.words)
if numberofwords > 50:
    print(" - Numero de palavras apos processamento: ", numberofwords)
else:
    print(corpus.words, "\n")
    print("\n Numero de palavras: ", numberofwords)

# Displaying the pre-processing time
print(" - [TIME] Tempo de pre-processamento do CORPUS: %f" % (processing_time))
print("\n")



# Starting the word search
prefix = "lon"

autocompleter = Autocompleter(corpus, prefix)

avl_result, avl_insert_time, avl_search_time, avl_height = autocompleter.avl_autocompleter_search()
bst_result, bst_insert_time, bst_search_time, bst_height = autocompleter.bst_autocompleter_search()
list_result, list_insert_time, list_search_time = autocompleter.list_autocompleter_search()

# Displaying the results
print(" ------------------ Resultados AVL ------------------ ")
autocompleter.autocompleter_print_result(prefix, 
                            avl_result, 
                            avl_insert_time, 
                            avl_search_time, 
                            avl_height, 
                            name="AVL")

print(' ------------------ Resultados BST ------------------ ')
autocompleter.autocompleter_print_result(prefix,
                            bst_result,
                            bst_insert_time,
                            bst_search_time,
                            bst_height, 
                            name="BST")

print(" ----------------- Resultados LISTA ----------------- ")
autocompleter.autocompleter_print_result(prefix,
                            list_result,
                            list_insert_time,
                            list_search_time, 
                            name="LISTA")

# write result csv
from os.path import basename, isfile

results_csv = r'C:\Users\Miguel\Documents\SEMESTRE 2023.2 - Eng.Comp\AEDII\projeto2\AVL\implementations\results\results.csv'

insertionTime_avl = sum(avl_insert_time)
insertionTime_bst = sum(bst_insert_time)
insertionTime_list = sum(list_insert_time)

file_exists = isfile(results_csv)

with open(results_csv, mode='a', newline='') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    if not file_exists:
        results_writer.writerow(['archiveName','numberOfWords', 'processingTime','algorithm','insertionTime', 'searchTime', 'Altura'])
    
    results_writer.writerow([basename(archive_name), numberofwords, processing_time,'AVL', insertionTime_avl, avl_search_time, avl_height])
    results_writer.writerow([basename(archive_name), numberofwords, processing_time,'BST', insertionTime_bst, bst_search_time, bst_height])
    results_writer.writerow([basename(archive_name), numberofwords, processing_time,'List', insertionTime_list, list_search_time, 'N/A'])


