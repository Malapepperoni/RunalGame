class Dog():
    """一次模拟的简单尝试"""

    def __init__(self,name,age):
          """初始化属性"""
          self.name = name
          self.age  = age
    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting。")
    def over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!") 

my_dog = Dog('while',6)       

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

my_dog.sit()

you_dog = Dog('lucy',8)