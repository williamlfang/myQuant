from pytdx.hq import  TdxHq_API
api=TdxHq_API()

with api.connect():
     data=[]
     for i in range(10):
        data+=api.get_security_bars(9,0,'000001',(9-i)*800,800)
print(api.to_df(data))

from pytdx.hq import  TdxHq_API
api=TdxHq_API()


def get_all_day_data():
    with api.connect():
         data=[]
         for i in range(10):
            data+=api.get_security_bars(9,0,'000001',(9-i)*800,800)
    print(api.to_df(data))
