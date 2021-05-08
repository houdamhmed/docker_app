f1 = open('Beyond the Wall of Sleep.txt', encoding="utf8")
Beyond= f1.read()
f2 = open('Pride and Prejudice.txt', encoding="utf8")
Pride= f2.read()
Beyond=Beyond.lower().split()
Pride=Pride.lower().split()
w= set(Beyond) & set(Pride)
common_words={'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during'}

for x in common_words:
    w.discard(x)
w= str(w)
import re
new_w = re.sub(r'[^\w\s]','',w)
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

new_w=' '.join(unique_list(new_w.split()))
f1.close()
f2.close()
word_list = new_w.split()
print('The word is : ')
print(new_w)
