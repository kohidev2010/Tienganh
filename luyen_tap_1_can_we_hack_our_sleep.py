banner = "REVIEWING VOCABULARIES"
x = banner.center(70, "*")
vocab = input("liệt kê từ vừng: ")
#nhapUser =  input ("nhập từ vựng mà bạn muốn ôn: ")
vocab_1 = ["conspiracy(n)kənˈspɪrəsi/: âm mưu , sự thông đồng , mưu đồ bí mật", "conspirator(n)kənˈspɪrətə(r)/kẻ âm mưu, người tham gia âm mưu", "conspire(v)kənˈspaɪə(r)âm mưu, lập mưu", "conspiratorial(adj)kənˌspɪrəˈtɔːriəl/:có tính chất âm mưu, bí mật"]
i = 0
if vocab==("conspi") or vocab==("c") or vocab==("co")or vocab==("con") or vocab==("cons") or vocab==("consp"):
    for i in range(len(vocab_1)):
        print(vocab_1[i])
vocab_1_detail = input("ban có muốn học kỹ từng từng không :")
if vocab_1_detail == "yes" or vocab_1_detail == "y" o