import pandas as pd 
import numpy as np

df = pd.read_excel("total_data.xls")
df.insert(1, '类别代号', 0)

for i in range(2023):
    if('特殊膳食' in df.iloc[i, 2]):
        df.iloc[i, 1] = 1
        
    elif('乳及其乳制品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 2
        
    elif('饮料' in df.iloc[i, 2]):
        df.iloc[i, 1] = 3
        
    elif('粮食及其制品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 4
        
    elif('食用油脂' in df.iloc[i, 2]):
        df.iloc[i, 1] = 5
        
    elif('调味品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 6
        
    elif('肉制品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 7
        
    elif('方便食品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 8
        
    elif('罐头' in df.iloc[i, 2]):
        df.iloc[i, 1] = 9
        
    elif('冷冻饮品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 10
        
    elif('速冻食品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 11
        
    elif('薯类和膨化食品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 12
        
    elif('糖果' in df.iloc[i, 2]):
        df.iloc[i, 1] = 13
        
    elif('茶叶' in df.iloc[i, 2]):
        df.iloc[i, 1] = 14
    
    elif('酒类' in df.iloc[i, 2]):
        df.iloc[i, 1] = 15
    
    elif('蔬菜' in df.iloc[i, 2]):
        df.iloc[i, 1] = 16
        
    elif('水果' in df.iloc[i, 2]):
        df.iloc[i, 1] = 17
        
    elif('炒货' in df.iloc[i, 2]):
        df.iloc[i, 1] = 18
    
    elif('蛋' in df.iloc[i, 2]):
        df.iloc[i, 1] = 19
        
    elif('可可' in df.iloc[i, 2]):
        df.iloc[i, 1] = 20
        
    elif('食糖' in df.iloc[i, 2]):
        df.iloc[i, 1] = 21
        
    elif('水产' in df.iloc[i, 2]):
        df.iloc[i, 1] = 22
        
    elif('淀粉' in df.iloc[i, 2]):
        df.iloc[i, 1] = 23
    
    elif('焙烤产品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 24
        
    elif('豆及其豆制品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 25
        
    elif('蜂产品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 26
        
    elif('保健食品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 27
        
    elif('食品添加剂' in df.iloc[i, 2]):
        df.iloc[i, 1] = 28
        
    elif('食品相关产品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 29
        
    elif('化妆品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 30
        
    elif('餐饮环节产品' in df.iloc[i, 2]):
        df.iloc[i, 1] = 31
    
    else:
        df.iloc[i, 1] = 32

        
        df.insert(25, '抽检代码', 0)

for i in range(2023):
    if('国抽' in df.iloc[i, 26]):
        df.iloc[i, 25] = 1
    elif('省抽' in df.iloc[i, 26]):
        df.iloc[i, 25] = 2
    elif('市抽' in df.iloc[i, 26]):
        df.iloc[i, 25] = 3

        
df.insert(15, '生产省份代码', 0)

for i in range(2023):
    if(df.iloc[i, 16] == '广东'):
        df.iloc[i, 15] = 1
    elif(df.iloc[i, 16] == '山东'):
        df.iloc[i, 15] = 2
    elif(df.iloc[i, 16] == '江苏'):
        df.iloc[i, 15] = 3
    elif(df.iloc[i, 16] == '河南'):
        df.iloc[i, 15] = 4
    elif(df.iloc[i, 16] == '河北'):
        df.iloc[i, 15] = 5
    elif(df.iloc[i, 16] == '上海'):
        df.iloc[i, 15] = 6
    elif(df.iloc[i, 16] == '浙江'):
        df.iloc[i, 15] = 7
    elif(df.iloc[i, 16] == '陕西'):
        df.iloc[i, 15] = 8
    elif(df.iloc[i, 16] == '湖南'):
        df.iloc[i, 15] = 9
    elif(df.iloc[i, 16] == '重庆'):
        df.iloc[i, 15] = 10
    elif(df.iloc[i, 16] == '福建'):
        df.iloc[i, 15] = 11
    elif(df.iloc[i, 16] == '天津'):
        df.iloc[i, 15] = 12
    elif(df.iloc[i, 16] == '云南'):
        df.iloc[i, 15] = 13
    elif(df.iloc[i, 16] == '四川'):
        df.iloc[i, 15] = 14
    elif(df.iloc[i, 16] == '广西'):
        df.iloc[i, 15] = 15
    elif(df.iloc[i, 16] == '安徽'):
        df.iloc[i, 15] = 16
    elif(df.iloc[i, 16] == '海南'):
        df.iloc[i, 15] = 17
    elif(df.iloc[i, 16] == '江西'):
        df.iloc[i, 15] = 18
    elif(df.iloc[i, 16] == '湖北'):
        df.iloc[i, 15] = 19
    elif(df.iloc[i, 16] == '山西'):
        df.iloc[i, 15] = 20
    elif(df.iloc[i, 16] == '辽宁'):
        df.iloc[i, 15] = 21
    elif(df.iloc[i, 16] == '黑龙江'):
        df.iloc[i, 15] = 22
    elif(df.iloc[i, 16] == '内蒙古'):
        df.iloc[i, 15] = 23
    elif(df.iloc[i, 16] == '新疆'):
        df.iloc[i, 15] = 24
    elif(df.iloc[i, 16] == '甘肃'):
        df.iloc[i, 15] = 25
    elif(df.iloc[i, 16] == '青海'):
        df.iloc[i, 15] = 26
    elif(df.iloc[i, 16] == '贵州'):
        df.iloc[i, 15] = 27
    elif(df.iloc[i, 16] == '吉林'):
        df.iloc[i, 15] = 28
    elif(df.iloc[i, 16] == '宁夏'):
        df.iloc[i, 15] = 29
        
df.insert(18, '抽样单位代码', 0)df.insert(25, '抽检代码', 0)

for i in range(2023):
    if('国抽' in df.iloc[i, 26]):
        df.iloc[i, 25] = 1
    elif('省抽' in df.iloc[i, 26]):
        df.iloc[i, 25] = 2
    elif('市抽' in df.iloc[i, 26]):
        df.iloc[i, 25] = 3

        
df.insert(15, '生产省份代码', 0)

for i in range(2023):
    if(df.iloc[i, 16] == '广东'):
        df.iloc[i, 15] = 1
    elif(df.iloc[i, 16] == '山东'):
        df.iloc[i, 15] = 2
    elif(df.iloc[i, 16] == '江苏'):
        df.iloc[i, 15] = 3
    elif(df.iloc[i, 16] == '河南'):
        df.iloc[i, 15] = 4
    elif(df.iloc[i, 16] == '河北'):
        df.iloc[i, 15] = 5
    elif(df.iloc[i, 16] == '上海'):
        df.iloc[i, 15] = 6
    elif(df.iloc[i, 16] == '浙江'):
        df.iloc[i, 15] = 7
    elif(df.iloc[i, 16] == '陕西'):
        df.iloc[i, 15] = 8
    elif(df.iloc[i, 16] == '湖南'):
        df.iloc[i, 15] = 9
    elif(df.iloc[i, 16] == '重庆'):
        df.iloc[i, 15] = 10
    elif(df.iloc[i, 16] == '福建'):
        df.iloc[i, 15] = 11
    elif(df.iloc[i, 16] == '天津'):
        df.iloc[i, 15] = 12
    elif(df.iloc[i, 16] == '云南'):
        df.iloc[i, 15] = 13
    elif(df.iloc[i, 16] == '四川'):
        df.iloc[i, 15] = 14
    elif(df.iloc[i, 16] == '广西'):
        df.iloc[i, 15] = 15
    elif(df.iloc[i, 16] == '安徽'):
        df.iloc[i, 15] = 16
    elif(df.iloc[i, 16] == '海南'):
        df.iloc[i, 15] = 17
    elif(df.iloc[i, 16] == '江西'):
        df.iloc[i, 15] = 18
    elif(df.iloc[i, 16] == '湖北'):
        df.iloc[i, 15] = 19
    elif(df.iloc[i, 16] == '山西'):
        df.iloc[i, 15] = 20
    elif(df.iloc[i, 16] == '辽宁'):
        df.iloc[i, 15] = 21
    elif(df.iloc[i, 16] == '黑龙江'):
        df.iloc[i, 15] = 22
    elif(df.iloc[i, 16] == '内蒙古'):
        df.iloc[i, 15] = 23
    elif(df.iloc[i, 16] == '新疆'):
        df.iloc[i, 15] = 24
    elif(df.iloc[i, 16] == '甘肃'):
        df.iloc[i, 15] = 25
    elif(df.iloc[i, 16] == '青海'):
        df.iloc[i, 15] = 26
    elif(df.iloc[i, 16] == '贵州'):
        df.iloc[i, 15] = 27
    elif(df.iloc[i, 16] == '吉林'):
        df.iloc[i, 15] = 28
    elif(df.iloc[i, 16] == '宁夏'):
        df.iloc[i, 15] = 29
        
df.insert(18, '抽样单位代码', 0)

area_data = {
        '北京': ['北京','朝阳区', '海淀区', '通州区', '房山区', '丰台区', '昌平区', '大兴区', '顺义区', '西城区', '延庆县', '石景山区', '宣武区', '怀柔区', '崇文区', '密云县',
               '东城区', '门头沟区', '平谷区'],
        '广东':['广东', '龙门', '和平', '连平', '霞山', '连山', '连南', '台山', '恩平', '鹤山', '龙川', '廉江', '乐昌', '罗定', '东源', '四会', '东莞', '广州', '中山', '深圳', '惠州', '江门', '珠海', '汕头', '佛山', '湛江', '河源', '紫金', '肇庆','潮州', '清远', '佛冈', '阳山', '清新', '韶关', '新丰', '揭阳', '阳江', '云浮', '郁南', '茂名', '电白', '化州', '梅州', '汕尾'],
        '山东':['山东', '冠县', '莒南', '荣成', '济南', '济阳', '青岛', '崂山', '临沂', '济宁', '菏泽', '烟台','泰安', '淄博', '潍坊', '日照', '威海', '滨州', '东营', '聊城', '德州', '莱芜', '枣庄'],
        '江苏':['江苏', '六套', '苏州', '徐州', '盐城', '无锡','南京', '南通', '连云', '常州', '扬州', '镇江', '淮安', '泰州', '宿迁'],
        '河南':['河南', '孟州', '商城', '社旗', '中牟', '汝州', '淇滨', '郑州', '南阳', '新乡', '安阳', '洛阳', '信阳','平顶', '周口', '商丘', '开封', '焦作', '解放', '驻马', '濮阳', '三门', '漯河', '许昌', '鹤壁', '济源'],
        '上海':['上海', '松江区', '宝山区', '金山区','嘉定区', '南汇区', '青浦区', '浦东新区', '奉贤区', '闵行区', '徐汇区', '静安区', '黄浦区', '普陀区', '杨浦区', '虹口区', '闸北区', '长宁区', '崇明县', '卢湾区'],
        '河北':[ '河北', '石家', '唐山', '保定', '邯郸', '邢台', '河北区', '沧州', '秦皇岛', '张家', '衡水', '廊坊', '承德'],
        '浙江':['浙江', '温州', '宁波','杭州', '台州', '嘉兴', '金华', '湖州', '绍兴', '舟山', '丽水', '衢州'],
        '陕西':['陕西', '西安', '咸阳', '宝鸡', '汉中', '渭南','安康', '榆林', '商洛', '延安', '铜川'],
        '湖南':[ '湖南', '长沙', '邵阳', '常德', '衡阳', '株洲', '湘潭', '永州', '岳阳', '怀化', '郴州','娄底', '益阳', '张家', '湘西'],
        '重庆':[  '重庆', '江北区', '渝北区', '沙坪坝区', '九龙坡区', '万州区', '永川市', '南岸区', '酉阳县', '北碚区', '涪陵区', '秀山县', '巴南区', '渝中区', '石柱县', '忠县', '合川市', '大渡口区', '开县', '长寿区', '荣昌县', '云阳县', '梁平县', '潼南县', '江津市', '彭水县', '璧山县', '綦江县',
     '大足县', '黔江区', '巫溪县', '巫山县', '垫江县', '丰都县', '武隆县', '万盛区', '铜梁县', '南川市', '奉节县', '双桥区', '城口县'],
        '福建':['福建', '漳州', '泉州','厦门', '福州', '莆田', '宁德', '三明', '南平', '龙岩'],
        '天津':['天津', '和平区', '北辰区', '河北区', '河西区', '西青区', '津南区', '东丽区', '武清区','宝坻区', '红桥区', '大港区', '汉沽区', '静海县', '宁河县', '塘沽区', '蓟县', '南开区', '河东区'],
        '云南':[ '云南', '昆明', '红河', '大理', '文山', '德宏', '曲靖', '昭雄', '楚雄', '保山', '玉溪', '丽江', '临沧', '思茅', '西双', '怒江', '迪庆'],
        '四川':['四川', '成都', '绵阳', '广元', '苍溪', '达州', '南充', '德阳', '广安', '阿坝', '巴中', '遂宁', '内江', '凉山', '攀枝', '乐山', '自贡', '泸州', '雅安', '宜宾', '资阳','眉山', '甘孜'],
        '广西':['广西', '扶绥', '陆川', '宾阳', '桂平', '贵港', '平南', '玉林', '北流', '博白', '兴业', '北海', '南宁', '柳州', '鹿寨', '融安', '桂林', '阳朔', '锦绣', '梧州', '钦州', '来宾', '河池', '百色', '贺州', '崇左',  '防城'],
        '安徽':['安徽', '芜湖', '合肥', '六安', '宿州', '阜阳','安庆', '马鞍', '蚌埠', '淮北', '淮南', '宣城', '黄山', '铜陵', '亳州','池州', '巢湖', '滁州'],
        '海南':['海南', '三亚', '海口', '琼海', '文昌', '东方', '昌江', '陵水', '乐东', '五指山', '保亭', '澄迈', '万宁','儋州', '临高', '白沙', '定安', '琼中', '屯昌'],
        '江西':['江西', '南昌', '赣州', '上饶', '吉安', '九江', '新余', '抚州', '宜春', '景德', '萍乡市', '鹰潭'],
        '湖北':['湖北', '武汉', '宜昌', '襄樊', '荆州', '恩施', '孝感', '黄冈', '十堰', '咸宁', '黄石', '铁山', '仙桃', '随州', '天门', '荆门', '潜江', '鄂州', '神农'],
        '山西':['山西', '河津', '曲沃', '太原', '大同', '运城', '长治', '晋城', '忻州', '临汾', '吕梁', '晋中', '阳泉', '朔州'],
        '辽宁':['辽宁', '大连', '沈阳', '丹东', '辽阳', '葫芦', '锦州', '朝阳', '营口', '鞍山', '抚顺', '阜新', '本溪', '盘锦', '铁岭'],
        '黑龙江':['黑龙', '齐齐', '哈尔', '大庆', '佳木', '双鸭', '牡丹', '鸡西','黑河', '绥化', '鹤岗', '伊春', '大兴', '七台'],
        '内蒙古':['内蒙', '赤峰', '包头', '通辽', '呼和', '乌海', '鄂尔', '呼伦','兴安', '巴彦', '乌兰', '锡林', '阿拉'],
        '贵州':['贵州', '沿河', '贵阳', '黔东', '黔南', '遵义', '黔西', '毕节', '铜仁','安顺', '六盘'],
        '甘肃':['甘肃', '兰州', '天水', '庆阳', '武威', '酒泉', '张掖', '陇南', '白银', '定西', '平凉', '嘉峪', '临夏','金昌', '甘南'],
        '青海':['青海', '西宁', '海西', '海东', '海北', '果洛', '玉树', '黄南'],
        '新疆':['新疆','新疆维吾尔自治区', '乌鲁', '伊犁', '昌吉','石河', '哈密', '阿克', '巴音', '喀什', '克拉', '和田', '阿勒', '吐鲁', '阿拉', '博尔', '五家',
     '克孜', '图木'],
        '吉林':['吉林', '吉林', '长春', '白山', '白城','延边', '松原', '辽源', '通化', '四平'],
        '宁夏':['宁夏', '银川', '吴忠', '中卫', '石嘴山', '固原']
}

for i in range(2023):
    if(type(df.iloc[i, 19]) == str):
        if(df.iloc[i, 19][:2] in area_data['山东']):
            df.iloc[i, 18] = 2
        elif(df.iloc[i, 19][:2] in area_data['广东']):
            df.iloc[i, 18] = 1
        elif(df.iloc[i, 19][:2] in area_data['江苏']):
            df.iloc[i, 18] = 3
        elif(df.iloc[i, 19][:2] in area_data['河南']):
            df.iloc[i, 18] = 4
        elif(df.iloc[i, 19][:2] in area_data['上海']):
            df.iloc[i, 18] = 6
        elif(df.iloc[i, 19][:2] in area_data['河北']):
            df.iloc[i, 18] = 5
        elif(df.iloc[i, 19][:2] in area_data['浙江']):
            df.iloc[i, 18] = 7
        elif(df.iloc[i, 19][:2] in area_data['陕西']):
            df.iloc[i, 18] = 8
        elif(df.iloc[i, 19][:2] in area_data['湖南']):
            df.iloc[i, 18] = 9
        elif(df.iloc[i, 19][:2] in area_data['重庆']):
            df.iloc[i, 18] = 10
        elif(df.iloc[i, 19][:2] in area_data['福建']):
            df.iloc[i, 18] = 11
        elif(df.iloc[i, 19][:2] in area_data['天津']):
            df.iloc[i, 18] = 12
        elif(df.iloc[i, 19][:2] in area_data['云南']):
            df.iloc[i, 18] = 13
        elif(df.iloc[i, 19][:2] in area_data['四川']):
            df.iloc[i, 18] = 14
        elif(df.iloc[i, 19][:2] in area_data['广西']):
            df.iloc[i, 18] = 15
        elif(df.iloc[i, 19][:2] in area_data['安徽']):
            df.iloc[i, 18] = 16
        elif(df.iloc[i, 19][:2] in area_data['海南']):
            df.iloc[i, 18] = 17
        elif(df.iloc[i, 19][:2] in area_data['江西']):
            df.iloc[i, 18] = 18
        elif(df.iloc[i, 19][:2] in area_data['湖北']):
            df.iloc[i, 18] = 19
        elif(df.iloc[i, 19][:2] in area_data['山西']):
            df.iloc[i, 18] = 20
        elif(df.iloc[i, 19][:2] in area_data['辽宁']):
            df.iloc[i, 18] = 21
        elif(df.iloc[i, 19][:2] in area_data['黑龙江']):
            df.iloc[i, 18] = 22
        elif(df.iloc[i, 19][:2] in area_data['内蒙古']):
            df.iloc[i, 18] = 23
        elif(df.iloc[i, 19][:2] in area_data['新疆']):
            df.iloc[i, 18] = 24
        elif(df.iloc[i, 19][:2] in area_data['甘肃']):
            df.iloc[i, 18] = 25
        elif(df.iloc[i, 19][:2] in area_data['青海']):
            df.iloc[i, 18] = 26
        elif(df.iloc[i, 19][:2] in area_data['贵州']):
            df.iloc[i, 18] = 27
        elif(df.iloc[i, 19][:2] in area_data['吉林']):
            df.iloc[i, 18] = 28
        elif(df.iloc[i, 19][:2] in area_data['宁夏']):
            df.iloc[i, 18] = 29
        elif(df.iloc[i, 19][:2] in area_data['北京']):
            df.iloc[i, 18] = 30
    