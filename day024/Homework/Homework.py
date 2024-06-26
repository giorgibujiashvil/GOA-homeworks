"""დავალება - ასევე განიხილეთ ბატონი ლუკას მიერ შესრულებული ამოცანები, მისი თითოეული ეტაპი ახსენით კომენტარებით: """

#შევქმენით  ფუნქციას
def litres(time):#სახელად ვარქმევთ litres, ფრჩხიბელში კი time
    return int(time * 0.5)
    #რეთურნს ვიყენებთ პრინტის მაგივრად ამიტომ return ინტ იმიტომ რომ გადაქციოს ინტეჯერად და ბოლოს time გამრავლებული 0.5-ზე





#შევქმენით  ფუნქციას
def paperwork(n, m):#სახელად ვარქმევთ paperwork,ფრჩხიბელში კი n, m 
    if n < 0 or m < 0: 
        # თუ n ნაკლებია 0-ზე ან m ნაკლებია 0-ზე
        return 0
    #შემოვატრიალებთ 0-ს
    
    return n * m
#და ბოლოს შემოვატრიალებთ და m-ს გავამრავლებთ n-ზე




#შევქმენით  ფუნქციას
def grow(numbers_list):#სახელად ვარქმევთ grow, ფრჩხიბელში კი numbers_list
    result = 1
    #შევქმენით result ცვლადი და გავუტოლეთ ნულს
    
    #შევქმენით for ციკლი 
    for number in numbers_list: #ამისთვის number ცვლადი number_list-ში 
        #შევქმენით result ცვლადი და გავუტოლეთ result-ი გამრავლებული number ცვლადზე
        result = result * number
    
    return result  #და საბოლოოდ შემოვაბრუნებთ result ცვლადს




#შევქმენით  ფუნქციას
def fake_bin(x):#სახელად ვარქმევთ fake_bin, ფრჩხიბელში კი x
    result = ""  #შევქმენით რესულტ ცვლადი და გავუტოლეთ ორ ფრჩხილს
    
    for char in x:  #ამისთვის char-ი x-ში
        if int(char) < 5:#თუ ინტეჯერი char-ი ნაკლებია 5ზე
            result = result + "0" #შევქმენით result ცვლადი და  გავუტოლეთ  result-ს დამატებული 0-ი
        else:#სხვა
            result = result + "1"
            #შევქმენით result ცვლადი და  გავუტოლეთ  result-ს დამატებული 1-ი
    
    return result
#და ბოლოს შემოვაბრუნეთ result ცვლადი


#შევქმენით  ფუნქციას
def count_by(x, n):#სახელად ვარქმევთ count_by, ფრჩხიბელში კი x, n
    multiples_x = []  # შევქმენით multiples_x ცვლადი და  გავუტოლეთ ორ ბრჩხილს ანუ მომხმარებელი რასაც შემოიტანს ავტომატურად ჩაიწერება
    
    for i in range(x, x * n + 1): #ამისთვის ი რეინჯში იქსი გამრავლებული ენზე და მიმატებული ერთი 
        if i % x == 0: #თუ ი ნაშთიანი გაყოფით გავყოფთ ნულზე უდრის ნულს
            multiples_x.append(i) # multiples_x ცვლადს 
    
    return multiples_x
    #და ბოლოს შემოვაბრუნებთ multiples_x ცვლადს

#შევქმენით  ფუნქციას
def count_by(x, n):#სახელად ვარქმევთ ცount_by, ფრჩხიბელში კი x, n-ს
    return list(range(x, x * n + 1, x))
    #შემოვაბრუნებთ ლისტს, რეინჯ ფუნქციის მეშვეობით კი იქსს გავამრავლებთ ენზე და დავუმატებთ ერთს