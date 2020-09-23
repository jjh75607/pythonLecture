menu = {
    "떢볶이": "튀김",
    "삼겹살": "소주",
    "피자": "콜라",
    "스팸": "쌀밥",
    "라면": "김치",
}

for i in range(5):
    food = input("[떡볶이, 삼겹살, 피자, 스팸, 라면] 중 좋아하는 것은 ? ")

    if food not in menu.keys():
        print("그런 음식은 없습니다")
    else:
        print("<%s>엔 <%s> 입니다." % (food, menu[food]))
