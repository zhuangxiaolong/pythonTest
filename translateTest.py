from translate import Translator
import string


def myTranslator(str):
    #准备翻译
    translator= Translator(to_lang="zh")
    result=""

    word=""
    for i,s in enumerate(str):
       if s=="_":
          #print(word)
          #translation = translator.translate(word)
          result=result+" "+word 
          word=s
          continue
       if s.isupper():
           if i==0:
               word=word+s
           else:
               if word.find("_")!=-1:
                   if len(word)==2:
                      word=s
                      continue
                  
               #print(word)
               if  word=="Get":
                   word=s
                   result=result+"获取"  #我也不知道为什么Get翻译不出来
               else:
                   result=result+" "+word 
                   #translation = translator.translate(word)
                   word=s  
       else:
          word=word+s
        
        #如果是最后的字符
       if i==len(str)-1:
               #translation = translator.translate(word)
               result=result+" "+word 

    translation = translator.translate(result)
    return translation
               
result=myTranslator("GetHome_jPage")
print("Done："+result)
result=myTranslator("GetHome_mPage")
print("Done："+result)


