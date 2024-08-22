inp = """
Khi Ô Mã Nhi dẫn đoàn thuyền tiến vào sông Bạch Đằng nhân lúc nước lớn, thủy quân nhà Trần tràn ra giao chiến, rồi giả thua chạy vào sâu bên trong. Ô Mã Nhi trúng kế khích tướng nên thúc quân ra nghênh chiến, các tướng Phàn Tham Chính, Hoạch Phong cũng ra tiếp ứng. Khi thuyền quân Nguyên đã vào sâu bên trong sông Bạch Đằng, tướng Nguyễn Khoái dẫn các quân Thánh Dực ra khiêu chiến và nhử quân Nguyên tiến sâu vào khúc sông đã đóng cọc, trong khi quân Trần đợi cho thủy triều xuống mới quay thuyền lại và đánh thẳng vào đội hình địch. Bình chương Áo Lỗ Xích của Nguyên Mông đã bị bắt sống trong cuộc chiến đấu quyết liệt của quân Thánh Dực.
Thủy quân Đại Việt từ Hải Đông - Vân Trà từ các phía Điền Công, Gia Đước, sông Thái, sông Giá nhanh chóng tiến ra sông Bạch Đằng, với hàng trăm chiến thuyền cùng quân lính các lộ dàn ra trên sông và dựa vào Ghềnh Cốc thành một dải thuyền chặn đầu thuyền địch ngang trên sông. Trong lúc thủy chiến đang diễn ra dữ dội thì đoàn chiến thuyền của hai vua Trần đóng ở vùng Hiệp Sơn (Kinh Môn, Hải Dương) bên bờ sông Giáp (sông Kinh Thầy, vùng Kinh Môn, Hải Dương) làm nhiệm vụ đánh cầm chừng và cản bước tiến của địch, cũng tấn công từ phía sau khiến quân Nguyên càng lúng túng và tổn thất rất nặng. Theo Đại Việt Sử ký Toàn thư, "nước sông do vậy đỏ ngầu cả". Bị bất lợi hoàn toàn, rất nhiều thuyền chiến của quân Nguyên bị cháy rụi
"""
inp0 = """
Khi Ô Mã Nhi dẫn đoàn thuyền tiến vào sông Bạch Đằng nhân lúc nước lớn, thủy quân nhà Trần tràn ra giao chiến, rồi giả thua chạy vào sâu bên trong. Ô Mã Nhi trúng kế khích tướng nên thúc quân ra nghênh chiến, các tướng Phàn Tham Chính, Hoạch Phong cũng ra tiếp ứng. Khi thuyền quân Nguyên đã vào sâu bên trong sông Bạch Đằng, tướng Nguyễn Khoái dẫn các quân Thánh Dực ra khiêu chiến và nhử quân Nguyên tiến sâu vào khúc sông đã đóng cọc, trong khi quân Trần đợi cho thủy triều xuống mới quay thuyền lại và đánh thẳng vào đội hình địch. Bình chương Áo Lỗ Xích của Nguyên Mông đã bị bắt sống trong cuộc chiến đấu quyết liệt của quân Thánh Dực.
Thủy quân Đại Việt từ Hải Đông - Vân Trà từ các phía Điền Công, Gia Đước, sông Thái, sông Giá nhanh chóng tiến ra sông Bạch Đằng, với hàng trăm chiến thuyền cùng quân lính các lộ dàn ra trên sông và dựa vào Ghềnh Cốc thành một dải thuyền chặn đầu thuyền địch ngang trên sông. Trong lúc thủy chiến đang diễn ra dữ dội thì đoàn chiến thuyền của hai vua Trần đóng ở vùng Hiệp Sơn (Kinh Môn, Hải Dương) bên bờ sông Giáp (sông Kinh Thầy, vùng Kinh Môn, Hải Dương) làm nhiệm vụ đánh cầm chừng và cản bước tiến của địch, cũng tấn công từ phía sau khiến quân Nguyên càng lúng túng và tổn thất rất nặng. Theo Đại Việt Sử ký Toàn thư, "nước sông do vậy đỏ ngầu cả". Bị bất lợi hoàn toàn, rất nhiều thuyền chiến của quân Nguyên bị cháy rụi
Bị tấn công tới tấp trên sông, một số cánh quân Nguyên bỏ thuyền chạy lên bờ sông bên trái của Yên Hưng để tìm đường trốn thoát, nhưng vừa lên tới bờ họ lại rơi vào ổ phục kích của quân Trần, bị chặn đánh kịch liệt. Trời về chiều khi giao tranh sắp kết thúc, Ô Mã Nhi cùng với binh lính dưới quyền chống cự tuyệt vọng trước sự tấn công của quân Trần, vì quân Nguyên của Thoát Hoan không tới cứu viện, nên đạo quân này hoàn toàn bị quân Trần tiêu diệt. Theo Nguyên sử, truyện của Phàn Tiếp chép rằng kịch chiến xảy ra từ giờ mão đến giờ dậu, tức là từ sáng kéo dài đến chiều tối mới kết thúc. Nguyên Sử có chép về tướng Nguyên Phàn Tiếp: "Tiếp cùng Ô Mã Nhi đem quân thủy trở về, bị giặc đón chặn. Triều sông Bạch Đằng xuống, thuyền Tiếp mắc cạn. Thuyền giặc dồn về nhiều, tên bắn như mưa. Tiếp hết sức đánh từ giờ mão đến giờ dậu. Tiếp bị thương, rớt xuống nước. Giặc móc lên bắt, dùng thuốc độc giết".
"""
inp1 = """
Ngày xửa ngày xưa, có hai chị em cùng cha khác mẹ tên là Tấm và Cám. Mẹ Tấm mất sớm, còn cha Tấm cưới thêm mẹ Cám, cha Tấm vô cùng hết mực yêu thương cô, nhưng rồi ông bệnh nặng, không lâu sau đó thì qua đời. Tấm phải sống chung với dì ghẻ là mẹ của Cám. Bà mẹ ghẻ là người cay nghiệt, hàng ngày bắt Tấm phải làm hết mọi công việc trong nhà còn Cám thì ngược lại được lêu lổng vui chơi tối ngày.
Một hôm bà mẹ bảo 2 chị em Tấm và Cám ra đồng đi bắt cá. Bà mẹ dặn: “Hễ đứa nào bắt được nhiều cá hơn sẽ được thưởng”. Tấm vâng lời dặn của mẹ, chăm chỉ siêng năng bắt cá, chẳng chốc mà giỏ cá đã đầy, còn Cám mải rong chơi nên đã xế chiều rồi mà Cám vẫn chưa bắt được con nào. Thấy chị Tấm bắt được nhiều cá, Cám mới nảy ra ý định bảo Tấm: Chị Tấm ơi chị Tấm. Đầu chị lấm, chị hụp cho sâu kẻo về mẹ mắng.
Tấm tin lời em mình nên để giỏ cá nhờ em coi, lội xuống ao gội đầu. Trên bờ Cám đã trút hết giỏ cá của Tấm vào giỏ mình rồi chạy về nhà trước. Khi Tấm bước lên bờ thì giỏ cá không còn. Tấm ngồi khóc nức nở thì bỗng đột nhiên ông Bụt hiện lên hỏi: Tại sao con khóc? Tấm kể hết sự tình xảy ra cho ông Bụt nghe, ông Bụt bảo Tấm tìm xem trong giỏ còn con nào không thì còn duy nhất một con cá bống.
Ông Bụt mới cất lời: Thôi con hãy nín đi. Con đem con cá bống này về bỏ xuống giếng nuôi, mỗi ngày đem cơm cho bống ăn. Khi cho ăn con nhớ gọi bống: “Bống bống bang bang, Lên ăn cơm vàng cơm bạc nhà ta, chớ ăn cơm hẩm cháo hoa nhà người.” Nói xong Bụt biến mất. Tấm nghe lời Bụt dặn nên đem Bống về bỏ xuống giếng nuôi. Hàng ngày cứ đến bữa Tấm lại mang cơm ra cho bống, hai bát cơm thì Tấm chỉ ăn một, để dành một bát lại cho cá bống. Chẳng bao lâu sau, cá bống đã lớn nhanh như thổi.
Thấy Tấm ngày ngày đem cơm ra giếng, dì ghẻ mới đem lòng sinh nghi, sai Cám rình xem thế nào. Cám về kể hết mọi chuyện cho mẹ biết. Sáng ngày hôm sau mẹ ghẻ cho Tấm đi chăn trâu ở đồng xa, bà ngọt ngào dặn Tấm rằng: Con ơi, đồng làng mình cấm chăn trâu. Con đi chăn trâu thì chăn đồng xa, chớ chăn đồng nhà làng bắt mất trâu. Tấm nghe lời mẹ nên dẫn trâu đi thật xa. Ở nhà mẹ con Cám ra giếng gọi y như Tấm hay gọi mỗi ngày, cá nghe tiếng trồi lên miệng giếng, hai mẹ con Cám bắt bống đem làm thịt.
Đến chiều chăn trâu về, Tấm đem cơm ra giếng kêu mà không thấy Bống lên, chỉ thấy nổi lên một cục máu đỏ. Thấy vậy Tấm ngồi khóc nức nở, Bụt hiện lên và hỏi: Làm sao con khóc? Tấm lại kể hết cho Bụt nghe, lúc này Bụt mới bảo: Bống của con đã bị người ta ăn thịt rồi. Thôi con hãy nín đị! Về nhà lượm lấy xương cá bỏ vào bốn cái hũ và chôn dưới bốn chân giường.
Tấm nghe lời vào nhà tìm xương bống, nhưng tìm mãi không thấy đâu. Bỗng có con gà ở đâu chạy ra: “cục ta cục tác, cho ta nắm thóc, ta bới xương cho”. Tấm lấy nắm thóc cho gà ăn, gà vào trong bếp, bới đống tro ra thì thấy xương bống ở đó. Tấm nhặt lấy đem bỏ vào 4 lọ chôn bốn chân giường. Ít lâu sau nhà Vua mở hội, mọi người nô nức đi xem hội. Mẹ con Cám chuẩn bị đi từ rất sớm, Tấm xin mẹ cho đi xem cùng thì dì ghẻ trộn một đấu thóc với một đấu gạo rồi bắt Tấm ngồi nhặt, khi nào nhặt xong thì mới được đi xem hội. Tấm lại khóc nức nở.
Bụt lại hiện lên và hỏi: Làm sao con khóc? Tấm kể rõ sự tình cho Bụt nghe, Bụt sai một đàn chim sẻ xuống nhặt cho Tấm, chỉ một loáng một cái là đã xong. Nhưng Tấm không có quần áo đẹp đi xem hội, thế là cô lại ôm mặt khóc. Bụt lại hiện lên: Làm sao con khóc?
Tấm sụt sùi: Quần áo con rách rưới thế này sao có thể đi xem hội được? Bụt đáp: Con hãy đào bốn hũ chôn ở bốn chân giường lên đi. Tấm nghe lời vào đào bốn hũ lên, hũ thứ nhất mở ra là một bộ váy áo đẹp rực rỡ, hũ thứ hai mở ra là một đôi giày thêu rất đẹp, hũ thứ 3 là một con ngựa nhỏ xíu, nhưng kì lạ là khi đặt xuống đất, con ngựa bỗng chốc biến thành ngựa thật, hũ cuối cùng là một yên cương vững chắc. Tấm vui mừng khôn xiết, vội thay đồ rồi lên đường tiến kinh. Ngựa phóng một lúc đã tới kinh thành, nhưng chẳng may trên đường đi qua chỗ lội, Tấm đã vô tình đánh rơi một chiếc giày không kịp nhặt. Đến hội Tấm lấy khăn gói chiếc giày còn lại và chen vào biển người.
Giữa lúc ấy, đoàn quân hộ tống nhà Vua đi qua chỗ lầy mà Tấm đánh rơi mất giày, hai con voi ngự đầu đàn cứ cắm đầu xuống, không chịu đi, vua cho lính xem xét thì tìm ra được một chiếc giày, nhà Vua đưa lên ngắm nghía: “Giày đẹp thế này, hẳn là người đi nó cũng rất đẹp”. Nhà vua ra lệnh cho tất cả đàn bà con gái đi trẩy hội thử giày, nếu ai đi vừa chiếc giày thì sẽ lấy về làm vợ. Ai ai cũng nô nức đến thử giày nhưng không một ai vừa, mẹ con Cám cũng qua thử nhưng không được, đến lượt Tấm, dì ghẻ mới bĩu môi: “Chuông khánh còn chẳng ăn ai. Nữa là mảnh chĩnh mảnh chai bờ rào”
Nhưng trái lại, khi Tấm thử giày, chiếc giày vừa như in, nàng đưa nốt chiếc thứ hai đang cầm trong tay thì đúng là một đôi, quân lính reo hò, nhà Vua thấy thế thì mừng khôn xiết, vội cho người rước nàng về cung. Từ ngày đó mẹ con Cám căm giận lắm, nhân ngày giỗ cha, Tấm xin phép nhà vua về nhà để làm giỗ. Thấy Tấm về mẹ con Cám sẵn bụng không ưa nên đã bày mưu giết Tấm. Mẹ ghẻ bảo Tấm: Nay là ngày giỗ cha con, con hãy trèo lên cây cau hái xuống cúng cha
Tấm vâng lời trèo lên cây cau thì ở dưới bà mẹ ghẻ đốn gốc, Tấm thấy cây rung rung mới hỏi. Dì ơi dì làm gì dưới đó thế ạ? Dì ghẻ trả lời: Gốc này nhiều kiến quá, dì bắt kiến cho nó khỏi đốt con. Tấm ngã xuống ao chết chìm. Bà mẹ ghẻ đem quần áo của Tấm cho Cám mặc và về cung nói dối với Vua rằng. Chị Tấm không may rớt xuống ao chết. Nay Cám là em vào thế chị. Nhà Vua giận dữ nhưng không nói lời nào. Tấm chết đi biến thành con chim Vàng Anh, bay vào cung vua. Một lần Cám đang giặt áo cho nhà vua, bỗng nghe tiếng hót: “Giặt áo chồng tao thì giặt cho sạch. Phơi áo chồng tao phơi lao phơi sào. Chớ phơi bờ rào rách áo chồng tao”
Cám nghe thấy thế sợ lắm,Vàng Anh ở trong cung thì hót líu lo, nhà Vua đi đâu Vàng Anh bay theo đó, thấy chim quyến luyến theo mình Vua bảo: “Vàng ảnh vàng anh, có phải vợ anh chui vào tay áo” Chim bay đến đậu trên tay nhà vua rồi chui vào tay áo. Từ ngày đó nhà vua chỉ chăm lo cho chim, làm cho chim một cái chuồng bằng vàng, ngày ngày chăm sóc chim. Cám thấy thế tức lắm về nhà hỏi ý mẹ, bà mẹ ghẻ xúi Cám bắt chim ăn thịt, lông chim mang đem chôn vào góc vườn, nhà vua biết được chuyện thì giận lắm. Góc vườn chỗ chôn lông chim Vàng Anh mọc ra hai cây xoan đào tỏa bóng sum suê, nhà vua thấy vậy bèn mắc võng ra nằm nghỉ ngơi.
Cám lại về kể chuyện với mẹ, mẹ Cám lại xúi chặt hai cây xoan đi làm khung cửi, một lần ngồi dệt áo cho nhà Vua, nghe tiếng khung cửi kêu: “Cót ca cót két. Lấy tranh chồng chị. Chị khoét mắt ra”. Cám vô cùng sợ hãi vội sai người mang khung cửi đi đốt, từ đống tro mọc lên một cây thị cành lá xanh tốt um tùm, nhưng lại chỉ có một quả. Một buổi nọ, có một bà cụ đi chợ qua, ngồi nghỉ dưới gốc cây, thấy quả thị bà mới ngỏ: “Thị ơi thị rụng bị bà. Bà để bà ngửi. Chứ bà không ăn”
Bà lão nói xong thị rụng vào bị của bà. Bà đem về nhà để trên gối, chỉ ngửi mà không ăn. Hàng ngày bà ra chợ, về đến nhà là cơm nước đã tinh tươm, nhà cửa sạch sẽ, mấy ngày như vậy, bà sinh nghi. Một lần bà giả vờ đi chợ, nhưng đi đến nửa đường bà lại quay về. Bà đứng bên ngoài cửa nhìn vào thì thấy một cô gái chui ra từ quả thị, dọn dẹp nhà cửa, bà vội vàng chạy vào xé ngay vỏ thị và ôm chầm lấy cô. Bà nhận cô làm con gái.
Từ đó, Tấm ở nhà giúp bà làm việc, bà lão mở quán nước ngay tại nhà, Tấm giúp bà têm trầu cánh phượng, quán mỗi ngày lại một đông khách. Một lần nhà Vua đi qua, dừng chân nghỉ bên quán nước, thấy trầu têm giống như Tấm têm ngày xưa mới ngỏ ý hỏi: Bà ơi, trầu này ai têm mà khéo vậy? Bà lão thật thà: Trầu này con gái bà têm.
Nhà vua muốn gặp con gái của bà, bà mới gọi Tấm ra, vua vui mừng khi nhận ra Tấm nên đã cho người đem nàng về cung. Về đến cung, Tấm kể rõ những sự tình cho nhà vua nghe, nhà vua tức giận cho người đem mẹ con Cám lên xử tội, nhưng Tấm thương cảm, xin nhà vua tha tội. Nhà vua đuổi mẹ con Cám ra ngoài cung, vừa ra khỏi thành, giông tố ập đến, mẹ con Cám bị sét đánh chết giữa đồng. Từ đó nhà Vua và Tấm sống hạnh phúc đến trọn đời.
"""

