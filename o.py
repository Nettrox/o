
def rep(test_str, O):
    var = 'AEIİÖUÜaeıiöüu'
    for ele in var:
        test_str = test_str.replace(ele, O)
    return test_str
 

input_str = "..." #buraya istenen metni ekle
O = "o"
print(rep(input_str, O))
