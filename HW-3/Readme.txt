	Feature Extraction for Classicifaction of poetry lines by Shakespeare and Emily Bronte

Example text for explanation: From fairest creatures we desire increase,

Methods implemented in order:
1. Bigrams of text: Each line/ text is taken and bigrams are computed with the characters. This method takes into account of all the 
two letter suffixes and prefixes of the words. 
Bigrams of the text: ['Fr', 'ro', 'om', 'm ', ' f', 'fa', 'ai', 'ir', 're', 'es', 'st', 't ', ' c', 'cr', 're', 'ea', 'at', 'tu', 'ur', 're', 'es', 's ', ' w', 'we', 'e ', ' d', 'de', 'es', 'si', 'ir',
 're', 'e ', ' i', 'in', 'nc', 'cr', 're', 'ea', 'as', 'se', 'e,']

2. Trigrams of text: Each line/ text is taken and trigrams are computed with the characters. This method takes into account of all the 
three letter suffixes and prefixes of the words. 
Trigrams of the text: ['Fro', 'rom', 'om ', 'm f', ' fa', 'fai', 'air', 'ire', 'res', 'est', 'st ', 't c', ' cr', 'cre', 'rea', 'eat', 'atu', 'tur', 'ure', 'res', 'es ', 's w', ' we', 'we
 ', 'e d', ' de', 'des', 'esi', 'sir', 'ire', 're ', 'e i', ' in', 'inc', 'ncr', 'cre', 'rea', 'eas', 'ase', 'se,']

3. Fourgrams of text: Each line/ text is taken and four-grams are computed with the characters. This method takes into account of all the 
four letter suffixes and prefixes of the words. 
Four-grams of the text: ['From', 'rom ', 'om f', 'm fa', ' fai', 'fair', 'aire', 'ires', 'rest', 'est ', 'st c', 't cr', ' cre', 'crea', 'reat', 'eatu', 'atur', 'ture', 'ures', 'res
', 'es w', 's we', ' we ', 'we d', 'e de', ' des', 'desi', 'esir', 'sire', 'ire ', 're i', 'e in', ' inc', 'incr', 'ncre', 'crea', 'reas', 'ease', 'ase,']

Each of the bigrams, trigrams and fourgrams of the text are added as a feature into the dictionary. This significantly contributes for 
enhanced classifictaion.

4. Tokenize the text : The given text is tokenised.
Tokenized text: ['From', 'fairest', 'creatures', 'we', 'desire', 'increase', ',']

5. Compute length of a sentence/ line: Length of each word is calculated and the sum of all the words in the line is returned. The length
of each sentence is added as a feature.
Length of each word : [4, 7, 9, 2, 6, 8, 1]
Sum of all the words : 37
By observing lines from Shakespeare and Bronte, we can infer that Shakespeare's lines are longer than Bronte's. Hence this adds a good 
feature for classification.

6. Remove Punctuations: From the tokenised text, all the punctuations are removed. Normalising the data helps extract important features.
List with Punctuations removed: ['From', 'fairest', 'creatures', 'we', 'desire', 'increase']

7. Length of Bigrams and trigrams of words: From the normalised data, the number of bigrams and trigrams of words for each sentence is calculated.
We can observe that the bigrams and trigrams for Shakespeare's lines are more when compared to Bronte's lines. Thus, this adds as a good feature 
for classification.
Bigrams: [('From', 'fairest'), ('fairest', 'creatures'), ('creatures', 'we'), ('we', 'desire'), ('desire', 'increase')]
Number of bigrams: 5
Trigrams: [('From', 'fairest', 'creatures'), ('fairest', 'creatures', 'we'), ('creatures', 'we', 'desire'), ('we', 'desire', 'increase')]
Number of trigrams: 4

8. Remove Stopwords: Removing the stop words used in English dictionary helps in further cleaning up of the data. This helps to take 
into account the frequency of the words other than the stop words, thus focussing on the actual vocabulary of the author.
List after removing the stopwords: ['From', 'fairest', 'creatures', 'desire', 'increase']

9. Stemming and lowercase conversion: Stemming removes the unwanted suffixes and prefixes and returns the root word. This method normalises the data.
Stemming and Lowercase: Fairest returns fair

This normalised data is given as input to the Classifier to compute the probability of occurance/ frequency of each of the words.