import google.generativeai as genai
from deep_translator import GoogleTranslator
import requests
api_keys = ["8dd3bfa3f3mshda3845149bb330ep1c4505jsna147eee499b5", "d89a8977f9mshd28e97843a01cf2p158370jsn0cb69019b238", "8eacc0c16dmshb79a0fe65bc3344p14e02ajsn29bf84e2e8b9"] #"8dd3bfa3f3mshda3845149bb330ep1c4505jsna147eee499b5", "030c80dc47mshbe06ccceee3100cp18b554jsnc6867b4f1b65", "0c6c1ec218msh58fce662b00a268p1e2172jsn77027176568f"
def summarizer(sentence, key):
    url = "https://chatgpt-api8.p.rapidapi.com/"
    payload = [
        {
            "content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
            "role": "system"
        },
        {
            "content": "Bạn hãy chọn và output 1 câu duy nhất diễn tả một hành động đặc sắc nhất trong đoạn sau:\n" + sentence,
            "role": "user"
        }
    ]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data["text"]
    translator = GoogleTranslator(source='vi', target='en')
    return (translator.translate(data['text']))

def gemini(ques):
    genai.configure(api_key="AIzaSyCfM6NvU3tQ_pr7gepDw02PYVTwIR6GjOM")
    model = genai.GenerativeModel('gemini-1.5-flash')
    a = (model.generate_content(ques))
    return a.candidates[0].content.parts[0].text

def texttoimage(message, key):
    url = "https://open-ai21.p.rapidapi.com/texttoimage2"
    payload = { "text": "Asia:" + message }
    headers = {
    	"x-rapidapi-key": key,
    	"x-rapidapi-host": "open-ai21.p.rapidapi.com",
    	"Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response)
    return response.json()["generated_image"]

paragraphs = inp.split("\n")
images = []
i = 0
while i < len(paragraphs):
    if paragraphs[i] == "":
        paragraphs.pop(i)
    else:
        plchd = summarizer(paragraphs[i], api_keys[i % len(api_keys)])
        plchd = gemini("Bạn hãy output 1 câu duy nhất bản dịch tiếng anh của câu văn sau:\n" + plchd)
        images.append(texttoimage(plchd, api_keys[(i - 1) % len(api_keys)]))
        print(plchd, images[i])
        i += 1
print(paragraphs)
print(images)