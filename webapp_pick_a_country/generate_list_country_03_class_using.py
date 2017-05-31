# -*- coding: utf-8 -*- 
# 使用模块module country
import country  
c = country.country_list_name()

# 測試   
print (c.country_name('CN'))
print (c.country_name('SG'))
print (c.country_name('ZZ'))
print (c.country_name('ABC'))
print (c.country_name(''))
 
