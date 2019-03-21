# 定义逆向最大匹配类
class IMM(object):

    # 初始化得到给定的字典中的所有词和长度最大的词
    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximum = 0
        #读取词典
        with open(dic_path, 'r', encoding='utf8') as f:
            for line in f:
                # strip():只能删除开头或是结尾的字符，不能删除中间部分的字符
                line = line.strip()
                print('line:',line)
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line)>=self.maximum:
                    self.maximum = len(line)

            print('self.dictionary:',self.dictionary,'\n','self.maximum:',self.maximum)

    # 该方法可切分新得到的词组
    def cut(self, text):
        result = []
        index = len(text)
        print('index:',index)
        while index > 0:
            word = None
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue
                print('index - size=>',index - size,':',index)
                piece = text[(index - size):index]
                print('piece:',piece)
                # 判断该词是否在词典中
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
        return result[::-1]

def main():
    text = "南京市长江大桥"
    # 词典的地址
    tokenizer = IMM('四十万汉语大词库.txt')
    print(tokenizer.cut(text))

main()