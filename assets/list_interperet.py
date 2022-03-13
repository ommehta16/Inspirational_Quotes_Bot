import pyautogui
#use [STRING].strip() and [STRING].replace()
#Take quotes  ✔
#replace — w/ - ✔
#split on linebreak ✔
#For all quotes w/ quotation marks, if next line has -, and NOT ", we kill the "-", zip them together, string the tuple, replace the "," with "-"
#If a line does not have a friend to help it out, it gets killed
class listmaker:
    @staticmethod
    def fixdash(thing: str):
        return thing.replace("—", "-")
    @staticmethod
    def validify_quotes(quotes: list):
        thingy = list()
        for i in range(len(quotes) - 1):
            if ' ' in quotes[i]:
                if '-' in quotes[i+1]:
                    workingstring = quotes[i]+quotes[i+1]
                    for i in range(10):
                        workingstring = workingstring.replace(str(i),"")
                    workingstring = workingstring.replace("\n","")
                    thingy.append(workingstring)
        return thingy[:]