def cleaning(date, *args):
    print(args)
    staffs = ''
    for person in args:
        staffs = staffs + '「' + person + '」'

    print(date + 'の清掃担当者は' + staffs + 'です')


cleaning('12月3日', '山本', '三浦')
cleaning('12月4日', '杉山', '田中', '井口')



def cleaning(date, **kwargs):
    print(kwargs)
    place_person = ''
    for place, person in kwargs.items():
        place_person = place_person + place + ':' + person + ' '

    print(date + 'の清掃担当者は ' + place_person + 'です')
cleaning('12月3日', トイレ='山本', 休憩室='三浦')
