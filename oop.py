import os
os.system('cls' if os.name == 'nt' else 'clear')

# def print_type(data):
#     for i in data:
#         print(i,type(i))

# test = [122,"Ömer",[1,2,3],(1,2,3),{1,2,3},True]
# print_type(test)

# class Person:
#     name = "Ömer"
#     age = 45

# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)

# Person.job = "Teacher"
# print(person1.job)

# #class attributes vs instance attributes

# person1.location = "Turkey"
# print(person1.location)
# # print(person2.location)

# person2.name = "Aaron"
# print(person2.name)
# print(person1.name)

#SELF keyword
# Classlar ile instance'ler arasında bağlantı kurmak için "self" kullanılır.
# class Person:
#      name = "Ömer"
#      age = 45
     
#      def test(self):
#         print("Hello World")

#      def set_details(self,name,age)  #Burada classlardan ziyade instancelere özellik verdik.
#          self.name = name
#          self.age = age

#      def get_details(self):
#          print(self.name,self.age)
       
# person1 = Person()
# person1.test() 
# Person.test(person1)  

# person1.get_details() #Burada instance tanımlaması yapmadığımız için class özelliklerini alacak ve (ömer,45) dönecek.
# person1.set_details("Faruk",28)
# person1.get_details() #Burada üst satırda tanımladığımız için instance değerlerini yani(faruk,28) döndürecek.

#static method

# class Person:
#      company="Clarusway"

#      def set_details(self,name,age):
#          self.name = name
#          self.age = age

#      def get_details(self):
#          print(self.name,self.age)
       
#      @staticmethod    #Bu func. instanceden bağımsız olarak çalışır.Bu tarz methodlara static method denir.
#      def salute():
#          print("Hi there!")

# person1 = Person()
# person1.salute()

#special methods

# class Person:
#     compony= "Clarusway"

#     def __init__(self,name,age): #Burada init jsdeki constructor görevi görür.Kendi otomatik çalışır.
#         self.name = name
#         self.age = age

#     def __str__(self): #Bu method sayesinde,print(person1) dediğimizde instance değerleri yerine hafızadaki adresini gösterir. __str__ ile instance değerlerine ulaşılabilir.
#         return f"{self.name}{self.age}"    

#     def get_details(self):
#        print(self.name, self.age)

# person1 = Person( "Ömer" , 28)
# person1.get_details()

# liste = [4,2,9,11,5]
# print(liste)
# print(person1)
# print(person1.__str__())

# encapsulatıon and abstraction

# class Person:
#     compony= "Clarusway"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self._id=5000 #Önünde _ görürseniz (_id) bunu değiştirmeyin !!!! Private demek istiyor.
#         self.__id2 = 4000
#     def __str__(self):
#         return f"{self.name}{self.age}"    

#     def get_details(self):
#        print(self.name, self.age)
# person1=Person("Ömer",28)
# print(person1._id)
# # print(person1.__id2) # Böyle ulaşamayız.
# print(person1._Person__id2)  #Böyle ulaşmamız gerekiyor.

# liste = [4,2,9,11,5]
# liste.sort()
# print(liste) 
#Kullanıcıyı gereksiz detaylardan soyutlama işlemine "Abstruction" denir.

#inheritance and polymorphism

class Person:
     company= "Clarusway"

     def __init__(self,name,age):
         self.name = name
         self.age = age
         
     def __str__(self):
         return f"{self.name}{self.age}"    

     def get_details(self):
       print(self.name, self.age)

class Lang:
     def __init__(self,langs):
         self.langs = langs
     def display_langs(self):
         print(self.langs)


class Employee(Person,Lang):  #Burada (person) diyerek inheritance yani miras yoluyla person değerlerini employee clasına aktardık.
        def __init__(self,name,age,path,langs):
        #  self.name = name
        #  self.age = age
         super().__init__(name,age)  #super() ile parenta yani persona ulaşıyoruz.name ve age işlemleri personda yapıldı path işlemi employeede yapıldı
                                    #bu şekilde age ve name değerleri persondan path değeri employee clasından alınmış oldu.
         self.path = path
         Lang.__init__(self,langs)
        #  self.langs = langs 
        # Yukarıda multiple inheritance yaptık ve hem persondan hemde langtan miras aldık.Burada super__init__ dediğimizde
        #ilk class yani person değerlerini getirdi.Bu sebepten biz lang özelliklerine ulaşamadık.Bunun için üst satırdaki gibi "self.langs = langs"
        #dememiz gerekir yada ismen "Lang.__init__(self,langs)" şeklinde çağırabiliriz.!!!!!Buradan çıkarılacak sonuç super()ile sadece ilk class
        #örnekteki person değerlerini getirir.!!!


#Override  
#Hazır classlardaki özellikler üzerinde değişiklik yapma işlemine "override" denir.
        def get_details(self):
            #  print(self.name, self.age, self.path)  bu şekilde olabilir.
            super().get_details() #Bu kısımda mevcut haliyle get_details() çağırdık ve alt satırda üzerine self.path özelliğ eklemiş olduk.
            print(self.path) # super ilede yapabiliriz.

emp1=Employee("Ömer", 28 , "FS",["Python","JavaScript"])
emp1.get_details()
emp1.display_langs()


print(Employee.mro())  #Bir classın soyağıcını görmek istersek classAdı.mro() ile ulaşılabilir.