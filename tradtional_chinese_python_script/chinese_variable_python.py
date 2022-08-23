# 一個盡量用繁體中文寫的眼鏡蛇程式語言
打印 = print
字典 = {'鍵':'值'}
列表 = ['元素']
數字 = {'零':0, 
        '壹':1,
        '貳':2,
        '參':3,
        '肆':4,
        '伍':5,
        '陸':6,
        '柒':7,
        '捌':8,
        '玖':9,
        '拾':10}
def 函數(數值):
    打印(數值)
    打印(列表[數字['零']])
    for 鍵 in 字典:
        打印(字典[鍵])

if __name__ == '__main__':
    for 鍵 in 數字:
        函數(數字[鍵])