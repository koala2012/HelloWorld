#! /usr/bin/env
#coding:utf-8

# import sys
# import os

# class Robot():
#     def __init__(self):
#         pass
    
#     def string_mapping(self):
#         encode_str = '6ipsyvaxztr23q5f0l9g81uhek4bjodwmcn7'
#         decode_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
#         encode_list = list(encode_str)
#         decode_list = list(decode_str)
        
#         print encode_list
#         print decode_list
        
#         mapping_list = {}
#         for item in encode_list:
#             mapping_list[item] = decode_list[int(encode_list.index(item))]
        
#         return mapping_list
    
#     def covert_str(self,input_str,mapping_list):
#         out_str = ''
#         temp = ''
#         input_str_list = list(input_str)
#         for item in input_str_list:
#             if item == ' ':
#                 temp = ' '
#             elif item == '-':
#                 temp = '-'
#             else:
#                 temp = mapping_list[item]
#             out_str +=temp
#         return out_str
    
# if __name__ == "__main__":
#     robot = Robot()
#     mapping_ls = robot.string_mapping()
#     input_str = 'xxegea49 iwepajd0wep soe-'
#     print 'decode string is -->'
#     print robot.covert_str(input_str,mapping_ls)

#! usr/bin/env
#coding:utf-8

import os
import sys

class ConvertSentence():
    
    def __init__(self):
        pass
    
    def convert_word(self, input_str):
        input_str_ls = input_str.split(' ')
        print input_str_ls
        return ' '.join(input_str_ls[::-1])

if __name__ == "__main__":
    convert = ConvertSentence()
    input_str = 'how are you'
    print "after coverted sentence is-->"
    print convert.convert_word(input_str)

            