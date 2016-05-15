

class Turing:

    def __init__(self, ruels_file_name, data_file_name):
        '''список с правилами в виде: состояние текущее_значение новое_значени новое_состояние смена_позиции разрешение_на_завершение_работы'''
        f = open(ruels_file_name, 'r')
        self.ruels = []
        while True:
            line = f.readline()
            if not line:  break
            content = line.strip().split(' ')
            if len(content) > 6:
                raise SyntaxError('Правила поведения машины описаны некорректно')
            self.ruels.append(content)
        f.close()
        
        '''входные данные '''        
        d = open(data_file_name, 'r')        
        line = d.readline()
        self.data  = line.strip()      
        d.close()
        
        '''начальное состояяние машины'''
        self.pos = 0
        self.state = 'first'
        self.permission_to_exit = 'no'
        self._otchet = ['начальное состояние: '+ self.state + ' начальная позиция: '+ str(self.pos) + ' начальные данные: ' + self.data ]     

    def step(self):
       for content in self.ruels:   
          if  self.pos < len(self.data) and self.pos > -1 and content[0] == self.state and self.data[self.pos] == content[1]:
                 self.state = content[3]
                 self.data = self.data[0:self.pos] + content[2] + self.data[self.pos+1:len(self.data)+1]
                 if content[4] == '>': self.pos += 1
                 elif content[4] == '<': self.pos -= 1
                 elif content[4] == '=': pass
                 self.permission_to_exit = content[5]
                 self._otchet.append('новое состояние: '+ self.state + ' текующая позиция: '+ str(self.pos) + ' новые данные: ' + self.data )
                 break
          elif content[0] == self.state and (self.pos) == len(self.data) and content[1] == '#':
                 self.data = self.data + content[2]
                 self.state = content[3]
                 self.permission_to_exit = content[5]
                 if content[4] == '>': self.pos += 1
                 elif content[4] == '<': self.pos -= 1
                 elif content[4] == '=': pass
                 break
                
          elif self.pos < 0 and content[0] == self.state and content[1] == '#':
                 self.data = content[2] + self.data       
                 self.state = content[3]
                 self.permission_to_exit = content[5]
                 if content[4] == '>': self.pos += 1
                 elif content[4] == '<': self.pos -= 1
                 elif content[4] == '=': pass
                 break
       
    def otchet(self):
        for elem in self._otchet:
               print(elem)
                    
    def main(self):       
       while self.permission_to_exit != 'yes': 
                 self.step() 
                 
                
          
                    










