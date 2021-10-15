#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/3/31 20:17 
# @Author : mayuyang
# @File : goods.py 
# @desc:


import requests
import json
import time


def get_time():
    millis = int(round(time.time() * 1000))
    print(millis)
    return str(millis)


class AddGoods:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json; charset=UTF-8',
        }
        self.cookies = {
            'JSESSIONID': 'd05aa6b6-5aa9-4bce-bed9-8282929804cf'
        }

        self.name_pre = 'myy_'

    def run(self):
        # 创建商品
        for i in range(20):
            name = str(i)
            time.sleep(1)
            draftId = self.draft(name)
            self.submit(draftId)
            data = self.getGoodsSkuByCondition(self.name_pre + name)
            self.updateGoodsCategory(data[0])

        # 手动数据库添加一下库存

        # 商品上架
        for i in range(1):
            name = str(i)
            time.sleep(1)
            data = self.getGoodsSkuByCondition(self.name_pre + name)
            self.batchUpdownSku(data[0], data[1])

    def draft(self, name):
        par = {
            'url': 'https://scmpdc-test05.dongfangfuli.com/goodsManager/spu/draft',
            'data': {"supplierId": "10000629",
                     "basicInfo": {"source": 2, "skuType": 1, "spuDetail": None, "name": "xjh_auto_001",
                                   "subtitle": None, "saleUnit": "台", "stockUnit": None, "brandId": 16220,
                                   "madeIn": "北京市北京", "enName": None, "enSubtitle": None, "comparableType": 6,
                                   "isImport": False, "manufactor": "0", "qcReport": None, "supplierSpuCode": None,
                                   "phytosanitaryCertificate": None, "declarationForm": None, "isOversea": False,
                                   "isDangerous": False, "isBrittle": False, "isLiquid": False,
                                   "certificationFileInfos": [
                                       {"fileType": 201, "fileUrl": None, "effectTime": None, "expiredTime": None},
                                       {"fileType": 202, "fileUrl": None, "effectTime": None, "expiredTime": None},
                                       {"fileType": 200,
                                        "fileUrl": "http://devimg.dongfangfuli.com/merchantSpu/picture/2f2d7616c8244eed90e47f612c1f1d0b.png",
                                        "effectTime": "2021-03-29", "expiredTime": "2021-04-03"}]},
                     "skuInfoParams": [
                         {"supplierSkuId": None, "specName": "规格1",
                          "specImageUrl": "http://devimg.dongfangfuli.com/merchantSpu/picture/4db88c56a2c54e4887977e86312d3662.png",
                          "productSpecProperties": [], "shipmentModel": None, "purchaseModelList": [1, 2],
                          "barCode": [],
                          "code": "29013812386019", "suggestPrice": 4, "netPrice": 1, "freight": 6, "jdUrl": None,
                          "tmallUrl": None, "otherUrl": None, "offlineSaleCertificate": None, "skuRemark": "1",
                          "warehouseStockExtInfoList": [
                              {"warehouseCode": "Warehouse1", "warehouseName": "【接口【上海】【普通】【self】",
                               "warehouseType": "1",
                               "minAlertStockQuantity": 1, "minPurchaseStockQuantity": 1},
                              {"warehouseCode": "Warehouse6", "warehouseName": "【接口】【北京+上海】【指定】【M1】",
                               "warehouseType": "2",
                               "minAlertStockQuantity": 1, "minPurchaseStockQuantity": 1}],
                          "warehouseList": [
                              {"id": 1, "placeNo": "ck01", "placeName": "仓库01百世1", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2, "placeNo": "ck02", "placeName": "仓库02复融", "placeSort": "1",
                               "placeSortname": "3PL自营仓",
                               "warehouseType": "1"},
                              {"id": 3, "placeNo": "ck03", "placeName": "仓库03（法网）", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 4, "placeNo": "ck04", "placeName": "仓库04百世", "placeSort": "1",
                               "placeSortname": "3PL自营仓",
                               "warehouseType": "1"},
                              {"id": 14, "placeNo": "14", "placeName": "有一多1123", "placeSort": "3",
                               "placeSortname": "商家仓",
                               "warehouseType": "3"},
                              {"id": 15, "placeNo": "15", "placeName": "有多多", "placeSort": None, "placeSortname": None,
                               "warehouseType": None},
                              {"id": 17, "placeNo": "17", "placeName": "无", "placeSort": None, "placeSortname": None,
                               "warehouseType": None},
                              {"id": 18, "placeNo": "18", "placeName": "凑数的 ", "placeSort": None, "placeSortname": None,
                               "warehouseType": None},
                              {"id": 41, "placeNo": "41", "placeName": "aa", "placeSort": None, "placeSortname": None,
                               "warehouseType": None},
                              {"id": 45, "placeNo": "45", "placeName": "测试仓1", "placeSort": None, "placeSortname": None,
                               "warehouseType": None},
                              {"id": 62, "placeNo": "62", "placeName": "归属感虽然", "placeSort": None,
                               "placeSortname": None,
                               "warehouseType": None},
                              {"id": 197, "placeNo": "197", "placeName": "冒烟测试---000", "placeSort": None,
                               "placeSortname": None, "warehouseType": None},
                              {"id": 203, "placeNo": "203", "placeName": "百事可乐的配送范围", "placeSort": None,
                               "placeSortname": None, "warehouseType": None},
                              {"id": 270, "placeNo": "270", "placeName": "pdd001", "placeSort": None,
                               "placeSortname": None,
                               "warehouseType": None},
                              {"id": 312, "placeNo": "312", "placeName": "1", "placeSort": None, "placeSortname": None,
                               "warehouseType": None},
                              {"id": 347, "placeNo": "347", "placeName": "仓转换1单仓(28)-同步PHP仓库", "placeSort": "3",
                               "placeSortname": None, "warehouseType": "3"},
                              {"id": 520, "placeNo": "520", "placeName": "仓转换1多仓(3)-同步PHP仓库", "placeSort": "3",
                               "placeSortname": None, "warehouseType": "3"},
                              {"id": 526, "placeNo": "526", "placeName": "仓转换1多仓(2)-同步PHP仓库", "placeSort": "3",
                               "placeSortname": None, "warehouseType": "3"},
                              {"id": 537, "placeNo": "537", "placeName": "仓转换1单仓(1751)-同步PHP仓库", "placeSort": "3",
                               "placeSortname": None, "warehouseType": "3"},
                              {"id": 546, "placeNo": "546", "placeName": "仓转换1多仓(2)-同步PHP仓库", "placeSort": "3",
                               "placeSortname": None, "warehouseType": "3"},
                              {"id": 719, "placeNo": "202006181521", "placeName": "捷泰仓库", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 734, "placeNo": "202006231617", "placeName": "DN3PL自营仓001（复融）", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 753, "placeNo": "202006281552", "placeName": "卡卡卡西自营百世01", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 772, "placeNo": "202006301426", "placeName": "B3pl自营复融仓", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 775, "placeNo": "202006301451", "placeName": "E3pl自营复融仓", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 777, "placeNo": "202006301501", "placeName": "H3pl自营未对接仓", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 779, "placeNo": "202006301507", "placeName": "G3pl自营未对接仓", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 785, "placeNo": "ck08", "placeName": "东福自营仓库", "placeSort": "3",
                               "placeSortname": "自营仓",
                               "warehouseType": "3"},
                              {"id": 819, "placeNo": "32131231212", "placeName": "配送仓库一号", "placeSort": "3",
                               "placeSortname": "商家仓", "warehouseType": "3"},
                              {"id": 820, "placeNo": "131231231", "placeName": "新增仓库一号", "placeSort": "3",
                               "placeSortname": "商家仓", "warehouseType": "3"},
                              {"id": 834, "placeNo": "07081542", "placeName": "WD新捷泰仓库", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 841, "placeNo": "202007101533", "placeName": "111自动应答自动预约自营复融", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 843, "placeNo": "202007101538", "placeName": "110自动应答非自动预约自营捷泰", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 845, "placeNo": "202007101555", "placeName": "100自动应答非自动预约自营捷泰", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 847, "placeNo": "PGCCK01_001", "placeName": "皮革厂仓库001", "placeSort": "3",
                               "placeSortname": "商家仓", "warehouseType": "3"},
                              {"id": 855, "placeNo": "202007161457", "placeName": "111自动应答自动预约自营捷泰", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 856, "placeNo": "202007161525", "placeName": "111自动应答自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 857, "placeNo": "202007161644", "placeName": "111自动应答自动预约3pl非百世复融捷泰",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 859, "placeNo": "202007170911", "placeName": "111自动应答自动预约3自营仓", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 861, "placeNo": "PGCCK01", "placeName": "江南皮革厂上海仓", "placeSort": "3",
                               "placeSortname": "商家仓", "warehouseType": "3"},
                              {"id": 866, "placeNo": "23423423423", "placeName": "上海仓库", "placeSort": "3",
                               "placeSortname": "商家仓", "warehouseType": "3"},
                              {"id": 867, "placeNo": "12312312", "placeName": "北京仓库", "placeSort": "3",
                               "placeSortname": "商家仓", "warehouseType": "3"},
                              {"id": 869, "placeNo": "202007221755", "placeName": "供应商77的自营仓地点002", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 873, "placeNo": "234232342", "placeName": "北京仓库", "placeSort": "3",
                               "placeSortname": "商家仓", "warehouseType": "3"},
                              {"id": 2515, "placeNo": "202007271339", "placeName": "111自动应答自动预约自营加盟百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2516, "placeNo": "202007271352", "placeName": "110自动应答非自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2517, "placeNo": "202007271354", "placeName": "110自动应答非自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2518, "placeNo": "202007271409", "placeName": "100自动应答非自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2519, "placeNo": "202007271412", "placeName": "100自动应答非自动预约自营加盟百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2520, "placeNo": "202007271414", "placeName": "101自动应答非自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2521, "placeNo": "202007271416", "placeName": "101自动应答非自动预约自营加盟百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2522, "placeNo": "202007271418", "placeName": "000非自动应答非自动预约自营加盟百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2523, "placeNo": "202007271420", "placeName": "000非自动应答非自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2524, "placeNo": "202007271422", "placeName": "011非自动应答自动预约自营加盟百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2525, "placeNo": "202007271423", "placeName": "011自动应答自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2526, "placeNo": "202007271425", "placeName": "001非自动应答非自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2527, "placeNo": "202007271427", "placeName": "001非自动应答非自动预约自营加盟百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2528, "placeNo": "202007271428", "placeName": "010非自动应答非自动预约自营加盟百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2529, "placeNo": "202007271430", "placeName": "010非自动应答非自动预约自营best百世",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2530, "placeNo": "202007272059", "placeName": "结算单的自营百世best仓库", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2531, "placeNo": "202007272103", "placeName": "结算单的自营百世加盟仓库", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2560, "placeNo": "xjh001", "placeName": "徐敬浩自营仓库", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2584, "placeNo": "SHANGHAI001", "placeName": "全国仓", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 2600, "placeNo": "ck08v1", "placeName": "东福自营虚拟1", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 2616, "placeNo": "20200907", "placeName": "111自营实体仓库", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 2639, "placeNo": "202009161023", "placeName": "自营未对接", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 2655, "placeNo": "Warehouse1", "placeName": "【接口【上海】【普通】【self】", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2656, "placeNo": "Warehouse2", "placeName": "【接口】【北京】【精准】【self】", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2657, "placeNo": "Warehouse3", "placeName": "【接口】【北京+上海】【指定】【self】",
                               "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2665, "placeNo": "102601", "placeName": "102601的3pl自营仓", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2666, "placeNo": "102602", "placeName": "102602的名称改", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2667, "placeNo": "102603", "placeName": "102603的自营仓", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 2668, "placeNo": "102604", "placeName": "102604的自营仓名称改", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 2692, "placeNo": "102811", "placeName": "102811名称", "placeSort": "5",
                               "placeSortname": "直营门店", "warehouseType": "5"},
                              {"id": 2732, "placeNo": "202011041726", "placeName": "自营未对接仓库", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 2737, "placeNo": "110905", "placeName": "110905虚拟直营门店", "placeSort": "5",
                               "placeSortname": "直营门店", "warehouseType": "5"},
                              {"id": 2747, "placeNo": "111001", "placeName": "111001自营仓", "placeSort": "3",
                               "placeSortname": "自营仓", "warehouseType": "3"},
                              {"id": 2748, "placeNo": "202011131538", "placeName": "接口-WD-3PL勿动仓库", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2759, "placeNo": "wqzy", "placeName": "新增地点档专用仓库", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2771, "placeNo": "987654321", "placeName": "忘优", "placeSort": "4",
                               "placeSortname": "商家门店", "warehouseType": "4"},
                              {"id": 3073, "placeNo": "SFSJ", "placeName": "双捷仓库", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 3973, "placeNo": "120501", "placeName": "151501名称1", "placeSort": "4",
                               "placeSortname": "商家门店", "warehouseType": "4"},
                              {"id": 3974, "placeNo": "120502", "placeName": "151501名称1", "placeSort": "4",
                               "placeSortname": "商家门店", "warehouseType": "4"},
                              {"id": 3986, "placeNo": "BSGZ", "placeName": "百世广州仓", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 3987, "placeNo": "BSBJ", "placeName": "百世北京仓", "placeSort": "1",
                               "placeSortname": "3PL自营仓", "warehouseType": "1"},
                              {"id": 2652, "placeNo": "Warehouse4", "placeName": "【接口】【上海】【普通】【M1】", "placeSort": "2",
                               "placeSortname": "商家仓", "warehouseType": "2"},
                              {"id": 2653, "placeNo": "Warehouse5", "placeName": "【接口】【北京】【精准】【M1】", "placeSort": "2",
                               "placeSortname": "商家仓", "warehouseType": "2"},
                              {"id": 2654, "placeNo": "Warehouse6", "placeName": "【接口】【北京+上海】【指定】【M1】",
                               "placeSort": "2",
                               "placeSortname": "商家仓", "warehouseType": "2"}],
                          "warehouseIds": ["Warehouse1", "Warehouse6"],
                          "index": 0, "jdPrice": None, "jdCommentsQuantity": None, "tmallPrice": None,
                          "tmallCommentsQuantity": None, "otherPrice": None, "otherCommentsQuantity": None,
                          "offlinePrice": None}],
                     "storeInfo": {"storeCondition": 1, "storeConditionDetail": None, "isExpireDateManagement": False},
                     "packageInfo": {"grossWeight": 8, "singleGrossWeight": 8, "singleNetWeight": 8, "packageBill": "8",
                                     "singleBoxLength": 8, "singleBoxHeight": 8, "singleBoxWidth": 8, "boxLength": 8,
                                     "boxWidth": 8, "boxHeight": 8},
                     "supplyInfo": {"supplyStart": None, "supplyEnd": None, "isSaleReturn": False, "quantityInBox": 1,
                                    "isPurchaseByBox": False}, "backCategoryId": "302",
                     "standardPicInfos":
                         [
                             {"seq": 0,
                              "url": "http://devimg.dongfangfuli.com/merchantSpu/picture/3e7f0f03850b4a7db39549f93edf1ff8.jpg",
                              "picType": 2},
                             {"seq": 1,
                              "url": "http://devimg.dongfangfuli.com/merchantSpu/picture/289ea5dd0ee34267ae5c4346b175ab0a.png",
                              "picType": 2},
                             {"seq": 2,
                              "url": "http://devimg.dongfangfuli.com/merchantSpu/picture/65c50f0deee340ac9e5192ca9767944e.jpg",
                              "picType": 2},
                             {"seq": 3,
                              "url": "http://devimg.dongfangfuli.com/merchantSpu/picture/723e1302e8aa4c67b608addbd5095800.jpg",
                              "picType": 2},
                             {"seq": 4,
                              "url": "http://devimg.dongfangfuli.com/merchantSpu/picture/efc490dc4b8c47f5b3290acc84fba28a.jpg",
                              "picType": 2},
                             {"seq": 5,
                              "url": "http://devimg.dongfangfuli.com/merchantSpu/picture/3d1354c168a141188ca863de22a52f82.jpg",
                              "picType": 2},
                             {"seq": 6,
                              "url": "http://devimg.dongfangfuli.com/merchantSpu/picture/0d38f8d384d747c0b5b26f57d95b379a.jpg",
                              "picType": 2},
                             {"seq": 7,
                              "url": None,
                              "picType": 2},
                             {"seq": 8,
                              "url": None,
                              "picType": 2},
                             {"seq": 9,
                              "url": None,
                              "picType": 2}],
                     "h5PicInfos": [{"seq": 0, "url": None, "picType": 2}, {"seq": 1, "url": None, "picType": 2},
                                    {"seq": 2, "url": None, "picType": 2},
                                    {"seq": 3, "url": None, "desc": "商品卖点细节图,白底", "picType": 2},
                                    {"seq": 4, "url": None, "picType": 2}, {"seq": 5, "url": None, "picType": 2},
                                    {"seq": 6, "url": None, "picType": 2}, {"seq": 7, "url": None, "picType": 2},
                                    {"seq": 8, "url": None, "picType": 2}, {"seq": 9, "url": None, "picType": 2}],
                     "brochurePicUrl": None, "detailPicList": [], "detailH5PicList": [],
                     "properties": {"2": "8", "4": "8", "5": "8", "6": "", "10": "5", "12": "", "13": ""},
                     "supplierSpuId": None, "draftNumber": None, "processId": None}
        }

        par['data']['basicInfo']['name'] = self.name_pre + str(name)
        par['data']['skuInfoParams'][0]['code'] = get_time()

        data = requests.post(par['url'], json=par['data'], headers=self.headers, cookies=self.cookies)
        if data.status_code == 200:
            data = json.loads(data.text)
            print(data)
            return data['data']['draftId']

    def submit(self, draftId):
        par = {
            'url': 'https://scmpdc-test05.dongfangfuli.com/goodsManager/spu/submit',
            'data': {"draftId": draftId, "supplierId": "10000629", "channelIds": [2]}
        }
        data = requests.post(par['url'], json=par['data'], headers=self.headers, cookies=self.cookies)
        if data.status_code == 200:
            data = json.loads(data.text)
            if data['respCode'] == '00000000':
                return True
        print('cw')

    def getGoodsSkuByCondition(self, name):
        par = {
            'url': 'https://scmpdc-test05.dongfangfuli.com/merchant/goods/getGoodsSkuByCondition',
            'data': {"pageNum": 1, "pageSize": 20, "backCategoryId": None, "comparableTypeId": None,
                     "frontCategoryId": None, "createTimeArray": [], "putawayTimeArray": [], "soldoutTimeArray": [],
                     "putawayTimeArray2": [], "soldoutTimeArray2": [], "merchantSkuName": name}
        }
        data = requests.post(par['url'], json=par['data'], headers=self.headers, cookies=self.cookies)
        if data.status_code == 200:
            data = json.loads(data.text)
            if data['respCode'] == '00000000':
                return [data['data']['list'][0]['skuCode'], data['data']['list'][0]['skuId']]
        print('cwwww')

    def updateGoodsCategory(self, skucode):
        skucode = str(skucode)
        par = {
            'url': "https://scmpdc-test05.dongfangfuli.com/goods/operation/category/updateGoodsCategory",
            'data': {"paramList": [
                {"skuCode": skucode, "merchantId": "1", "channel": "优选生活", "category": 165},
                {"skuCode": skucode, "merchantId": "1", "channel": "生日汇", "category": 19},
                {"skuCode": skucode, "merchantId": "1", "channel": "东福超市", "category": 2000228},
                {"skuCode": skucode, "merchantId": "1", "channel": "图书", "category": 2000226}]}
        }
        data = requests.post(par['url'], json=par['data'], headers=self.headers, cookies=self.cookies)
        if data.status_code == 200:
            data = json.loads(data.text)
            if data['respCode'] == '00000000':
                return True
        print('cww')

    def batchUpdownSku(self, skuCode, skuId):
        par = {
            'url': 'https://scmpdc-test05.dongfangfuli.com/merchant/goods/batchUpdownSku',
            'data': {
                "paramList": [{"skuCode": skuCode, "merchantId": "1", "skuId": skuId, "checkUpInfo": []}],
                "channels": ["2", "3", "17", "998"], "skuSaleStatus": "UP", "offReasonTag": "", "offReason": None}
        }
        data = requests.post(par['url'], json=par['data'], headers=self.headers, cookies=self.cookies)
        if data.status_code == 200:
            data = json.loads(data.text)
            print(data)
            if data['respCode'] == '00000000':
                return True
        print('cww')


if __name__ == '__main__':
    x = AddGoods()
    x.run()
