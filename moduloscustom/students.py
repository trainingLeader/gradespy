import moduloscustom.utilscustoms as uc
import moduloscustom.mensajes as msg
def addStudent(src:list):
    isAddStudent = True
    while(isAddStudent):
        nombre = input('Ingrese el nombre del estudiante :')
        student = [nombre,[],[],[]]
        src.append(student)
        isAddStudent = uc.validateData(msg.messagest)
