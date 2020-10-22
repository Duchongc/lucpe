# InterfaceUseCaseParameterExplosion
## init  
###  url 接口url
###  method 接口请求方式
###  headers  接口请求头
###  fission 需要参与用例爆炸的列表
#### 元组形式的列表，如果接口参数有2个，那么格式是[[],[]]
#### 元组形式的列表，如果接口参数有三个，那么格式是[[],[],[]]
#### 在二维数组里写一个key对应的用例情况，比如，空，非空，长度，错误的
####  [["a", "1", ""],[["a", "1", ""],[["a", "1", ""]]    
###  data 接口参数   {"key":[{"k1": "value", "k2":"v2"}, {"k1": "value", "k2":"v2"}]}
###  return 最终的返回结果 [{"url":url, "method":"post", "headers":"", "data":{}},{"url":url, "method":"post", "headers":"", "data":{}}]


[Github-flavored Markdown](git@github.com:Duchongc/lucpe.git)
