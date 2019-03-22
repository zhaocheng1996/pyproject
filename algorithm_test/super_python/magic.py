'''
魔法函数练习，双下划线
'''

class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list
    # def __getitem__(self, item):
    #     return self.employee[item]
    def __str__(self):
        return "'".join(self.employee)
company = Company(['zhangsan','lisi','wangwu'])

#没有写__getitem__的时候，要有这一句才能遍历
# employee = company.employee
# for item in employee:
#     print(item)

# for item in company:
#     print(item)

print(company)#zhangsan'lisi'wangwu






