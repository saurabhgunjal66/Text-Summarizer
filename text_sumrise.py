import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text="""As we all know, a paragraph is a group of sentences that are 
connected and make absolute sense. While writing a long essay or 
letter, we break them into paragraphs for better understanding and
 to make a well-structured writing piece. Paragraph writing on any 
 topic is not only about expressing your thoughts on the given topic, 
 but it is also about framing ideas about the topic and making it 
 convenient for the readers to follow it. In English paragraph writing, 
 it is essential to focus on the writing style, i.e., the flow and 
 connection between the sentences."""


def summraizer(rowdocs):
    stopwords=list(STOP_WORDS)
    #print(stopwords)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(text)
    #print(doc)
    token=[token.text for token in doc]
    #print(token)
    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text] +=1
    #print(word_freq)
    max_freq=max(word_freq.values())
    #print(max_freq)
    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq
    #print(word_freq)

    sent_token=[sent for sent in doc.sents]
    #print(sent_token)
    sent_scores={}
    for sent in  sent_token:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]
   #print(sent_scores)
    select_len=int(len(sent_token)*0.3)
    #print(select_len)
    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    #print(summary)
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)
    # print(text)
    # print(summary)
    # print( " original length",len(text.split(' ')))
    # print( " summary length",len(summary.split(' ')))


    return summary,doc,len(rowdocs.split(' ')),len(summary.split(' '))
    


