#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 14:27
# @Author  : Anran
# @File    : InterfaceUseCaseParameterExplosion.py
# @Function:
from allpairspy import AllPairs


class Lucpe(object):

    def init(self, url, method, headers, data, fission)-> str:
        """
        :param url: url
        :param method: get or post
        :param headers: headers
        :param data: params
        :param fission: rules
        :return:
        """
        if url:
            self.url = url
        if method:
            self.method = method
        if headers:
            self.headers = headers
        if isinstance(eval(data), dict):
            self.data = data
        else:
            return "data must dict"
        if isinstance(fission, list):
            self.fission = fission
        else:
            return "fission must list"

    def get_interface_parameter(self):
        """
        get interface parameter
        :return:
        """
        results = []
        parms = eval(self.data)
        fission_list = self.fission
        for i, pairs in enumerate(AllPairs(fission_list)):  # 有几种组合就会遍历几次
            new_parms = {}
            for m in pairs:
                parm = parms
                if isinstance(parm, dict):
                    for k, v in parm.items():
                        if k not in new_parms:
                            if isinstance(v, dict):
                                dict_kk = {}
                                for k1, v1 in v.items():
                                    if k1 not in dict_kk:
                                        dict_kk[k1] = m
                                new_parms[k] = dict_kk
                            elif isinstance(v, list):
                                list_kk = []
                                for v2 in v:
                                    kk = {}
                                    if isinstance(v2, dict):
                                        for k3, v3 in v2.items():
                                            if k3 not in kk:
                                                kk[k3] = m
                                    list_kk.append(kk)
                                new_parms[k] = list_kk
                            else:
                                new_parms[k] = m
                                break
            results.append(new_parms)
        fission_data = []
        for result in results:
            api_case_fission = {}
            api_case_fission['url'] = self.url
            api_case_fission['method'] = self.method
            api_case_fission['headers'] = self.headers
            api_case_fission['data'] = result
            fission_data.append(api_case_fission)
        return fission_data


if __name__ == "__main__":
    l = Lucpe()
    l.init("/backend-api/get-transfer-info", "POST",
           "{}", "{'complaint_type': '', 'city_id': '', 'order_id': ''}", [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
    result = l.get_interface_parameter()
    print(result)