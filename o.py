
def rep(test_str, O):
    var = 'AEIİOÖUÜaeıioüu'
    for ele in var:
        test_str = test_str.replace(ele, O)
    return test_str
 

input_str = "knk benzer bir durum bende de var. olmaması için hayatımızı çöpe atmamış olmamız ve bir şeylerin peşinde koşturuyor olmamız gerek sanırım. ikimiz de ileride evsiz kalacağımızı unutmaya çalışarak yaşıyoruz" #buraya istenen metni ekle
O = "o"
print(rep(input_str, O))