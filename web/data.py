# coding:utf-8
college_list = (
        ('00', u'机械工程学院'),
        ('01', u'材料科学与工程学院'),
        ('02', u'电气工程学院'),
        ('03', u'信息科学与工程(软件)学院'),
        ('04', u'建筑工程与力学学院'),
        ('05', u'环境与化学工程学院'),
        ('06', u'车辆与能源学院'),
        ('07', u'理学院'),
        ('08', u'经济管理学院'),
        ('09', u'外国语学院'),
        ('10', u'文法学院'),
        ('11', u'公共管理学院'),
        ('12', u'马克思主义学院'),
        ('13', u'艺术与设计学院'),
        ('14', u'体育学院'),
        ('15', u'里仁学院'),
    )

major_list = (
("00", "冶金机械系"),
("01", "机械电子工程系"),
("02", "机电控制工程系"),
("03", "塑性成形工程系"),
("04", "机械制造及其自动化系"),
("05", "机械设计系"),
("06", "机械工学部"),
("07", "工程图学部"),
("08", "机械基础实验中心"),
("09", "工程训练中心"),
("10", "金属系"),
("11", "无机系"),
("12", "材料物理系"),
("13", "高分子系"),
("14", "自动化系"),
("15", "仪器科学与工程系"),
("16", "自动化仪表系"),
("17", "电力工程系"),
("18", "电气工程及其自动化系"),
("19", "生物医学工程系"),
("20", "光电子工程系"),
("21", "计算机教学实验中心与教育技术学系"),
("22", "电子与通信工程系"),
("23", "计算机科学与工程系"),
("24", "软件工程系"),
("25", "土木工程系"),
("26", "工程力学系"),
("27", "建筑环境与能源应用工程系"),
("28", "建筑系"),
("29", "化学工程与工艺系"),
("30", "应用化学系"),
("31", "环境科学与工程系"),
("32", "过程装备与控制工程系"),
("33", "生物技术与工程系"),
("34", "车辆与交通工程系"),
("35", "石油工程系"),
("36", "能源与动力工程系"),
("37", "电子信息科学与技术系"),
("38", "应用数学系"),
("39", "统计学系"),
("40", "信息与计算科学系"),
("41", "应用物理系"),
("42", "工商管理系"),
("43", "经济系"),
("44", "会计系"),
("45", "旅游系"),
("46", "工业工程系"),
("47", "公共事业管理系"),
("48", "电子商务系"),
("49", "英语系"),
("50", "日语系"),
("51", "俄语系"),
("52", "德语系"),
("53", "法语系"),
("54", "法学系"),
("55", "政治学系"),
("56", "文学与新闻传播学系"),
("57", "国际关系"),
("58", "学系"),
("59", "公共事业管理学系"),
("60", "行政管理学系"),
("61", "哲学系"),
("62", "公共管理学院"),
("63", "马克思主义中国化教研部"),
("64", "马克思主义基本原理教研部"),
("65", "思想道德修养教研部"),
("66", "研究生思想政治理论课教研部"),
("67", "工业设计系"),
("68", "环境设计系"),
("69", "公共艺术系"),
("70", "视觉传达系"),
("71", "音乐表演系"),
("72", "雕塑系"),
("73", "基础部"),
("74", "社会体育教研室"),
("75", "公共体育教研室"),
("76", "机械工程系"),
("77", "电气工程系"),
("78", "信息工程系"),
("79", "经济管理系"),
("80", "文法外语系"),
("81", "建筑与环境化学工程系")
)

major_select_list = {
        '00':[
("00", "冶金机械系"),
("01", "机械电子工程系"),
("02", "机电控制工程系"),
("03", "塑性成形工程系"),
("04", "机械制造及其自动化系"),
("05", "机械设计系"),
("06", "机械工学部"),
("07", "工程图学部"),
("08", "机械基础实验中心"),
("09", "工程训练中心")],
        '01':[
("10", "金属系"),
("11", "无机系"),
("12", "材料物理系"),
("13", "高分子系")],
        '02':[
("14", "自动化系"),
("15", "仪器科学与工程系"),
("16", "自动化仪表系"),
("17", "电力工程系"),
("18", "电气工程及其自动化系"),
("19", "生物医学工程系")],
        '03':[
("20", "光电子工程系"),
("21", "计算机教学实验中心与教育技术学系"),
("22", "电子与通信工程系"),
("23", "计算机科学与工程系"),
("24", "软件工程系")],
        '04':[
("25", "土木工程系"),
("26", "工程力学系"),
("27", "建筑环境与能源应用工程系"),
("28", "建筑系")],
        '05':[
("29", "化学工程与工艺系"),
("30", "应用化学系"),
("31", "环境科学与工程系"),
("32", "过程装备与控制工程系"),
("33", "生物技术与工程系")],
        '06':[
("34", "车辆与交通工程系"),
("35", "石油工程系"),
("36", "能源与动力工程系")],
        '07':[
("37", "电子信息科学与技术系"),
("38", "应用数学系"),
("39", "统计学系"),
("40", "信息与计算科学系"),
("41", "应用物理系")],
        '08':[
("42", "工商管理系"),
("43", "经济系"),
("44", "会计系"),
("45", "旅游系"),
("46", "工业工程系"),
("47", "公共事业管理系"),
("48", "电子商务系")],
        '09':[
("49", "英语系"),
("50", "日语系"),
("51", "俄语系"),
("52", "德语系"),
("53", "法语系")],
        '10':[
("54", "法学系"),
("55", "政治学系"),
("56", "文学与新闻传播学系"),
("57", "国际关系"),
("58", "学系"),
("59", "公共事业管理学系"),
("60", "行政管理学系"),
("61", "哲学系")],
        '11':[
("62", "公共管理学院")],
        '12':[
("63", "马克思主义中国化教研部"),
("64", "马克思主义基本原理教研部"),
("65", "思想道德修养教研部"),
("66", "研究生思想政治理论课教研部")],
        '13':[
("67", "工业设计系"),
("68", "环境设计系"),
("69", "公共艺术系"),
("70", "视觉传达系"),
("71", "音乐表演系"),
("72", "雕塑系"),
("73", "基础部")],
        '14':[
("74", "社会体育教研室"),
("75", "公共体育教研室")],
        '15':[
("76", "机械工程系"),
("77", "电气工程系"),
("78", "信息工程系"),
("79", "经济管理系"),
("80", "文法外语系"),
("81", "建筑与环境化学工程系")]
}

authority_list = (
        ('00','冻结的用户'),#仅扫描0号权限组，其他权限全无
        ('01','无法登入'),
        ('02','无法修改个人信息'),
        ('a0',u'查看社团通知'),#a——社团通知
        ('a1',u'发布社团通知'),
        ('a2',u'修改社团通知'),
        ('a3',u'修改社团通知时间'),
        ('b0',u'添加任意部员'),#b——部员成员操作
        ('b1',u'删除任意部员'),
        ('b2',u'修改任意部员信息'),
        ('b3',u'修改任意部员创建时间'),
        ('c0', u'添加任意部长'),#c——部长成员操作
        ('c1', u'删除任意部长'),
        ('c2', u'修改任意部长信息'),
        ('c3', u'修改任意部长创建时间'),
        ('d0', u'添加任意主席'),#d——主席成员操作
        ('d1', u'删除任意主席'),
        ('d2', u'修改任意主席信息'),
        ('d3', u'修改任意主席创建时间'),
        ('e0', u'修改低等级账号权限'),#e——权限操作
        ('e1', u'查看低等级账号权限'),
        ('e2', u'查看任意账号权限'),
)
